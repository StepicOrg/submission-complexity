#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

# with open('requirements.txt') as r:
#     requirements = r.read().splitlines()

setup(
    name='Submission Complexity',
    version='0.1',
    description='Tools for build complexity score for Stepik code submissions',
    author='Anastasia Lavrenko',
    author_email='lavrenko.a@gmail.com',
    url='https://stepik.org/',
    packages=[find_packages(exclude=['test', '*.test', '*.test.*'])],
    install_requires=['javalang', 'radon']
    # install_requires=requirements
)
