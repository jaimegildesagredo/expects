equal
-----

.. code-block:: python

    expect(1).to(equal(1))

    expect(1).not_to(equal(2))

    expect(1).to(equal(2))

.. admonition:: Failure
    :class: error

    Expected ``1`` to equal ``2``

.. code-block:: python

    expect(1).not_to(equal(1))

.. admonition:: Failure
    :class: error

    Expected ``1`` not to equal ``1``

be
--

.. code-block:: python

    class Foo(object):
        pass

    value = Foo()

    expect(value).to(be(value))

    expect(1).not_to(be(2))

    expect(1).to(be(2))

.. admonition:: Failure
    :class: error

    Expected ``1`` to be ``2``

.. code-block:: python

    expect(value).not_to(be(value))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` not to be ``<Foo object at 0x7ff289cb4310>``

be_true
-------

.. code-block:: python

    expect(True).to(be_true)

    expect(False).not_to(be_true)

    expect(False).to(be_true)

.. admonition:: Failure
    :class: error

    Expected ``False`` to be ``True``

.. code-block:: python

    expect(True).not_to(be_true)

.. admonition:: Failure
    :class: error

    Expected ``True`` not to be ``True``

be_false
--------

.. code-block:: python

    expect(False).to(be_false)

    expect(True).not_to(be_false)

    expect(True).to(be_false)

.. admonition:: Failure
    :class: error

    Expected ``True`` to be ``False``

.. code-block:: python

    expect(False).not_to(be_false)

.. admonition:: Failure
    :class: error

    Expected ``False`` not to be ``False``

be_none
-------

.. code-block:: python

    expect(None).to(be_none)

    expect('foo').not_to(be_none)

    expect(True).to(be_none)

.. admonition:: Failure
    :class: error

    Expected ``True`` to be ``None``

.. code-block:: python

    expect(None).not_to(be_none)

.. admonition:: Failure
    :class: error

    Expected ``None`` not to be ``None``

be_a / be_an
------------

.. code-block:: python

    class Foo(object):
        pass

    class Bar(object):
        pass

    class Object(object):
        pass

    expect(Foo()).to(be_a(Foo))

    expect(Foo()).not_to(be_a(Bar))

    expect(Foo()).to(be_an(object))

    expect(Foo()).not_to(be_an(Object))

    expect(Foo()).to(be_a(Bar))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to be a ``Bar``

.. code-block:: python

    expect(Foo()).to_not(be_a(Foo))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` not to be a ``Foo``

.. code-block:: python

    expect(Foo()).to(be_an(Object))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to be an ``Object``

