from setuptools import setup, find_packages, Extensions
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

maintain_auth = 'Tokyn Blast'
maintain_auth_contact = 'tokynblast@gmail.com'

setup(
  name='pyTGM',
  version='4.0.0',
  description='Terminal Game Maker',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://youtube.tokynblast.space/programming/libraries/pytgm/init',  
  author=maintain_auth,
  author_email=maintain_auth_contact,
  maintainer=maintain_auth,
  maintainer_email=maintain_auth_contact,
  license='Bspace', 
  classifiers=classifiers,
  keywords='game,game maker,terminal,tools,pytgm,terimnal input', 
  packages=find_packages(),
  install_requires=[''],
  ext_modules=[ Extension(
            'click',
            sources=['terd/click.c'],
            extra_compile_args=extra_compile_args[sys.platform],
        )],
  python_requires=">=3.13",
  platforms=["Windows", "Linux", "MacOS"]
)
