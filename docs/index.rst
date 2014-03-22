Expects
=======

.. image:: https://secure.travis-ci.org/jaimegildesagredo/expects.png?branch=master
    :target: http://travis-ci.org/jaimegildesagredo/expects

**Expects** is an *expressive* and *extensible* TDD/BDD assertion library for Python.

Usage
-----

Just import the ``expect`` callable and start writing test assertions.

.. code-block:: python

    from expects import expect

    expect([]).to.be.empty

    expect(False).not_to.be.true

    expect({'name': 'Jack', 'email': 'jack@example.com'}).to.have.key('name') \
                                                         .with_value.match('\w+')

    expect(str).to.have.property('split')

    expect(lambda: foo).to.raise_error(NameError)

You can see all the *builtin* assertions with lots of examples `here <reference.html>`_.

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
   reference
   plugins
   changes



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