.. code-block:: python

    expect(Foo()).not_to(be_an(object))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` not to be an ``object``

be_empty
--------

.. code-block:: python

    expect('').to(be_empty)

    expect(iter('')).to(be_empty)

    expect('foo').not_to(be_empty)

    expect('foo').to(be_empty)

.. admonition:: Failure
    :class: error

    Expected ``'foo'`` to be empty

.. code-block:: python

    expect(iter('foo')).to(be_empty)

.. admonition:: Failure
    :class: error

    Expected ``<str_iterator object at 0x7fd4832d6950>`` to be empty

.. code-block:: python

    expect('').to_not(be_empty)

.. admonition:: Failure
    :class: error

    Expected ``''`` not to be empty

be_above
--------

.. code-block:: python

    expect(5).to(be_above(4))

    expect(1).not_to(be_above(4))

    expect(1).to(be_above(4))

.. admonition:: Failure
    :class: error

    Expected ``1`` to be above ``4``

.. code-block:: python

    expect(5).not_to(be_above(4))

.. admonition:: Failure
    :class: error

    Expected ``5`` not to be above ``4``

be_below
--------

.. code-block:: python

    expect(1).to(be_below(4))

    expect(4).not_to(be_below(1))

    expect(4).to(be_below(1))

.. admonition:: Failure
    :class: error

    Expected ``4`` to be below ``1``

.. code-block:: python

    expect(1).not_to(be_below(4))

.. admonition:: Failure
    :class: error

    Expected ``1`` not to be below ``4``

be_above_or_equal
-----------------

.. code-block:: python

    expect(5).to(be_above_or_equal(4))

    expect(5).to(be_above_or_equal(5))

    expect(1).to_not(be_above_or_equal(4))

    expect(1).to(be_above_or_equal(4))

.. admonition:: Failure
    :class: error

    Expected ``1`` to be above or equal ``4``

.. code-block:: python

    expect(5).not_to(be_above_or_equal(4))

.. admonition:: Failure
    :class: error

    Expected ``5`` not to be above or equal ``4``

.. code-block:: python

    expect(5).not_to(be_above_or_equal(5))

.. admonition:: Failure
    :class: error

    Expected ``5`` not to be above or equal ``5``

be_below_or_equal
-----------------

.. code-block:: python

    expect(1).to(be_below_or_equal(4))

    expect(5).to(be_below_or_equal(5))

    expect(4).not_to(be_below_or_equal(1))

    expect(4).to(be_below_or_equal(1))

.. admonition:: Failure
    :class: error

    Expected ``4`` to be below or equal ``1``

.. code-block:: python

    expect(1).not_to(be_below_or_equal(4))

.. admonition:: Failure
    :class: error

    Expected ``1`` not to be below or equal ``4``

.. code-block:: python

    expect(5).not_to(be_below_or_equal(5))

.. admonition:: Failure
    :class: error

    Expected ``5`` not to be below or equal ``5``

be_within
---------

.. code-block:: python

    expect(5).to(be_within(4, 7))

    expect(5.5).to(be_within(4, 7))

    expect(1).not_to(be_within(4, 7))

    expect(1).to(be_within(4, 7))

.. admonition:: Failure
    :class: error

    Expected ``1`` to be within ``4, 7``

.. code-block:: python

    expect(5).not_to(be_within(4, 7))

.. admonition:: Failure
    :class: error

    Expected ``5`` not to be within ``4, 7``

be_callable
-----------

.. code-block:: python

    expect(lambda: None).to(be_callable)

    expect('foo').to(be_callable)

.. admonition:: Failure
    :class: error

    Expected ``'foo'`` to be callable

have_len / have_length
----------------------

.. code-block:: python

    expect('foo').to(have_len(3))

    expect('foo').to(have_len(be_above_or_equal(3)))

    expect(iter('foo')).to(have_length(3))

    expect('foo').not_to(have_len(2))

    expect('foo').to(have_length(2))

.. admonition:: Failure
    :class: error

    Expected ``'foo'`` to have length ``2``

.. code-block:: python

    expect('foo').to(have_len(be_bellow(2)))

.. admonition:: Failure
    :class: error

    Expected ``'foo'`` to have len be bellow ``2``
.. code-block:: python

    expect(iter('foo')).to(have_len(2))

.. admonition:: Failure
    :class: error

    Expected ``<str_iterator object at 0x7fd4832d6950>`` to have len ``2``

.. code-block:: python

    expect('foo').not_to(have_len(3))

.. admonition:: Failure
    :class: error

    Expected ``'foo'`` not to have len ``3``

have_property
-------------

.. code-block:: python

    class Foo(object):
        def __init__(self, **kwargs):
            for name, value in kwargs.items():
                setattr(self, name, value)

    expect(Foo(bar=0, baz=1)).to(have_property('bar'))

    expect(Foo(bar=0, baz=1)).to(have_property('bar', 0))

    expect(Foo(bar=0, baz=1)).not_to(have_property('foo'))

    expect(Foo(bar=0, baz=1)).not_to(have_property('foo', 0))

    expect(Foo(bar=0, baz=1)).not_to(have_property('bar', 1))

    expect(Foo(bar=0, baz=1)).to(have_property('bar', be_below(1)))

    expect(Foo(bar=0, baz=1)).to(have_property('bar', not_(be_above(1))))

    expect(Foo(bar=0, baz=1)).to(have_property('foo'))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have property ``'foo'``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_property('foo', 0))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have property ``'foo'`` equal ``0``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_property('bar', 1))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have property ``'bar'`` equal ``1``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_property('bar', None))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have property ``'bar'`` equal ``None``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).not_to(have_property('bar'))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` not to have property ``'bar'``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).not_to(have_property('bar', 0))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` not to have property ``'bar'`` equal ``0``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_property('bar', be_above(1)))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have property ``'bar'`` be above ``1``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_property('bar', not_(be_below(1))))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have property ``'bar'`` not be below ``1``

have_properties
---------------

.. code-block:: python

    class Foo(object):
        def __init__(self, **kwargs):
            for name, value in kwargs.items():
                setattr(self, name, value)

    expect(Foo(bar=0, baz=1)).to(have_properties('bar', 'baz'))

    expect(Foo(bar=0, baz=1)).to(have_properties(bar=0, baz=1))

    expect(Foo(bar=0, baz=1)).to(have_properties('bar', baz=1))

    expect(Foo(bar=0, baz=1)).to(have_properties({'bar': 0, 'baz': 1}))

    expect(Foo(bar=0, baz=1)).to(have_properties(bar=be_an(int)))

    expect(Foo(bar=0, baz=1)).to_not(have_properties('foo', 'foobar'))

    expect(Foo(bar=0, baz=1)).to_not(have_properties(foo=0, foobar=1))

    expect(Foo(bar=0, baz=1)).not_to(have_properties(foo=0, bar=1))

    expect(Foo(bar=0, baz=1)).not_to(have_properties({'foo': 0, 'foobar': 1}))

    expect(Foo(bar=0, baz=1)).not_to(have_properties({'foo': 0, 'bar': 1}))

    expect(Foo(bar=0, baz=1)).not_to(have_properties('foo', 'bar'))

    expect(Foo(bar=0, baz=1)).to(have_properties('bar', 'foo'))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have properties ``'bar'`` and ``'foo'``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_properties(bar=0, foo=1))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have properties ``'bar'`` equal ``0`` and ``'foo'`` equal ``1``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_properties(bar=1, baz=1))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have properties ``'bar'`` equal ``1`` and ``'baz'`` equal ``1``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_properties('foo', bar=0))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have properties ``'foo'`` and ``'bar'`` equal ``0``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_properties('baz', bar=1))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have properties ``'baz'`` and ``'bar'`` equal ``1``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_properties({'bar': 1, 'baz': 1}))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` to have properties ``'bar'``  equal ``1`` and ``'baz'`` equal ``1``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).not_to(have_properties('bar', 'baz'))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` not to have properties ``'bar'``  and ``'baz'``

.. code-block:: python

    expect(Foo(bar=0, baz=1)).not_to(have_properties(bar=0, baz=1))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` not to have properties ``'bar'`` equal ``0`` and ``'baz'`` equal ``1``


