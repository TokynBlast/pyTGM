"""Tells Python how to build the pytgm package"""

import os
import subprocess
from platform import system as sys
import shutil
from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext

class BuildExt(build_ext):
    """
    Determines the OS and sets up the Ninja build system.
    """
    def build_extensions(self):
        os_type = sys()
        if os_type == "Windows":
            for ext in self.extensions:
                ext.extra_compile_args = ["/std:c++17", "/EHsc", "/bigobj"]
                ext.extra_link_args = ["User32.lib"]
        elif os_type in ["Linux", "Darwin"]:  # MacOS is "Darwin"
            for ext in self.extensions:
                ext.extra_compile_args = ["-std=c++17", "-O3", "-Wall", "-fPIC"]
                ext.extra_link_args = []

        # Use Ninja if available
        if shutil.which("ninja"):
            print("Using Ninja build system")
            os.environ["CMAKE_GENERATOR"] = "Ninja"
        else:
            print("Ninja not found, falling back to default build system.")

        super().build_extensions()

# Define extensions
sound = Pybind11Extension(
    name="pytgm.sound",
    sources=["pytgm/sound.cpp"],
    language="c++",
)

cls = Pybind11Extension(
    name="pytgm.terminal.cls",
    sources=["pytgm/terminal/cls.cpp"],
    language="c++",
)

color = Pybind11Extension(
    name="pytgm.terminal.color",
    sources=["pytgm/terminal/color.cpp"],
    language="c++",
)

pos = Pybind11Extension(
    name="pytgm.terminal.pos",
    sources=["pytgm/terminal/pos.cpp"],
    language="c++",
)

geky = Pybind11Extension(
    name="pytgm.terminal.geky",
    sources=["pytgm/terminal/geky.cpp"],
    language="c++",
)

rect = Pybind11Extension(
    name="pytgm.rect",
    sources=["pytgm/pattern/rect.cpp"],
    language="c++",
)

hk512 = Pybind11Extension(
    name="pytgm.encrypt.hk512",
    sources=["pytgm/encrypt/hk512.cpp"],
    language="c++",
)

setup(
    name='pyTGM',
    version='5.0.0',
    description='Game maker contained in the terminal using C++ and Python',
    long_description=(open('README.md', encoding='utf-8').read().close() + '\n\n' + # pylint: disable=consider-using-with
                      open('CHANGELOG.txt', encoding='utf-8').read().close() + '\n\n' + #pylint: disable=consider-using-with line-too-long
                      open('CHANGELOG_NOTES.txt', encoding='utf-8').read().close()), #pylint: disable=consider-using-with line-too-long
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
    keywords='game, game maker, terminal, tools, pytgm, terminal input',
    packages=find_packages(),
    install_requires=['pybind11==2.13.6', 'setuptools==75.8.0', 'wheel==0.45.1'],
    ext_modules=[sound, cls, color, pos, geky, rect, hk512],
    cmdclass={"build_ext": BuildExt},
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"],
)
