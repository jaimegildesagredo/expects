Expects
=======

**Expects** is an *expressive* and *extensible* TDD/BDD assertion library for Python. Expects can be *extended* by defining `new matchers <custom-matchers.html>`_.

.. code-block:: python

    expect([1, {'foo': 1}]).to(contain(have_key('foo', 2)))

.. admonition:: Failure
    :class: error

    expected: [1, {'foo': 1}] to contain have key 'foo' equal 2
         but: item have key 'foo' equal 2 not found

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

    expect(str).to(have_property('split') & be_callable)

    expect(lambda: foo).to(raise_error(NameError))

    expect('Foo').to(equal('Bar') | equal('Foo'))

Contents
--------

.. toctree::
   :maxdepth: 2

   install
   matchers
   aliases
   custom-matchers
   3rd-party-matchers
   changes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

