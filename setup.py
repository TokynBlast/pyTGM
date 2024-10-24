from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Game Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10 :: Linux' :: Windows 11,
  'License :: Bspace License',
  'Programming Language :: Python :: >=3.6'
]
 
setup(
  name='pytgm',
  version='2.1.3',
  description='Terminal Game Maker',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://pytgm.tokynblast.space/init',  
  author='Tokyn Blast',
  author_email='tokynblast@gmail.com',
  license='Bspace', 
  classifiers=classifiers,
  keywords='game,game maker,terminal,tools', 
  packages=find_packages(),
  install_requires=[''] 
)
