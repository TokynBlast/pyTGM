"""Builds the pyTGM package using nanobind"""

import os
import sys
import json
import platform
import subprocess
from pathlib import Path
from multiprocessing import cpu_count
from setuptools.command.build_ext import build_ext
from setuptools import setup, find_packages, Extension

with open("meta.json", encoding="utf-8") as f:
    meta = json.load(f)

# OS-specific install_requires
require = ['nanobind']
if platform.system() == "Darwin":
    require += ['setuptools>=66.1.1', 'wheel>=0.45.1']

class CMakeBuild(build_ext):
    """Build C++ extensions using CMake and nanobind"""
    def run(self):
        if not self.check_cmake():
            raise RuntimeError("CMake is required to build extensions")
        for ext in self.extensions:
            self.build_extension(ext)

    def check_cmake(self):
        try:
            subprocess.check_output(['cmake', '--version'])
            return True
        except OSError:
            return False

    def build_extension(self, ext):
        extdir = Path(self.get_ext_fullpath(ext.name)).parent.resolve()
        cfg = 'Debug' if self.debug else 'Release'
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={cfg}",
        ]

        if platform.system() == "Windows":
            cmake_args.append(f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}")
            if sys.maxsize > 2**32:
                cmake_args.extend(["-A", "x64"])
            build_args = ["--", "/m"]
        else:
            build_args = ["--", f"-j{cpu_count()}"]

        build_temp = Path(self.build_temp) / ext.name
        build_temp.mkdir(parents=True, exist_ok=True)

        subprocess.check_call(["cmake", Path(__file__).parent.resolve()] + cmake_args, cwd=build_temp)
        subprocess.check_call(["cmake", "--build", "."] + build_args, cwd=build_temp)

# Define modules and their source files
modules = [
    ("pyTGM.encrypt.b64", "pyTGM/encrypt/b64.cpp"),
    ("pyTGM.encrypt.hk512", "pyTGM/encrypt/hk512.cpp"),
    ("pyTGM.terminal.geky", "pyTGM/terminal/geky.cpp"),
    ("pyTGM.terminal.clear", "pyTGM/terminal/clear.cpp"),
    ("pyTGM.terminal.color", "pyTGM/terminal/color.cpp"),
    ("pyTGM.terminal.pos", "pyTGM/terminal/pos.cpp"),
    ("pyTGM.sound", "pyTGM/sound.cpp"),
    ("pyTGM.rect", "pyTGM/rect.cpp"),
]

extensions = [
    Extension(
        name=mod,
        sources=[src],
        include_dirs=[".", "pyTGM"],
        language="c++"
    )
    for mod, src in modules
]

setup(
    **meta,
    long_description=(
        open('README.md', encoding='utf-8').read() + '\n\n' +
        open('CHANGELOG.txt', encoding='utf-8').read() + '\n\n' +
        open('CHANGELOG_NOTES.txt', encoding='utf-8').read()
    ),
    packages=find_packages(),
    install_requires=require,
    ext_modules=extensions,
    cmdclass={"build_ext": CMakeBuild},
)
