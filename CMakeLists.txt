cmake_minimum_required(VERSION 3.12.4)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wshadow-all -Wextra -Wpedantic")

project(sync_files CXX)

set(SOURCES
    src/main.cpp
)

add_executable(sync_files ${SOURCES})
