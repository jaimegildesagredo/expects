# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_description = open('README.rst').read()

setup(
    name='expects',
    version='0.3.0',
    description='Expressive and extensible TDD/BDD assertion library for Python',
    long_description=long_description,
    url='https://github.com/jaimegildesagredo/expects',
    author='Jaime Gil de Sagredo Luna',
    author_email='jaimegildesagredo@gmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=['spec', 'spec.*']),
    entry_points={
        'expects.matchers': [
            'equal = expects.matchers.equal:Equal',
            'be = expects.matchers.be:Be',
            'be_true = expects.matchers.be_true:BeTrue',
            'be_false = expects.matchers.be_false:BeFalse',
            'be_none = expects.matchers.be_none:BeNone',
            'be_a = expects.matchers.be_a:BeAnInstanceOf',
            'be_an = expects.matchers.be_a:BeAnInstanceOf',
            'be_empty = expects.matchers.be_empty:BeEmpty',
            'be_above = expects.matchers.be_above:BeAbove',
            'be_below = expects.matchers.be_below:BeBelow',
            'be_above_or_equal = expects.matchers.be_above_or_equal:BeAboveOrEqual',
            'be_below_or_equal = expects.matchers.be_below_or_equal:BeBelowOrEqual',
            'be_within = expects.matchers.be_within:BeWithIn',
            'have_length = expects.matchers.have_length:HaveLength',
            'have_property = expects.matchers.have_property:HaveProperty',
            'have_properties = expects.matchers.have_properties:HaveProperties',
            'have_key = expects.matchers.have_key:HaveKey',
            'have_keys = expects.matchers.have_keys:HaveKeys',
            'contain = expects.matchers.contain:Contain',
            'contain_only = expects.matchers.contain_only:ContainOnly',
            'start_with = expects.matchers.start_with:StartWith',
            'end_with = expects.matchers.end_with:EndWith',
            'match = expects.matchers.match:Match',
            'raise_error = expects.matchers.raise_error:RaiseError'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License'
    ]
)
