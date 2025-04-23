cmake_minimum_required(VERSION 3.14)
project(pyTGM)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python
find_package(Python3 3.11 REQUIRED COMPONENTS Interpreter Development)

# Get Python include dirs
message(STATUS "Using Python include dir: ${Python3_INCLUDE_DIRS}")
include_directories(${Python3_INCLUDE_DIRS})

# Find nanobind
execute_process(
  COMMAND ${Python3_EXECUTABLE} -m nanobind --cmake_dir
  OUTPUT_VARIABLE NANOBIND_PATH
  OUTPUT_STRIP_TRAILING_WHITESPACE)

if(NOT EXISTS ${NANOBIND_PATH})
  message(FATAL_ERROR "nanobind not found. Please install with: pip install nanobind")
endif()

list(APPEND CMAKE_PREFIX_PATH ${NANOBIND_PATH})
find_package(nanobind CONFIG REQUIRED)

# Include nanobind
include_directories(${nanobind_INCLUDE_DIRS})

# Build directory setup
set(SRC_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/pyTGM)
file(GLOB_RECURSE ALL_CPP_FILES
  ${SRC_ROOT}/*.cpp
)

set(MODULES
  "hk512:encrypt/hk512.cpp"
  "b64:encrypt/b64.cpp"
  "rect:rect.cpp"
  "clear:terminal/clear.cpp"
  "color:terminal/color.cpp"
  "geky:terminal/geky.cpp"
  "pos:terminal/pos.cpp"
  "sound:sound.cpp"
)

# Add each module
foreach(MODULE ${MODULES})
  string(REPLACE ":" ";" PARTS ${MODULE})
  list(GET PARTS 0 MOD_NAME)
  list(GET PARTS 1 MOD_PATH)
  set(SRC_FILE ${SRC_ROOT}/${MOD_PATH})

  if(EXISTS ${SRC_FILE})
    message(STATUS "Building module: ${MOD_NAME} -> ${SRC_FILE}")
    nanobind_add_module(${MOD_NAME} ${SRC_FILE})
    target_include_directories(${MOD_NAME} PRIVATE ${SRC_ROOT})
  else()
    message(WARNING "Source file for module '${MOD_NAME}' not found: ${SRC_FILE}")
  endif()
endforeach()

# Optional install rule
include(GNUInstallDirs)
install(TARGETS
  hk512 b64 rect clear color geky pos sound
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/pyTGM
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}/pyTGM
)
