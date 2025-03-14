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
    last_dir = None  # The directory we just fully searched
    while True:
        print(f"Searching for {filename} in {current_dir} (ignoring {last_dir})")
        # Walk the current directory
        for root, dirs, files in os.walk(current_dir):
            # At the top level of current_dir, remove the directory we already searched.
            if last_dir and os.path.abspath(root) == current_dir:
                dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) != last_dir]
            if filename in files:
                found_path = os.path.join(root, filename)
                # Get a relative path (adjust if you want it to start with 'pyTGM')
                rel_path = os.path.relpath(found_path, os.getcwd())
                if 'pyTGM' in rel_path:
                    parts = rel_path.split(os.sep)
                    idx = parts.index('pyTGM')
                    rel_path = os.path.join('pyTGM', *parts[idx+1:])
                print(f"Found: {rel_path}")
                return rel_path
        # File was not found in current_dir; move up one level
        parent = os.path.dirname(current_dir)
        if parent == current_dir:  # We have reached the filesystem root
            break
        # Remember the directory we just searched so we skip it in the parent's search.
        last_dir = current_dir
        current_dir = parent
    print(f"NONE for {filename}")
    return None


def get_relative_path(path):
    if path is None:
        return None
    abs_path = os.path.abspath(path)
    return os.path.relpath('.', abs_path, os.getcwd())




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

extensions_files = [
    "geky", "sound", "clear", "color", "pos", "rect", "hk512", "b64"
]

extensions_files = {
    module: [f"{module}.pyx", f"{module}.cpp", f"{module}.hpp"] for module in extensions_files
}

found_files = {}
for module, files in extensions_files.items():
    found_files[module] = [find_file(f) for f in files]
    if None in found_files[module]:
        print(f"Missing files for: {module}")

extend = []
for module, files in extensions_files.items():
    found_files_filtered = [f for f in found_files[module] if f is not None]
    source_files = [get_relative_path(f) for f in found_files_filtered]

    if not source_files or not all(os.path.exists(f) for f in source_files):
        print(f"Warning: Skipping {module} - some source files missing:\n   {source_files}\n\n\n")
        continue
    include_path = os.path.dirname(source_files[0])

    extension = Extension(
        name=f"pyTGM.encrypt.{module}" if module in ["b64", "hk512"]
             else f"pyTGM.terminal.{module}" if module in ["geky", "clear", "color", "pos"]
             else f"pyTGM.{module}",
        sources=source_files,
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
        print(f"Cythonize failed for files: {[ext.sources for ext in extend]}")
        print(f"Error: {str(e)}")
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
