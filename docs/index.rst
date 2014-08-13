Expects
=======

.. image:: http://img.shields.io/pypi/v/expects.svg
    :target: https://pypi.python.org/pypi/expects
    :alt: Latest version

.. image:: http://img.shields.io/pypi/dm/expects.svg
    :target: https://pypi.python.org/pypi/expects
    :alt: Number of PyPI downloads

.. image:: https://secure.travis-ci.org/jaimegildesagredo/expects.svg?branch=master
    :target: http://travis-ci.org/jaimegildesagredo/expects
    :alt: Build status

**Expects** is an *expressive* and *extensible* TDD/BDD assertion library for Python.

Usage
-----

Just import the ``expect`` callable and the `built-in matchers <matchers.html>`_ and start writing test assertions.

.. code-block:: python

    from expects import *

    expect([]).to(be_empty)

    expect(False).not_to(be_true)

    expect({
        'name': 'Jack',
        'email': 'jack@example.com'
    }).to(have_key('name', match('\w+')))

    expect(str).to(have_property('split'))

    expect(lambda: foo).to(raise_error(NameError))

Installation
------------

You can install the last stable release of Expects from PyPI using pip or easy_install.

.. code-block:: bash

    $ pip install expects

For more installation methods visit the `installation guide <install.html>`_.

Contents
--------

.. toctree::
   :maxdepth: 2

   install
   matchers
   custom-matchers
   testing
   changes



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

