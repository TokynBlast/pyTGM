cmake_minimum_required(VERSION 3.14)
project(pyTGM)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python (generic package, required by nanobind)
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)

# Display Python include path
message(STATUS "Using Python include dir: ${Python_INCLUDE_DIRS}")
include_directories(${Python_INCLUDE_DIRS})

# Find nanobind using Python executable
execute_process(
  COMMAND ${Python_EXECUTABLE} -m nanobind --cmake_dir
  OUTPUT_VARIABLE NANOBIND_PATH
  OUTPUT_STRIP_TRAILING_WHITESPACE)

if(NOT EXISTS ${NANOBIND_PATH})
  message(FATAL_ERROR "nanobind not found at ${NANOBIND_PATH}. Please install with: pip install nanobind")
endif()

# Add nanobind to CMake prefix path
list(APPEND CMAKE_PREFIX_PATH ${NANOBIND_PATH})
find_package(nanobind CONFIG REQUIRED)

# Include nanobind (optional if using nanobind_add_module)
include_directories(${nanobind_INCLUDE_DIRS})

# Set source root
set(SRC_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/pyTGM)

# Define all modules
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

# Build each nanobind module
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

# Install the modules
include(GNUInstallDirs)
install(TARGETS
  hk512 b64 rect clear color geky pos sound
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/pyTGM
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}/pyTGM
)
