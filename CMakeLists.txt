cmake_minimum_required(VERSION 3.15)
project(pyTGM_project LANGUAGES CXX)

# Always prefer Release unless user overrides
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

find_package(Python 3.11 REQUIRED COMPONENTS Interpreter Development.Module)

# Find nanobind
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
    OUTPUT_VARIABLE nanobind_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
find_package(nanobind CONFIG REQUIRED)

# Include Python headers
include_directories(${Python_INCLUDE_DIRS})

# Define where your C++ files are
set(SRC_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/pyTGM)

# List all modules (format: module_name : relative_path)
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

# Build each C++ file as its own nanobind module
foreach(MODULE ${MODULES})
  string(REPLACE ":" ";" PARTS ${MODULE})
  list(GET PARTS 0 MOD_NAME)
  list(GET PARTS 1 MOD_PATH)
  
  set(SRC_FILE ${SRC_ROOT}/${MOD_PATH})
  
  if(EXISTS ${SRC_FILE})
    message(STATUS "Building module: ${MOD_NAME} -> ${SRC_FILE}")
    nanobind_add_module(${MOD_NAME} ${SRC_FILE})
    
    # Ensure correct output path matching pyTGM/ structure
    if(MOD_PATH MATCHES "terminal/")
      set_target_properties(${MOD_NAME} PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/pyTGM/terminal"
      )
    elseif(MOD_PATH MATCHES "encrypt/")
      set_target_properties(${MOD_NAME} PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/pyTGM/encrypt"
      )
    else()
      set_target_properties(${MOD_NAME} PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/pyTGM"
      )
    endif()
  else()
    message(WARNING "Source file for module '${MOD_NAME}' not found: ${SRC_FILE}")
  endif()
endforeach()

# Install rules to allow "make install" later if needed
install(TARGETS hk512 b64 rect clear color geky pos sound
  LIBRARY DESTINATION pyTGM
)