.. code-block:: python

    expect(Foo(bar=0, baz=1)).to(have_properties(bar=be_a(str)))

.. admonition:: Failure
    :class: error

    Expected ``<Foo object at 0x7ff289cb4310>`` not to have properties ``'bar'`` be a ``str``

have_key
--------

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_key('bar'))

    expect({'bar': 0, 'baz': 1}).to(have_key('bar', 0))

    expect({'bar': 0, 'baz': 1}).not_to(have_key('foo'))

    expect({'bar': 0, 'baz': 1}).not_to(have_key('foo', 0))

    expect({'bar': 0, 'baz': 1}).to_not(have_key('bar', 1))

    expect({'bar': 0, 'baz': 1}).to(have_key('bar', be_below(1)))

    expect({'bar': 0, 'baz': 1}).to(have_key('foo'))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have key ``'foo'``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_key('foo', 0))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have key ``'foo'`` equal ``0``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_key('bar', 1))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have key ``'bar'`` equal ``1``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_key('bar', None))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have key ``'bar'`` equal ``None``

.. code-block:: python

    expect('My foo string').to(have_key('foo', 0))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have key ``'foo'`` equal ``0`` but is not a dict

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to(have_key('bar'))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` not to have key ``'bar'``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to(have_key('bar', 0))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` not to have key ``'bar'`` equal ``0``

