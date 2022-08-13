from setuptools import setup, find_packages
 
VERSION = '0.1.7'
DESCRIPTION = 'A Python wrapper for Multiversus API'

classifiers = [
  'Development Status :: 3 - Alpha ',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='mulpyversus',
  version='0.1.7',
  description='A Python wrapper for Multiversus API',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/AshladBP/MulpyVersus',  
  author='Ashlad',
  author_email='imadbenbp@gmail.ocm',
  license='MIT', 
  classifiers=classifiers,
  keywords='mulpyversus multiversus api python',
  packages=find_packages(),
  install_requires=[''] 
)