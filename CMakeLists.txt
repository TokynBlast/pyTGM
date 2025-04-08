cmake_minimum_required(VERSION 3.14)
project(pyTGM)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

if (CMAKE_VERSION VERSION_LESS 3.18)
  set(DEV_MODULE Development)
else()
  set(DEV_MODULE Development.Module)
endif()

find_package(Python 3.8 COMPONENTS Interpreter ${DEV_MODULE} REQUIRED)

set(MODULES
    "hk512:encrypt/hk512"
    "b64:encrypt/b64"
    "rect:rect"
    "clear:terminal/clear"
    "color:terminal/color"
    "geky:terminal/geky"
    "pos:terminal/pos"
    "sound:sound"
)

execute_process(
  COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)


foreach(entry ${MODULES})
    string(REPLACE ":" ";" entry_list ${entry})
    list(GET entry_list 0 mod_name)
    list(GET entry_list 1 mod_dir)

    set(module_cpp "./../${mod_dir}/${mod_name}.cpp")

    if(EXISTS "${module_cpp}")
        add_library(${mod_name} SHARED "${module_cpp}")

        target_include_directories(${mod_name} PRIVATE ${Python3_INCLUDE_DIRS})
        target_link_libraries(${mod_name} PRIVATE ${Python3_LIBRARIES})

        set_target_properties(${mod_name} PROPERTIES
            PREFIX ""
            SUFFIX ".so"
        )
    else()
        message(WARNING "Source file for module '${mod_name}' not found: ${module_cpp}")
    endif()
endforeach()

message(STATUS "C++ modules being built:")
foreach(entry ${MODULES})
    string(REPLACE ":" ";" entry_list ${entry})
    list(GET entry_list 0 mod_name)
    message(STATUS "  ${mod_name}")
endforeach()
