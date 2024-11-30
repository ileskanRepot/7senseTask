cmake_minimum_required(VERSION 3.12)
project(getObjects LANGUAGES CXX)

# Require C++11 or newer
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include degub. Not required for final projects
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")

set(CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)

# Find Python, NumPy and OpenMP
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(Python3 REQUIRED NumPy)
find_package(OpenMP REQUIRED)

# Include directories for Pybind11 and NumPy
find_package(pybind11 REQUIRED)

include_directories(${Python3_INCLUDE_DIRS} ${Python3_NumPy_INCLUDE_DIRS})

# Define the target module
pybind11_add_module(getObjects main.cpp)

# Link Python libraries (if needed)
target_link_libraries(getObjects PRIVATE Python3::Python Python3::NumPy)
target_link_libraries(getObjects PRIVATE OpenMP::OpenMP_CXX)
