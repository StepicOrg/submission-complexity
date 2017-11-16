#!/usr/bin/env python

from setuptools import find_packages, setup

with open('requirements.txt') as r:
    requirements = r.read().splitlines()

setup(
    name='submission-complexity',
    packages=find_packages(exclude=['test', '*.test', '*.test.*', 'grammars', 'scripts']),
    version='0.2',
    description='Tools for build complexity score for Stepik code submissions',
    author='Anastasia Lavrenko',
    author_email='lavrenko.a@gmail.com',
    url='https://github.com/StepicOrg/submission-complexity',
    install_requires=requirements,
)
