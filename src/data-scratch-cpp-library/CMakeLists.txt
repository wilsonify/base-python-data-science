cmake_minimum_required(VERSION 3.14)
project(data-scratch-cpp-library LANGUAGES CXX)
set(VERSION_MAJOR 1)
set(VERSION_MINOR 0)

set(CMAKE_CXX_STANDARD 20) # Use C++20 for ranges, operator<=>, and other modern features
set(CMAKE_CXX_FLAGS="-g -O0 -Wall -W -Wshadow -Wunused-variable -Wunused-parameter -Wunused-function -Wunused -Wno-system-headers -Wno-deprecated -Woverloaded-virtual -Wwrite-strings")
set(CMAKE_C_FLAGS="-g -O0 -Wall -W")
set(CMAKE_SHARED_LINKER_FLAGS="")
set(CMAKE_EXE_LINKER_FLAGS="")

# Build a shared library with core data science modules
include_directories(dscpp)

# Core implemented modules (ported from TypeScript)
set(CORE_MODULES
    c04_linear_algebra
    c05_statistics  
    c06_probability
    c11_machine_learning
    c12_k_nearest_neighbors
)

# Additional modules (original implementations, currently disabled due to compilation issues)
# To enable these modules, fix compilation errors first and add to CORE_MODULES
set(ADDITIONAL_MODULES
    # c07_hypothesis_and_inference  # Compilation errors
    # c08_gradient_descent          # Compilation errors
    # c10_working_with_data         # Needs testing
    # c13_naive_bayes               # Needs porting
    # c14_simple_linear_regression  # Needs porting
    # c15_multiple_regression       # Needs porting
    # c16_logistic_regression       # Needs porting
    # c17_decision_trees            # Needs porting
    # c18_neural_networks           # Needs porting
    # c20_clustering                # Needs porting
    # c22_network_analysis          # Needs testing
    # c23_recommender_systems       # Needs testing
    # c24_databases                 # Needs testing
    # c25_mapreduce                 # Needs testing
)

# Collect source files for core modules
foreach(module ${CORE_MODULES})
    FILE(GLOB ${module}Sources dscpp/${module}/*.cpp)
    list(APPEND ALL_SOURCES ${${module}Sources})
endforeach()

# Collect source files for additional modules
foreach(module ${ADDITIONAL_MODULES})
    FILE(GLOB ${module}Sources dscpp/${module}/*.cpp)
    list(APPEND ALL_SOURCES ${${module}Sources})
endforeach()

# Create the shared library
add_library(data-scratch-cpp-library SHARED ${ALL_SOURCES})

# Set library properties
set_target_properties(data-scratch-cpp-library PROPERTIES
    VERSION ${VERSION_MAJOR}.${VERSION_MINOR}
    SOVERSION ${VERSION_MAJOR}
    PUBLIC_HEADER "dscpp.h"
)

# Installation
install(TARGETS data-scratch-cpp-library
    LIBRARY DESTINATION lib
    PUBLIC_HEADER DESTINATION include
)

# Install headers for each module
foreach(module ${CORE_MODULES})
    install(DIRECTORY dscpp/${module}/
        DESTINATION include/dscpp/${module}
        FILES_MATCHING PATTERN "*.h"
    )
endforeach()

foreach(module ${ADDITIONAL_MODULES})
    install(DIRECTORY dscpp/${module}/
        DESTINATION include/dscpp/${module}
        FILES_MATCHING PATTERN "*.h"
    )
endforeach()