.. code-block:: python

    expect('My foo string').not_to(have_key('foo', 0))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` not to have key ``'foo'`` equal ``0`` but is not a dict

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_key('bar', be_above(1)))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have key ``'bar'`` be above ``1``

have_keys
---------

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_keys('bar', 'baz'))

    expect({'bar': 0, 'baz': 1}).to(have_keys(bar=0, baz=1))

    expect({'bar': 0, 'baz': 1}).to(have_keys('bar', baz=1))

    expect({'bar': 0, 'baz': 1}).to(have_keys({'bar': 0, 'baz': 1}))

    expect({'bar': 0, 'baz': 1}).not_to(have_keys('foo', 'foobar'))

    expect({'bar': 0, 'baz': 1}).not_to(have_keys(foo=0, foobar=1))

    expect({'bar': 0, 'baz': 1}).not_to(have_keys(foo=0, bar=1))

    expect({'bar': 0, 'baz': 1}).not_to(have_keys({'foo': 0, 'foobar': 1}))

    expect({'bar': 0, 'baz': 1}).not_to(have_keys('foo', 'bar'))

    expect({'bar': 0, 'baz': 1}).to(have_keys('bar', 'foo'))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have keys ``'bar'`` and ``'foo'``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_keys(bar=0, foo=1))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have keys ``'bar'`` equal ``0`` and ``'foo'`` equal ``1``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_keys(bar=1, baz=1))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have keys ``'bar'`` equal ``1`` and ``'baz'`` equal ``1``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_keys('foo', 'fuu', bar=0))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have keys ``'foo'``, ``'fuu'`` and ``'bar'`` equal ``0``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_keys('baz', bar=1))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have keys ``'baz'`` and ``'bar'`` equal ``1``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(have_keys({'bar': 1, 'baz': 1}))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have keys ``'bar'`` equal ``1`` and ``'baz'`` equal ``1``

.. code-block:: python

    expect('My foo string').to(have_keys({'bar': 1, 'baz': 1}))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to have keys ``'bar'`` equal ``1`` and ``'baz'`` equal ``1`` but is not a dict

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to(have_keys('bar', 'baz'))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` not to have keys ``'bar'`` and ``'baz'``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to(have_keys(bar=0, baz=1))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` not to have keys ``'bar'`` equal ``0`` and ``'baz'`` equal ``1``

.. code-block:: python

    expect('My foo string').not_to(have_keys({'bar': 1, 'baz': 1}))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` not to have keys ``'bar'`` equal ``1`` and ``'baz'`` equal ``1`` but is not a dict

contain
-------

