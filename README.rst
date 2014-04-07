Expects
=======

.. image:: https://secure.travis-ci.org/jaimegildesagredo/expects.svg?branch=master
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

You can see all the *builtin* assertions with lots of examples `here <http://expects.readthedocs.org/en/latest/reference.html>`_.

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

License
-------

Expects is released under the `Apache2 license <http://www.apache.org/licenses/LICENSE-2.0.html>`_.

Changes
-------

See `Changes  <https://expects.readthedocs.org/en/latest/changes.html>`_.

Documentation
-------------

Expects docs are hosted on `Read The Docs <https://expects.readthedocs.org>`_.
