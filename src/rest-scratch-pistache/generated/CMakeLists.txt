cmake_minimum_required (VERSION 3.2)
project(api-server)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -pg -g3" )

set(VERSION_MAJOR 1)
set(VERSION_MINOR 0)
set(VERSION_PATCH 1)

set(CMAKE_EXPORT_COMPILE_COMMANDS true)

#build header only library
include_directories(external/json/include)

#build rapidjson
include_directories(external/rapidjson/include)
add_subdirectory(external/rapidjson)

#build the rest runner
include_directories(external/pistache/include)
add_subdirectory(external/pistache)
link_directories(external/pistache/build/src)

# build the main
include_directories(model)
include_directories(api)
include_directories(impl)

file(GLOB SRCS 
${CMAKE_CURRENT_SOURCE_DIR}/model/*.cpp
${CMAKE_CURRENT_SOURCE_DIR}/api/*.cpp
${CMAKE_CURRENT_SOURCE_DIR}/impl/*.cpp
${CMAKE_CURRENT_SOURCE_DIR}/*.cpp
)

add_executable(api-server ${SRCS}) 
target_link_libraries(api-server pistache pthread)