.. code-block:: python

    expect(['bar', 'baz']).to(contain('bar'))

    expect(['bar', 'baz']).to(contain('bar', 'baz'))

    expect(['bar', 'baz']).to(contain('baz', 'bar'))

    expect([{'foo': 1}, 'bar']).to(contain({'foo': 1}))

    expect(iter(['bar', 'baz'])).to(contain('bar'))

    expect(iter(['bar', 'baz'])).to(contain('bar', 'baz'))

    expect('My foo string').to(contain('foo'))

    expect('My foo string').to(contain('foo', 'string'))

    expect(['bar', 'baz']).not_to(contain('foo'))

    expect(['bar', 'baz']).not_to(contain('foo', 'foobar'))

    expect(['bar', 'baz']).not_to(contain('bar', 'foo'))

    expect(['bar', 'baz']).to(contain(be_a(str)))

    expect(['bar', 'baz']).to(contain('bar', 'foo'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain ``'bar'`` and ``'foo'``

.. code-block:: python

    expect(iter(['bar', 'baz'])).to(contain('bar', 'foo'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain ``'bar'`` and ``'foo'``

.. code-block:: python

    expect(object()).to(contain('bar'))

.. admonition:: Failure
    :class: error

    Expected ``<object object at 0x7f5004aa1070>`` to contain ``'bar'`` but is not a valid sequence type

.. code-block:: python

    expect(['bar', 'baz']).not_to(contain('bar'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` not to contain ``'bar'``

.. code-block:: python

    expect(['bar', 'baz']).not_to(contain('bar', 'baz'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` not to contain ``'bar'`` and ``'baz'``

.. code-block:: python

    expect(object()).not_to(contain('bar'))

.. admonition:: Failure
    :class: error

    Expected ``<object object at 0x7f5004aa1070>`` not to contain ``'bar'`` but is not a valid sequence type

.. code-block:: python

    expect(['bar', 'baz']).to(contain(be_an(int), have_len(5)))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain be an ``int`` and have len ``5``

contain_exactly
---------------

.. code-block:: python

    expect(['bar']).to(contain_exactly('bar'))

    expect(['bar', 'baz']).to(contain_exactly('bar', 'baz'))

    expect('My foo string').to(contain_exactly('My foo string'))

    expect('My foo string').to(contain_exactly('My foo', ' string'))

    expect(['bar', 'baz']).to(contain_exactly(equal('bar'), equal('baz')))

    expect(['bar', 'baz']).to(contain_exactly('foo'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain exactly ``'foo'``

.. code-block:: python

    expect(['bar', 'baz']).to(contain_exactly('foo', 'fuu'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain exactly ``'foo'`` and ``'fuu'``

.. code-block:: python

    expect(['bar', 'baz']).to(contain_exactly('baz', 'bar'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain exactly ``'baz'`` and ``'bar'``

.. code-block:: python

    expect(['bar', 'baz']).to(contain_exactly('bar'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain exactly ``'bar'``

.. code-block:: python

    expect(['bar', 'baz', 'foo']).to(contain_exactly('bar', 'baz'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz', 'foo']`` to contain exactly ``'bar'`` and ``'baz'``

.. code-block:: python

    expect(['bar', 'baz', 'foo', 'fuu']).to(contain_exactly('bar', 'baz', 'foo'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz', 'foo', 'fuu']`` to contain exactly ``'bar'``, ``'baz'`` and ``'foo'``

.. code-block:: python

    expect('My foo string').to(contain_exactly('foo'))

.. admonition:: Failure
    :class: error

    Expected ``'My foo string'`` to contain exactly ``'foo'``

.. code-block:: python

    expect(object()).to(contain_exactly('bar'))

.. admonition:: Failure
    :class: error

    Expected ``<object object at 0x7f5004aa1070>`` to contain exactly ``'bar'`` but is not a valid sequence type

.. code-block:: python

    expect(['bar', 'baz']).to(contain_exactly(equal('baz'), equal('baz')))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain exactly equal ``'bar'`` and equal ``'baz'``

contain_only
------------

.. code-block:: python

    expect(['bar']).to(contain_only('bar'))

    expect(['bar', 'baz']).to(contain_only(['baz', 'bar']))

    expect(iter(['bar', 'baz'])).to(contain_only('bar', 'baz'))

    expect('My foo string').to(contain_only('My foo string'))

    expect('My foo string').to(contain_only('My foo', ' string'))

    expect(['bar', 'baz']).to(contain_only(equal('bar'), equal('baz')))

    expect(['bar', 'baz']).to(contain_only('foo'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain only ``'foo'``

.. code-block:: python

    expect(['bar', 'baz', 'foo']).to(contain_only('bar', 'baz'))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz', 'foo']`` to contain only ``'bar'`` and ``'baz'``

.. code-block:: python

    expect('My foo string').to(contain_only('foo'))

.. admonition:: Failure
    :class: error

    Expected ``'My foo string'`` to contain only ``'foo'``

.. code-block:: python

    expect(object()).to(contain_only('bar'))

.. admonition:: Failure
    :class: error

    Expected ``<object object at 0x7f5004aa1070>`` to contain only ``'bar'`` but is not a valid sequence type

.. code-block:: python

    expect(['bar', 'baz']).to(contain_only(equal('baz'), equal('foo')))

.. admonition:: Failure
    :class: error

    Expected ``['bar', 'baz']`` to contain only equal ``'baz'`` and equal ``'foo'``

start_with
----------

.. code-block:: python

    expect('My foo string').to(start_with('My foo'))

    expect('My foo string').not_to(start_with('tring'))

    expect([1, 2, 3]).to(start_with(1))

    expect([1, 2, 3]).to(start_with(1, 2))

    expect(OrderedDict([('bar', 0), ('baz', 1)])).to(start_with('bar', 'baz'))

    expect(iter([1, 2, 3])).to(start_with(1, 2))

    expect([1, 2, 3]).not_to(start_with(2, 3))

    expect([1, 2, 3]).not_to(start_with(1, 1))

    expect('My foo string').to(start_with('tring'))

.. admonition:: Failure
    :class: error

    Expected ``'My foo string'`` to start with ``'tring'``

.. code-block:: python

    expect([1, 2, 3]).to(start_with(2))

.. admonition:: Failure
    :class: error

    Expected ``[1, 2, 3]`` to start with ``2``

.. code-block:: python

    expect([1, 2, 3]).to(start_with(2, 3))

.. admonition:: Failure
    :class: error

    Expected ``[1, 2, 3]`` to start with ``2`` and ``3``

.. code-block:: python

    expect([1, 2, 3]).to(start_with(1, 1))

.. admonition:: Failure
    :class: error

    Expected ``[1, 2, 3]`` to start with ``1`` and ``1``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(start_with('bar', 'baz'))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to start with ``'bar'`` and ``'baz'`` but it does not have ordered keys

end_with
--------

.. code-block:: python

    expect('My foo string').to(end_with('tring'))

    expect('My foo string').not_to(end_with('My foo'))

    expect([1, 2, 3]).to(end_with(3))

    expect([1, 2, 3]).to(end_with(2, 3))

    expect(OrderedDict([('bar', 0), ('baz', 1)])).to(end_with('bar, 'baz'))

    expect([1, 2, 3]).to_not(end_with(1, 2))

    expect([1, 2, 3]).to_not(end_with(3, 3))

    expect('My foo string').to(end_with('My fo'))

.. admonition:: Failure
    :class: error

    Expected ``'My foo string'`` to end with ``'My fo'``

.. code-block:: python

    expect([1, 2, 3]).to(end_with(3, 3))

.. admonition:: Failure
    :class: error

    Expected ``[1, 2, 3]`` to end with ``3`` and ``3``

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to(end_with('baz', 'bar'))

.. admonition:: Failure
    :class: error

    Expected ``{'bar': 0, 'baz': 1}`` to end with ``'baz'`` and ``'bar'`` but it does not have ordered keys

match
-----

.. code-block:: python

    expect('My foo string').to(match(r'My \w+ string'))

    expect('My foo string').to(match(r'\w+ string'))

    expect('My foo string').to(match(r'my [A-Z]+ strinG', re.I))

    expect('My foo string').not_to(match(r'My \W+ string'))

    expect('My foo string').not_to(match(r'My \W+ string', re.I))

    expect('My foo string').to(match(pattern))

.. admonition:: Failure
    :class: error

    Expected ``'My foo string'`` to match ``r'My \\W+ string'``

.. code-block:: python

    expect('My foo string').not_to(match(r'My \w+ string'))

.. admonition:: Failure
    :class: error

    Expected ``'My foo string'`` not to match ``r'My \\w+ string'``

raise_error
-----------

.. code-block:: python

    def callback():
        raise AttributeError('error message')

    expect(callback).to(raise_error)

    expect(callback).to(raise_error(AttributeError))

    expect(callback).to(raise_error(AttributeError, 'error message'))

    expect(callback).to(raise_error(AttributeError, match(r'error \w+')))

    def callback():
        raise AttributeError(2)

    expect(callback).to(raise_error(AttributeError, 2))

    def callback():
        raise KeyError()

    expect(callback).to(raise_error(AttributeError))

.. admonition:: Failure
    :class: error

    Expected ``<function callback at 0x7fe70cb103b0>`` to raise ``AttributeError`` but ``KeyError`` raised

.. code-block:: python

    expect(lambda: None).to(raise_error(AttributeError))

.. admonition:: Failure
    :class: error

    Expected ``<function <lambda> at 0x7f3e670863b0>`` to raise ``AttributeError`` but not raised

.. code-block:: python

    def callback():
        raise AttributeError('bar')

    expect(callback).to(raise_error(AttributeError, 'foo'))

.. admonition:: Failure
    :class: error

    Expected ``<function callback at 0x7fe70cb103b0>`` to raise ``AttributeError`` with message ``'foo'`` but message was ``'bar'``
