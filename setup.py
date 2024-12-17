"""
Setup script for the pyTGM package.
Handles package configuration and extension building.
"""

from sys import platform
from setuptools import setup, find_packages, Extension

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

extra_compile_args = {
    'linux': ['-std=c++11', '-O3', '-Wall', '-fPIC'],
    'darwin': ['-std=c++11', '-O3', '-Wall', '-fPIC'],
    'win32': ['/std:c++11', '/O2', '/W4']
}

MAIT_AUTH = 'Tokyn Blast'
MAIT_AUTH_CONT = 'tokynblast@gmail.com'

setup(
    name='pyTGM',
    version='4.0.0',
    description='Terminal Game Maker',
    long_description = (open('README.md', encoding='utf-8').read() + '\n\n' + \ # pylint: disable=consider-using-with
                        open('CHANGELOG.txt', encoding='utf-8').read()) # pylint: disable=consider-using-with
    long_description_content_type='text/markdown'

    url='https://youtube.tokynblast.space/programming/libraries/pytgm/init',
    author=MAIT_AUTH,
    author_email=MAIT_AUTH_CONT,
    maintainer=MAIT_AUTH,
    maintainer_email=MAIT_AUTH_CONT,
    license='Bspace',
    classifiers=classifiers,
    keywords='game,game maker,terminal,tools,pytgm,terimnal input',
    packages=find_packages(),
    install_requires=[''],
    ext_modules=[Extension(
        'click',
        sources=['pytgm/terd/click.cpp'],
        extra_compile_args=extra_compile_args[platform],
    )],
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"]
)
