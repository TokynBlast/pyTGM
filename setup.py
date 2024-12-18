"""
Setup script for the pyTGM package.
Handles package configuration and extension building.
"""

import platform
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

if platform.startswith("win"):
    extra_compile_args = ["/std:c++latest", "/EHsc", "/bigobj"]
    extra_link_args = ["User32.lib"]
    sources = ["pytgm/terd/click.cpp"]
elif platform.startswith("linux"):
    extra_compile_args = ["-std=c++11", "-O3", "-Wall", "-fPIC"]
    extra_link_args = []
    sources = ["pytgm/terd/click.cpp"]
elif platform.startswith("darwin"):
    extra_compile_args = ["-std=c++11", "-O3", "-Wall", "-fPIC"]
    extra_link_args = []
    sources = ["pytgm/terd/click.cpp"]
else:
    raise RuntimeError(f"Unsupported platform: {platform}")

MAIT_AUTH = 'Tokyn Blast'
MAIT_AUTH_CONT = 'tokynblast@gmail.com'

click_extension = Pybind11Extension(
    name="click",
    sources=sources,
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

setup(
    name='pyTGM',
    version='4.0.6',
    description='Terminal Game Maker',
    long_description=(open('README.md', encoding='utf-8').read() +
                      '\n\n' +
                      open('CHANGELOG.txt', encoding='utf-8').read()),
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.13',
    ],
    keywords='game, game maker, terminal, tools, pytgm, terminal input',
    packages=find_packages(),
    install_requires=[],
    ext_modules=[click_extension],
    cmdclass={"build_ext": build_ext},
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"],
)
