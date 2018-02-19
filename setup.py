import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

setup(name='arsa-api',
      version='1.0',
      description='Arsa API',
      author='Corey Collins',
      author_email='coreyecollins@gmail.com',
      packages=find_packages(exclude=['tests', 'tests.*']),
      tests_require=['pytest'],
      install_requires=[
          'boto3'
          ]
)
