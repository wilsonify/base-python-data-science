cmake_minimum_required(VERSION 3.14)
project(base-python-data-science LANGUAGES Fortran CXX)
set(VERSION_MAJOR 1)
set(VERSION_MINOR 0)

set(CMAKE_CXX_STANDARD 11) # GoogleTest requires at least C++11
set(CMAKE_CXX_FLAGS="-g -O0 -Wall -W -Wshadow -Wunused-variable -Wunused-parameter -Wunused-function -Wunused -Wno-system-headers -Wno-deprecated -Woverloaded-virtual -Wwrite-strings -fprofile-arcs -ftest-coverage")
set(CMAKE_C_FLAGS="-g -O0 -Wall -W -fprofile-arcs -ftest-coverage")
set(CMAKE_SHARED_LINKER_FLAGS="-fprofile-arcs -ftest-coverage")
set(CMAKE_EXE_LINKER_FLAGS="-fprofile-arcs -ftest-coverage")

# Fortran specific setup
ENABLE_LANGUAGE(Fortran)
set(CMAKE_Fortran_Compiler gfortran)
set(FORT_EXT .f90)
set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -cpp -g -fcheck=bounds  -fbacktrace")

#build the test runner
include_directories(external/googletest/googletest/include)
include_directories(external/googletest/googlemock/include)
add_subdirectory(external/googletest)
link_directories(external/googletest/build/lib)

# build a shared library
include_directories(src/data-scratch-cpp-library)
FILE(GLOB datascratchcpplibrarySources src/data-scratch-cpp-library/*.cpp)
add_library(data-scratch-cpp-library SHARED ${datascratchcpplibrarySources})
link_directories(${CMAKE_CURRENT_BINARY_DIR})

# build a test
FILE(GLOB testfizzbuzzerSources tests/test-data-scratch-cpp/*.cpp)
add_executable(test-data-scratch-cpp ${testfizzbuzzerSources} )
target_link_libraries(test-data-scratch-cpp gtest gtest_main data-scratch-cpp-library)

# build a fortran library
#include_directories(fortranlibrary)
#FILE(GLOB fortranlibrarySources fortran-library/*.f90)
#add_library(fortranlibrary SHARED ${fortranlibrarySources})
#set_target_properties(fortranlibrary PROPERTIES LINKER_LANGUAGE Fortran)
#link_directories(${CMAKE_CURRENT_BINARY_DIR})

enable_testing ()
add_test(run-test-data-scratch-cpp test-data-scratch-cpp)

# build an installer
include (InstallRequiredSystemLibraries)
set (CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/LICENSE")
set (CPACK_PACKAGE_NAME "base-python-data-science")
set (CPACK_PACKAGE_VERSION_MAJOR "${VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${VERSION_MINOR}")
set (CPACK_SOURCE_GENERATOR "TGZ")
include (CPack)