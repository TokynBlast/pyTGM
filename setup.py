""" Builds the pyTGM package using nanobind """

import os
import sys
import subprocess
import platform
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext

# Required for macOS compatibility
if platform.system() == "Darwin":
    require = ['nanobind', 'setuptools>=66.1.1', 'wheel>=0.45.1']
else:
    require = ['nanobind']

class CMakeBuild(build_ext):
    """Build extensions via CMake and nanobind."""
    def run(self):
        try:
            subprocess.check_output(['cmake', '--version'])
        except OSError as exc:
            raise RuntimeError("CMake must be installed to build this package") from exc

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cfg = 'Debug' if self.debug else 'Release'
        sourcedir = os.path.abspath(os.path.dirname(__file__))

        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={cfg}",
        ]
        build_args = []

        if platform.system() == "Windows":
            cmake_args += [f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}"]
            if sys.maxsize > 2**32:
                cmake_args += ["-A", "x64"]
            build_args += ["--", "/m"]
        else:
            build_args += ["--", "-j2"]

        build_temp = os.path.join(self.build_temp, ext.name)
        os.makedirs(build_temp, exist_ok=True)

        subprocess.check_call(["cmake", sourcedir] + cmake_args, cwd=build_temp)
        subprocess.check_call(["cmake", "--build", "."] + build_args, cwd=build_temp)

# Extension list: one dummy Extension for each C++ module
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
        name=mod_name,
        sources=[source],
        include_dirs=[
            os.getcwd(),
            os.path.join(os.getcwd(), "pyTGM")
        ],
        language="c++"
    )
    for mod_name, source in modules
]

setup(
    name='pyTGM',
    version='5.0.0',
    description='A terminal-based game development library!',
    long_description=(
        open('README.md', encoding='utf-8').read() + '\n\n' +
        open('CHANGELOG.txt', encoding='utf-8').read() + '\n\n' +
        open('CHANGELOG_NOTES.txt', encoding='utf-8').read()
    ),
    long_description_content_type='text/markdown',
    url='https://github.com/TokynBlast/pyTGM',
    author='Tokyn Blast',
    author_email='tokynblast@gmail.com',
    license='Bspace',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: C++ :: 17',
    ],
    keywords='game, game maker, terminal, tools, pyTGM, pytgm, terminal input, pygame alternative, pygame, terminal, ascii, ansi',
    packages=find_packages(),
    install_requires=require,
    ext_modules=extensions,
    cmdclass={"build_ext": CMakeBuild},
    python_requires=">=3.11",
    platforms=["Windows", "Linux", "MacOS"],
)
