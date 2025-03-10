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

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

def get_ext_source(module_name, pyx_path, cpp_path):
    if os.path.exists(cpp_path):
        print(f"Using pre-generated C++ file for {module_name}: {cpp_path}")
        return cpp_path
    elif USE_CYTHON:
        print(f"Cythonizing {pyx_path} for {module_name}")
        return pyx_path
    else:
        raise RuntimeError(f"Cython is required to compile module {module_name}.")

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

extend = [
    Extension(
            name="pyTGM.terminal.geky",
            sources=["pyTGM/terminal/geky/geky.pyx", "pyTGM/terminal/geky/geky.cpp"],
            include_dirs=[os.getcwd()],
        ),

    Extension(
        name="pyTGM.sound",
        sources=["pyTGM/sound/sound.cpp","pyTGM/sound/sound.pyx"],
        include_dirs=[os.getcwd()],
    ),

    Extension(
        name="pyTGM.terminal.clear",
        sources=["pyTGM/terminal/clear/clear.cpp", "pyTGM/terminal/clear/clear.pyx"],
        include_dirs=[os.getcwd()],
    ),

    Extension(
        name="pyTGM.terminal.color",
        sources=["pyTGM/terminal/color/color.cpp", "pyTGM/terminal/color/color.pyx"],
        include_dirs=[os.getcwd()],
    ),

    Extension(
        name="pyTGM.terminal.pos",
        sources=["pyTGM/terminal/pos/pos.cpp", "pyTGM/terminal/pos/pos.pyx"],
        include_dirs=[os.getcwd()],
    ),

    Extension(
        name="pyTGM.rect",
        sources=["pyTGM/rect/rect.cpp", "pyTGM/rect/rect.pyx"],
        include_dirs=[os.getcwd()],
    ),

    Extension(
        name="pyTGM.encrypt.hk512",
        sources=["pyTGM/encrypt/hk512/hk512.cpp", "pyTGM/encrypt/hk512/hk512.pyx"],
        include_dirs=[os.getcwd()],
    ),

    Extension(
        name="pyTGM.encrypt.hk512",
        sources=["pyTGM/encrypt/b64/b64.cpp", "pyTGM/encrypt/b64/b64.pyx"],
        include_dirs=[os.getcwd()],
    )
]

if USE_CYTHON:
    extensions = cythonize(extend, language_level=3, annotate=False)

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
    ext_modules=extend,
    cmdclass={"build_ext": BuildExt},
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"],
)
