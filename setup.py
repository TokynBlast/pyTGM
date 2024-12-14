"""
Setup script for the pyTGM package.
Handles package configuration and extension building.
"""

from setuptools import setup, find_packages, Extension
from sys import platform

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Game Developers',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS',
    'License :: Bspace License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.13',
]

extra_compile_args = {
    'linux': ['-std=c++11', '-O3', '-Wall', '-fPIC'],
    'darwin': ['-std=c++11', '-O3', '-Wall', '-fPIC'],
    'win32': ['/std:c++11', '/O2', '/W4']
}

MAINTAIN_AUTH = 'Tokyn Blast'
MAINTAIN_AUTH_CONTACT = 'tokynblast@gmail.com'

setup(
    name='pyTGM',
    version='4.0.0',
    description='Terminal Game Maker',
    long_description=open('README.txt', encoding='utf-8').read() + '\n\n' + open('CHANGELOG.txt', encoding='utf-8').read(),
    url='https://youtube.tokynblast.space/programming/libraries/pytgm/init',
    author=MAINTAIN_AUTH,
    author_email=MAINTAIN_AUTH_CONTACT,
    maintainer=MAINTAIN_AUTH,
    maintainer_email=MAINTAIN_AUTH_CONTACT,
    license='Bspace',
    classifiers=classifiers,
    keywords='game,game maker,terminal,tools,pytgm,terimnal input',
    packages=find_packages(),
    install_requires=[''],
    ext_modules=[Extension(
        'click',
        sources=['terd/click.c'],
        extra_compile_args=extra_compile_args[platform],
    )],
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"]
)
