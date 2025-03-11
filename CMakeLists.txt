cmake_minimum_required(VERSION 3.14)
project(pyTGM)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

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

foreach(entry ${MODULES})
    string(REGEX MATCH "([^:]+):(.*)" _ ${entry})
    set(mod_name ${CMAKE_MATCH_1})
    set(mod_dir ${CMAKE_MATCH_2})

    set(module_cpp "${CMAKE_CURRENT_SOURCE_DIR}/${mod_dir}/${mod_name}.cpp")
    add_library(${mod_name} SHARED ${module_cpp})

    target_include_directories(${mod_name} PRIVATE ${Python3_INCLUDE_DIRS})
    target_link_libraries(${mod_name} PRIVATE ${Python3_LIBRARIES})

    set_target_properties(${mod_name} PROPERTIES
        PREFIX ""
        SUFFIX ".so"
    )
endforeach()

message(STATUS "Cython Extensions Generated for these modules:")
foreach(entry ${MODULES})
    string(REGEX MATCH "([^:]+):" _ ${entry})
    message(STATUS "  ${CMAKE_MATCH_1}")
endforeach()
