cmake_minimum_required(VERSION 3.14)
project(pyTGM)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python3 and pybind11 packages
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

# Recursively find all C++ source files
file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS *.cpp *.cc *.cxx)

if(NOT SRC_FILES)
  message(FATAL_ERROR "No C++ source files found!")
endif()

# Create the Python module target using pybind11
pybind11_add_module(pyTGM MODULE ${SRC_FILES})

# Link against Python and pybind11 libraries (pybind11_add_module already does some linking)
target_link_libraries(pyTGM PRIVATE Python3::Python)
