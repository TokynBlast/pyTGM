""" Builds the pyTGM package """

import os
import sys
import platform
import subprocess
from platform import system as sys_
from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext

if sys_() == "Darwin":
    require = ['cython>=3.0.12', 'setuptools>=66.1.1', 'wheel>=0.45.1']
else:
    require = []

def get_ext_source(module_name, pyx_path, cpp_path):
    if os.path.exists(cpp_path):
        print(f"Using pre-generated C++ file for {module_name}: {cpp_path}")
        return cpp_path
    print(f"Cythonizing {pyx_path} for {module_name}")
    return pyx_path

def normalize_path(*paths):
    return os.path.join(*paths)

def check_sources(sources):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    for source in sources:
        full_path = os.path.join(root_dir, source)
        print(f"Checking for source file: {full_path}")
        if not os.path.exists(full_path):
            raise RuntimeError(f"Source file not found: {full_path}")

def find_file(filename, search_path="."):
    search_path = os.path.abspath(search_path)
    current_dir = search_path
    last_dir = None
    while True:
        print(f"Searching for {filename} in {current_dir} (ignoring {last_dir})")
        for root, dirs, files_in_dir in os.walk(current_dir):
            if last_dir and os.path.abspath(root) == current_dir:
                dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) != last_dir]
            if filename in files_in_dir:
                found_path = os.path.join(root, filename)
                rel_path = os.path.relpath(found_path, os.getcwd())
                if 'pyTGM' in rel_path:
                    parts = rel_path.split(os.sep)
                    idx = parts.index('pyTGM')
                    rel_path = os.path.join('pyTGM', *parts[idx + 1:])
                print(f"Found: {rel_path}")
                return rel_path
        parent = os.path.dirname(current_dir)
        if parent == current_dir:
            break
        last_dir = current_dir
        current_dir = parent
    print(f"NONE for {filename}")
    return None

def get_relative_path(path):
    if path is None:
        return None
    base = os.getcwd()
    rel_path = os.path.relpath(os.path.abspath(path), base)
    if not rel_path.startswith("./"):
        rel_path = "./" + rel_path
    return rel_path

class BuildExt(build_ext):
    """Builds the extensions written in C++, to work with Python"""
    def run(self):
        try:
            subprocess.check_output(['cmake', '--version'])
        except OSError as exc:
            raise RuntimeError("CMake must be installed to build this package") from exc

        cython_found = False
        for cython_cmd in (['cython3', '--version'], ['cython', '--version']):
            try:
                subprocess.check_output(cython_cmd)
                cython_found = True
                break
            except (OSError, subprocess.CalledProcessError):
                continue
        if not cython_found:
            raise RuntimeError("Cython must be installed to build this package (neither 'cython3' nor 'cython' was found)")

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

extensions_files = {
    module: [f"{module}.pyx", f"{module}.cpp", f"{module}.hpp"] for module in [
        "b64", "hk512", "geky", "clear", "color", "pos"
    ]
}

found_files = {}
for module, file_list in extensions_files.items():  # Renamed from 'files'
    found_files[module] = [find_file(f) for f in file_list]
    if None in found_files[module]:
        print(f"Missing files for: {module}")

extend = []
for module, file_list in extensions_files.items():  # Renamed from 'files'
    found = [find_file(f) for f in file_list]
    source_file = None
    if found[1] is not None:
        source_file = get_relative_path(found[1])
    elif found[0] is not None:
        source_file = get_relative_path(found[0])
    else:
        print(f"Warning: Skipping {module} - no source file found")
        continue
    if found[2] is None:
        print(f"Warning: Header file for {module} not found.")

    extension = Extension(
        name=(
            f"pyTGM.encrypt.{module}" if module in ["b64", "hk512"]
            else f"pyTGM.terminal.{module}" if module in ["geky", "clear", "color", "pos"]
            else f"pyTGM.{module}"
        ),
        sources=[source_file],
        include_dirs=[
            os.getcwd(),
            os.path.join(os.getcwd(), 'pyTGM')
        ],
        language="c++"
    )
    extend.append(extension)

for extension in extend:
    print(f"\nChecking sources for extension: {extension.name}")
    check_sources(extension.sources)
    print(f"Include dirs: {extension.include_dirs}")

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
    print(f"Cythonize failed for files: {[ext.sources for ext in extend]}")
    print(f"Error: {str(e)}")
    raise

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
    python_requires=">=3.11",
    platforms=["Windows", "Linux", "MacOS"],
)
