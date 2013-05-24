# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_description = open('README.rst').read()

setup(
    name='expects',
    version='0.1',
    description='Expectations library for Python',
    long_description=long_description,
    author='Jaime Gil de Sagredo Luna',
    author_email='jaimegildesagredo@gmail.com',
    packages=find_packages(exclude=['spec', 'spec.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
