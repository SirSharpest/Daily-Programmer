cmake_minimum_required(VERSION 3.3)
project(Daily_Programmer)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c11")

set(SOURCE_FILES "Genetic Algorithm/main.c")
add_executable(Daily_Programmer ${SOURCE_FILES})