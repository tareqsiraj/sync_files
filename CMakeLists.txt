cmake_minimum_required(VERSION 3.12.4)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wshadow-all -Wextra -Wpedantic")

project(sync_files CXX)

option(COMPILER_COLORED_OUTPUT "Produce colored compiler output in GCC/Clang" ON)

if (${COMPILER_COLORED_OUTPUT})
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fcolor-diagnostics")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fcolor-diagnostics")
endif()


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(SOURCES
    src/main.cpp
)

add_executable(sync_files ${SOURCES})
target_link_libraries(sync_files
    PRIVATE
    CONAN_PKG::Boost
)
