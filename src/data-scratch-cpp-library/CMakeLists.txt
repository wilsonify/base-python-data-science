cmake_minimum_required(VERSION 3.14)
project(data-scratch-cpp-library LANGUAGES CXX)
set(VERSION_MAJOR 1)
set(VERSION_MINOR 0)

set(CMAKE_CXX_STANDARD 11) # GoogleTest requires at least C++11
set(CMAKE_CXX_FLAGS="-g -O0 -Wall -W -Wshadow -Wunused-variable -Wunused-parameter -Wunused-function -Wunused -Wno-system-headers -Wno-deprecated -Woverloaded-virtual -Wwrite-strings -fprofile-arcs -ftest-coverage")
set(CMAKE_C_FLAGS="-g -O0 -Wall -W -fprofile-arcs -ftest-coverage")
set(CMAKE_SHARED_LINKER_FLAGS="-fprofile-arcs -ftest-coverage")
set(CMAKE_EXE_LINKER_FLAGS="-fprofile-arcs -ftest-coverage")

# build a shared library
include_directories(data-scratch-cpp-library)
FILE(GLOB datascratchcpplibrarySources *.cpp)
add_library(data-scratch-cpp-library SHARED ${datascratchcpplibrarySources})
link_directories(${CMAKE_CURRENT_BINARY_DIR})
