cmake_minimum_required(VERSION 3.14)
project(pyTGM)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python3 and pybind11 packages
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

find_package(pybind11 REQUIRED)
if (NOT pybind11_FOUND)
    execute_process(
        COMMAND apt install python3-pybind11 --cmakedir
        OUTPUT_VARIABLE pybind11_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    set(pybind11_DIR ${pybind11_DIR} CACHE PATH "Path to pybind11 CMake files")
    find_package(pybind11 REQUIRED)
endif()


# Recursively find all C++ source files
file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS *.cpp *.cc *.cxx)

if(NOT SRC_FILES)
  message(FATAL_ERROR "No C++ source files found!")
endif()

# Add the pybind11 module
pybind11_add_module(pyTGM MODULE ${SRC_FILES})

# Link against Python and pybind11
target_link_libraries(pyTGM PRIVATE Python3::Python pybind11::module)
