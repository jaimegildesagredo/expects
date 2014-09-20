Expects
=======

**Expects** is an *expressive* and *extensible* TDD/BDD assertion library for Python. Expects can be *extended* by defining `new matchers <custom-matchers.html>`_.

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

