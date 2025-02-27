""" Builds the pyTGM package """

import os
import sys
import platform
import subprocess
from Cython.Build import cythonize
from platform import system as sys_
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext

if sys_() == "Darwin":
    require = ['cython>=3.0.12', 'setuptools>=66.1.1', 'wheel>=0.45.1']
else:
    require = []


class BuildExt(build_ext):
    def run(self):
        try:
            subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build this package")
        try:
            subprocess.check_output(['cython3', '--version'])
        except OSError:
            raise RuntimeError("Cython must be installed to build this package")
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cfg = 'Debug' if self.debug else 'Release'
        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DPYTHON_EXECUTABLE={sys.executable}',
            f'-DCMAKE_BUILD_TYPE={cfg}'
        ]
        build_args = []
        if platform.system() == "Windows":
            cmake_args += [f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}']
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            build_args += ['--', '-j2']

        build_temp = self.build_temp
        if not os.path.exists(build_temp):
            os.makedirs(build_temp)

        # Run CMake
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=build_temp)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=build_temp)

# Cython extensions
geky = Extension(
        name="pyTGM.terminal.geky",
        sources=["pyTGM/terminal/geky/geky.pyx", "pyTGM/terminal/geky/geky.cpp"],
        include_dirs=[os.getcwd()],
    )

sound = Extension(
    name="pyTGM.sound",
    sources=["pyTGM/sound/sound.cpp","pyTGM/sound/sound.pyx"],
    include_dirs=[os.getcwd()],
)

clear = Extension(
    name="pyTGM.terminal.clear",
    sources=["pyTGM/terminal/clear/clear.cpp", "pyTGM/terminal/clear/clear.pyx"],
    include_dirs=[os.getcwd()],
)

color = Extension(
    name="pyTGM.terminal.color",
    sources=["pyTGM/terminal/color/color.cpp", "pyTGM/terminal/color/color.pyx"],
    include_dirs=[os.getcwd()],
)

pos = Extension(
    name="pyTGM.terminal.pos",
    sources=["pyTGM/terminal/pos/pos.cpp", "pyTGM/terminal/pos/pos.pyx"],
    include_dirs=[os.getcwd()],
)

rect = Extension(
    name="pyTGM.rect",
    sources=["pyTGM/rect/rect.cpp", "pyTGM/rect/rect.pyx"],
    include_dirs=[os.getcwd()],
)

hk512 = Extension(
    name="pyTGM.encrypt.hk512",
    sources=["pyTGM/encrypt/hk512/hk512.cpp", "pyTGM/encrypt/hk512/hk512.pyx"],
    include_dirs=[os.getcwd()],
)

b64 = Extension(
    name="pyTGM.encrypt.hk512",
    sources=["pyTGM/encrypt/b64/b64.cpp", "pyTGM/encrypt/b64/b64.pyx"],
    include_dirs=[os.getcwd()],
)

setup(
    name='pyTGM',
    version='5.0.0',
    description='A game development library, for the terminal!',
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
    keywords='game, game maker, terminal, tools, pyTGM, pytgm, terminal input',
    packages=find_packages(),
    install_requires=require,
    ext_modules=cythonize(sound, clear, color, pos, geky, rect, hk512, b64),
    cmdclass={"build_ext": BuildExt},
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"],
)
