cmake_minimum_required(VERSION 3.14)
project(data-scratch-cpp-library-tests LANGUAGES CXX)
set(VERSION_MAJOR 1)
set(VERSION_MINOR 0)

set(CMAKE_CXX_STANDARD 17) # Use C++17 for better testing features
set(CMAKE_CXX_FLAGS="-g -O0 -Wall -W -Wshadow -Wunused-variable -Wunused-parameter -Wunused-function -Wunused -Wno-system-headers -Wno-deprecated -Woverloaded-virtual -Wwrite-strings -fprofile-arcs -ftest-coverage")
set(CMAKE_C_FLAGS="-g -O0 -Wall -W -fprofile-arcs -ftest-coverage")
set(CMAKE_SHARED_LINKER_FLAGS="-fprofile-arcs -ftest-coverage")
set(CMAKE_EXE_LINKER_FLAGS="-fprofile-arcs -ftest-coverage")

# Add GoogleTest using system package if available, otherwise build from source
find_package(GTest QUIET)

if(NOT GTest_FOUND)
    # Build GoogleTest from source
    include(FetchContent)
    FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/v1.14.0.zip
    )
    # For Windows: Prevent overriding the parent project's compiler/linker settings
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)
endif()

# Include the library headers
include_directories(../dscpp)

# Build the data science library
FILE(GLOB datascratchcpplibrarySources ../dscpp/c04_linear_algebra/*.cpp 
                                        ../dscpp/c05_statistics/*.cpp 
                                        ../dscpp/c06_probability/*.cpp 
                                        ../dscpp/c11_machine_learning/*.cpp 
                                        ../dscpp/c12_k_nearest_neighbors/*.cpp)
add_library(data-scratch-cpp-library SHARED ${datascratchcpplibrarySources})
target_include_directories(data-scratch-cpp-library PUBLIC ../dscpp)

# Build tests
set(TEST_SOURCES
    test-dscpp/test_linear_algebra.cpp
    test-dscpp/test_statistics.cpp
    test-dscpp/test_probability.cpp
    test-dscpp/test_machine_learning.cpp
    test-dscpp/test_knn.cpp
)

add_executable(test-data-scratch-cpp ${TEST_SOURCES})

# Link with GoogleTest (either system package or built from source)
if(GTest_FOUND)
    target_link_libraries(test-data-scratch-cpp 
        GTest::gtest 
        GTest::gtest_main 
        data-scratch-cpp-library
    )
else()
    target_link_libraries(test-data-scratch-cpp 
        gtest 
        gtest_main 
        data-scratch-cpp-library
    )
endif()

# Add chrono for performance tests
target_link_libraries(test-data-scratch-cpp pthread)

# Enable testing
enable_testing()
add_test(NAME AllTests COMMAND test-data-scratch-cpp)

# Add individual tests for better reporting
add_test(NAME LinearAlgebraTests COMMAND test-data-scratch-cpp --gtest_filter="LinearAlgebra*")
add_test(NAME StatisticsTests COMMAND test-data-scratch-cpp --gtest_filter="Statistics*")
add_test(NAME ProbabilityTests COMMAND test-data-scratch-cpp --gtest_filter="Probability*")
add_test(NAME MachineLearningTests COMMAND test-data-scratch-cpp --gtest_filter="MachineLearning*")
add_test(NAME KNNTests COMMAND test-data-scratch-cpp --gtest_filter="KNN*")

# Set test properties
set_tests_properties(AllTests PROPERTIES TIMEOUT 300)
set_tests_properties(LinearAlgebraTests PROPERTIES TIMEOUT 60)
set_tests_properties(StatisticsTests PROPERTIES TIMEOUT 60)
set_tests_properties(ProbabilityTests PROPERTIES TIMEOUT 60)
set_tests_properties(MachineLearningTests PROPERTIES TIMEOUT 60)
set_tests_properties(KNNTests PROPERTIES TIMEOUT 120)

# Coverage support
option(ENABLE_COVERAGE "Enable coverage reporting" ON)
if(ENABLE_COVERAGE AND CMAKE_BUILD_TYPE STREQUAL "Debug")
    find_program(GCOV_PATH gcov)
    find_program(LCOV_PATH lcov)
    find_program(GENHTML_PATH genhtml)
    
    if(GCOV_PATH AND LCOV_PATH AND GENHTML_PATH)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage")
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --coverage")
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} --coverage")
        set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} --coverage")
        
        # Add coverage target
        add_custom_target(coverage
            COMMAND ${LCOV_PATH} --directory . --capture --output-file coverage.info
            COMMAND ${LCOV_PATH} --remove coverage.info '/usr/*' --output-file coverage.info
            COMMAND ${GENHTML_PATH} -o coverage coverage.info
            WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
            COMMENT "Generating code coverage report"
        )
    endif()
endif()

# Build an installer
include(InstallRequiredSystemLibraries)
set(CPACK_PACKAGE_NAME "data-scratch-cpp-library-tests")
set(CPACK_PACKAGE_VERSION_MAJOR "${VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${VERSION_MINOR}")
set(CPACK_SOURCE_GENERATOR "TGZ")
include(CPack)
