"""
Setup script for the pyTGM package.
Handles package configuration and extension building.
"""

from platform import system as sys
from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS',
    'License :: Other/Proprietary License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.13',
]

class BuildExt(build_ext):
    """
    Determines the OS
    """
    def build_extensions(self):
        os_type = sys()
        if os_type == "Windows":
            for ext in self.extensions:
                ext.extra_compile_args = ["/std:c++latest", "/EHsc", "/bigobj"]
                ext.extra_link_args = ["User32.lib"]
        elif os_type == "Linux":
            for ext in self.extensions:
                ext.extra_compile_args = ["-std=c++11", "-O3", "-Wall", "-fPIC"]
                ext.extra_link_args = []
        elif os_type == "Darwin":
            for ext in self.extensions:
                ext.extra_compile_args = ["-std=c++11", "-O3", "-Wall", "-fPIC"]
                ext.extra_link_args = []
        else:
            raise RuntimeError(f"Unsupported platform: {os_type}")
        super().build_extensions()

MAIT_AUTH = 'Tokyn Blast'
MAIT_AUTH_CONT = 'tokynblast@gmail.com'

click_extension = Pybind11Extension(
    name="pytgm.terd.click",
    sources=["pytgm/terd/click.cpp"],
    language="c++",
)

setup(
    name='pyTGM',
    version='4.1.1',
    description='Terminal Game Maker',
    long_description=(open('README.md', encoding='utf-8').read() + '\n\n' + # pylint: disable=consider-using-with
                      open('CHANGELOG.txt', encoding='utf-8').read() + '\n\n' +  # pylint: disable=consider-using-with
                      open('CHANGELOG_NOTES.txt', encoding='utf-8').read()), # pylint: disable=consider-using-with
    long_description_content_type='text/markdown',
    url='https://github.com/TokynBlast/pyTGM',
    author='Tokyn Blast',
    author_email='tokynblast@gmail.com',
    license='Bspace',
    classifiers=classifiers,
    keywords='game, game maker, terminal, tools, pytgm, terminal input',
    packages=find_packages(),
    install_requires=[],
    ext_modules=[click_extension],
    cmdclass={"build_ext": BuildExt},
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"],
)
