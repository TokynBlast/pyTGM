from setuptools import setup, find_packages, Extensions
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Game Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10 :: Linux',
  'License :: Bspace License',
  'Programming Language :: Python :: >=3.13'
]
 
setup(
  name='pyTGM',
  version='4.0.0',
  description='Terminal Game Maker',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://youtube.tokynblast.space/programming/libraries/pytgm/init',  
  author='Tokyn Blast',
  author_email='tokynblast@gmail.com',
  maintainer='Tokyn Blast'
  maintainer_email='tokynblast@gmail.com'
  license='Bspace', 
  classifiers=classifiers,
  keywords='game,game maker,terminal,tools', 
  packages=find_packages(),
  install_requires=[''] 
  ext_modules=[Extension("click",["click.c"])]
  puthon_requires=">=3.13"
  platforms=["Windows", "Linux", "MacOS"]
)