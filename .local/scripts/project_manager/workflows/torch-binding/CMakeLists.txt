cmake_minimum_required(VERSION 3.10)
project({{NAME_PLACEHOLDER}} LANGUAGES CXX CUDA)

find_package(Torch REQUIRED)
find_package(CUDA REQUIRED)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CUDA_STANDARD 14)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

add_library({{NAME_PLACEHOLDER}} SHARED
    lib/cpu/sample.cpp
    lib/cuda/sample.cu
)

target_link_libraries({{NAME_PLACEHOLDER}} ${TORCH_LIBRARIES})
set_property(TARGET {{NAME_PLACEHOLDER}} PROPERTY CXX_STANDARD 14)

if(APPLE)
    set_target_properties({{NAME_PLACEHOLDER}} PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
endif(APPLE)
