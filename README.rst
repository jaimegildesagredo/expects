Expects
=======

.. image:: https://img.shields.io/pypi/v/expects.svg
    :target: https://pypi.python.org/pypi/expects
    :alt: Latest version

.. image:: https://img.shields.io/badge/Docs-latest-brightgreen.svg
    :target: http://expects.readthedocs.io/en/latest
    :alt: Docs

.. image:: https://img.shields.io/badge/Licence-Apache2-brightgreen.svg
    :target: https://www.tldrlegal.com/l/apache2
    :alt: License

.. image:: https://img.shields.io/pypi/dm/expects.svg
    :target: https://pypi.python.org/pypi/expects
    :alt: Number of PyPI downloads

.. image:: https://secure.travis-ci.org/jaimegildesagredo/expects.svg?branch=master
    :target: http://travis-ci.org/jaimegildesagredo/expects
    :alt: Build status

**Expects** is an *expressive* and *extensible* TDD/BDD assertion library for Python. Expects can be *extended* by defining `new matchers <http://expects.readthedocs.io/en/latest/custom-matchers.html>`_.

Usage
-----

Just import the ``expect`` callable and the `built-in matchers <http://expects.readthedocs.io/en/latest/matchers.html>`_ and start writing test assertions.

.. code-block:: python

    from expects import *

    expect([]).to(be_empty)

    expect(False).not_to(be_true)

    expect({
        'name': 'Jack',
        'email': 'jack@example.com'
    }).to(have_key('name', match('\w+')))

    expect(str).to(have_property('split') & be_callable)

    expect(lambda: foo).to(raise_error(NameError))

    expect('Foo').to(equal('Bar') | equal('Foo'))

Installation
------------

You can install the last stable release of Expects from PyPI using pip or easy_install.

.. code-block:: bash

    $ pip install expects

Also you can install the latest sources from Github.

.. code-block:: bash

     $ pip install -e git+git://github.com/jaimegildesagredo/expects.git#egg=expects

Specs
-----

To run the Expects specs you should install the development requirements and then run `mamba`.

.. code-block:: bash

    $ pip install -r test-requirements.txt
    $ mamba

Changes
-------

See `Changes  <https://expects.readthedocs.io/en/latest/changes.html>`_.

3rd Party Matchers
------------------

See `3rd-Party Matchers list <http://expects.readthedocs.io/en/latest/3rd-party-matchers.html>`_.
