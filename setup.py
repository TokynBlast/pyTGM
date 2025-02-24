"""Tells Python how to build the pyTGM package"""

from platform import system as sys
from setuptools import setup#, find_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext

require = []

req_os = sys()
if req_os == "Darwin":
    require = ['pybind11==2.13.6', 'setuptools==75.8.0', 'wheel==0.45.1']
else:
    require = []

del req_os

class BuildExt(build_ext):
    """
    Determines the OS and sets the build params
    """

    def build_extensions(self):
        os_type = sys()
        if os_type == "Windows":
            for ext in self.extensions:
                ext.extra_compile_args = ["/std:c++17", "/EHsc", "/bigobj"]
                ext.extra_link_args = ["User32.lib"]
        elif os_type in ["Linux", "Darwin"]:
            for ext in self.extensions:
                ext.extra_compile_args = ["-std=c++17", "-O3", "-Wall", "-fPIC"]
                ext.extra_link_args = []
        super().build_extensions()
        del os_type

# Define extensions
sound = Pybind11Extension(
    name="pyTGM.sound",
    sources=["pyTGM/sound.cpp"],
    language="c++",
)

clear = Pybind11Extension(
    name="pyTGM.terminal.clear",
    sources=["pyTGM/terminal/clear.cpp"],
    language="c++",
)

color = Pybind11Extension(
    name="pyTGM.terminal.color",
    sources=["pyTGM/terminal/color.cpp"],
    language="c++",
)

pos = Pybind11Extension(
    name="pyTGM.terminal.pos",
    sources=["pyTGM/terminal/pos.cpp"],
    language="c++",
)

geky = Pybind11Extension(
    name="pyTGM.terminal.geky",
    sources=["pyTGM/terminal/geky.cpp"],
    language="c++",
)

rect = Pybind11Extension(
    name="pyTGM.rect",
    sources=["pyTGM/pattern/rect.cpp"],
    language="c++",
)

hk512 = Pybind11Extension(
    name="pyTGM.encrypt.hk512",
    sources=["pyTGM/encrypt/hk512.cpp"],
    language="c++",
)

setup(
    name='pyTGM',
    version='5.0.0',
    description='Game maker contained in the terminal using C++ and Python',
    long_description=(open('README.md', encoding='utf-8').read() + '\n\n' + # pylint: disable=consider-using-with
                      open('CHANGELOG.txt', encoding='utf-8').read() + '\n\n' + #pylint: disable=consider-using-with line-too-long
                      open('CHANGELOG_NOTES.txt', encoding='utf-8').read()), #pylint: disable=consider-using-with line-too-long
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
        'Programming Language :: C++ :: 11',
    ],
    keywords='game, game maker, terminal, tools, pytgm, terminal input',
    packages=['pyTGM',
              'pyTGM.encrypt',
              'pyTGM.pattern',
              'pyTGM.terminal'],
    install_requires=require,
    ext_modules=[sound, clear, color, pos, geky, rect, hk512],
    cmdclass={"build_ext": BuildExt},
    python_requires=">=3.13",
    platforms=["Windows", "Linux", "MacOS"],
    include_package_data=True,
    data_files=[('', ['setup.py'])],
)
