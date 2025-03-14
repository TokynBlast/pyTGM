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

execute_process(
    COMMAND pwd
    COMMAND echo "/n/n/n"
    COMMAND ls
    COMMAND echo "/n/n/n"
    COMMAND cd ..
    COMMAND echo "/n/n/n"
    COMMAND ls
    OUTPUT_VARIABLE PWD_VAR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

message(STATUS "/n/n/nCurrent working directory: ${PWD_VAR}/n/n/n")

foreach(entry ${MODULES})
    string(REPLACE ":" ";" entry_list ${entry})
    list(GET entry_list 0 mod_name)
    list(GET entry_list 1 mod_dir)

    set(module_cpp "../${mod_dir}/${mod_name}.cpp")

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
