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

def normalize_path(*paths):
    """Normalize path relative to package root"""
    return os.path.join(*paths)

def check_sources(sources):
    """Check if source files exist"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    for source in sources:
        if not source.startswith(""):
            source = os.path.join("pyTGM", source)
        full_path = os.path.join(root_dir, source)
        print(f"Checking for source file: {full_path}")
        if not os.path.exists(full_path):
            raise RuntimeError(f"Source file not found: {full_path}")

def find_file(filename, search_path="."):
    """Search for a file in the given path and all subdirectories"""
    for root, _, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

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

        sourcedir = os.path.abspath(os.path.dirname(__file__))

        print(f"Building extension: {ext.name}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Source directory: {sourcedir}")
        print(f"Extension directory: {extdir}")

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

        try:
            subprocess.check_call(['cmake', sourcedir] + cmake_args, cwd=build_temp)
        except subprocess.CalledProcessError as e:
            print(f"Error running cmake: {e.output}")
            raise

        try:
            subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=build_temp)
        except subprocess.CalledProcessError as e:
            print(f"Error building with cmake: {e.output}")
            raise

# Cython extensions

geky_pyx = find_file("geky.pyx")
if geky_pyx:
    print(f"Found geky.pyx at: {geky_pyx}")
else:
    print("geky.pyx not found in project directory")

extend = [
    Extension(
        name="pyTGM.terminal.geky",
        sources=[
            "terminal/geky/geky.pyx",
            "terminal/geky/geky.cpp"
        ],
        include_dirs=[
            os.getcwd(),
            "terminal/geky",
        ],
        language="c++",
    ),

    Extension(
        name="pyTGM.sound",
        sources=[
            "sound/sound.cpp",
            "sound/sound.pyx"
        ],
        include_dirs=[
            os.getcwd(),
            "sound",
        ],
        language="c++",
    ),

    Extension(
        name="pyTGM.terminal.clear",
        sources=[
            "terminal/clear/clear.cpp",
            "terminal/clear/clear.pyx"
        ],
        include_dirs=[
            os.getcwd(),
            "terminal/clear",
        ],
        language="c++",
    ),

    Extension(
        name="pyTGM.terminal.color",
        sources=[
            "terminal/color/color.cpp",
            "terminal/color/color.pyx"
        ],
        include_dirs=[
            os.getcwd(),
            "terminal/color",
        ],
        language="c++",
    ),

    Extension(
        name="pyTGM.terminal.pos",
        sources=[
            "terminal/pos/pos.cpp",
            "terminal/pos/pos.pyx"
        ],
        include_dirs=[
            os.getcwd(),
            "terminal/pos",
        ],
        language="c++",
    ),

    Extension(
        name="pyTGM.rect",
        sources=[
            "rect/rect.cpp",
            "rect/rect.pyx"
        ],
        include_dirs=[
            os.getcwd(),
            "rect",
        ],
        language="c++",
    ),

    Extension(
        name="pyTGM.encrypt.hk512",
        sources=[
            "encrypt/hk512/hk512.cpp",
            "encrypt/hk512/hk512.pyx"
        ],
        include_dirs=[
            os.getcwd(),
            "encrypt/hk512",
        ],
        language="c++",
    ),

    Extension(
        name="pyTGM.encrypt.b64",
        sources=[
            "encrypt/b64/b64.cpp",
            "encrypt/b64/b64.pyx"
        ],
        include_dirs=[
            os.getcwd(),
            "encrypt/b64",
        ],
        language="c++",
    )
]

for extension in extend:
    check_sources(extension.sources)

if USE_CYTHON:
    try:
        extensions = cythonize(
            extend,
            language_level=3,
            annotate=False,
            compiler_directives={
                'language_level': '3',
                'embedsignature': True
            }
        )
    except Exception as e:
        print(f"Cythonize failed: {str(e)}")
        raise
else:
    extensions = extend

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
    keywords='game, game maker, terminal, tools, pyTGM, pytgm, terminal input, pygame alternative',
    packages=find_packages(),
    install_requires=require,
    ext_modules=extensions,
    cmdclass={"build_ext": BuildExt},
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"],
)
