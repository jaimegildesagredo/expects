a
-

.. code-block:: python

    class Foo(object):
        bar = 0
        baz = 1
    
    obj = Foo()
    
    expect(obj).to.be.a(Foo)
    expect(obj).to.be.a(object)
    expect(obj).not_to.be.a(Bar)
    expect(obj).to.be.a(Bar)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to be a Bar instance

.. code-block:: python

    expect(obj).not_to.be.a(object)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to be a object instance

.. code-block:: python

    expect(obj).not_to.be.a(Foo)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to be a Foo instance

above
-----

.. code-block:: python

    expect(5).to.be.above(4)
    expect(1).not_to.be.above(4)
    expect(1).to.be.above(4)
.. admonition:: Failure
    :class: error

    Expected 1 to be above 4

.. code-block:: python

    expect(5).not_to.be.above(4)
.. admonition:: Failure
    :class: error

    Expected 5 not to be above 4

above_or_equal
--------------

.. code-block:: python

    expect(5).to.be.above_or_equal(4)
    expect(5).to.be.above_or_equal(5)
    expect(1).not_to.be.above_or_equal(4)
    expect(1).to.be.above_or_equal(4)
.. admonition:: Failure
    :class: error

    Expected 1 to be above or equal 4

.. code-block:: python

    expect(5).not_to.be.above_or_equal(4)
.. admonition:: Failure
    :class: error

    Expected 5 not to be above or equal 4

.. code-block:: python

    expect(5).not_to.be.above_or_equal(5)
.. admonition:: Failure
    :class: error

    Expected 5 not to be above or equal 5

an
--

.. code-block:: python

    class Foo(object):
        bar = 0
        baz = 1
    
    obj = Foo()
    
    expect(obj).to.be.an(object)
    expect(obj).not_to.be.an(Object)
    expect(obj).to.be.an(Object)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to be an Object instance

.. code-block:: python

    expect(obj).not_to.be.an(object)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to be an object instance

be
--

.. code-block:: python

    value = 1
    
    expect(value).to.be(value)
    expect(1).not_to.be(2)
    expect(1).to.be(2)
.. admonition:: Failure
    :class: error

    Expected 1 to be 2

.. code-block:: python

    expect(value).not_to.be(value)
.. admonition:: Failure
    :class: error

    Expected 1 not to be 1

below
-----

.. code-block:: python

    expect(1).to.be.below(4)
    expect(4).not_to.be.below(1)
    expect(4).to.be.below(1)
.. admonition:: Failure
    :class: error

    Expected 4 to be below 1

.. code-block:: python

    expect(1).not_to.be.below(4)
.. admonition:: Failure
    :class: error

    Expected 1 not to be below 4

below_or_equal
--------------

.. code-block:: python

    expect(1).to.be.below_or_equal(4)
    expect(5).to.be.below_or_equal(5)
    expect(4).not_to.be.below_or_equal(1)
    expect(4).to.be.below_or_equal(1)
.. admonition:: Failure
    :class: error

    Expected 4 to be below or equal 1

.. code-block:: python

    expect(1).not_to.be.below_or_equal(4)
.. admonition:: Failure
    :class: error

    Expected 1 not to be below or equal 4

.. code-block:: python

    expect(5).not_to.be.below_or_equal(5)
.. admonition:: Failure
    :class: error

    Expected 5 not to be below or equal 5

empty
-----

.. code-block:: python

    expect('').to.be.empty
    expect(iter('')).to.be.empty
    expect('foo').not_to.be.empty
    expect('foo').to.be.empty
.. admonition:: Failure
    :class: error

    Expected 'foo' to be empty

.. code-block:: python

    expect(iter('foo')).to.be.empty
.. admonition:: Failure
    :class: error

    Expected <str_iterator object at 0x7fd4832d6950> to be empty

.. code-block:: python

    expect('').not_to.be.empty
.. admonition:: Failure
    :class: error

    Expected '' not to be empty

equal
-----

.. code-block:: python

    expect(1).to.equal(1)
    expect(1).not_to.equal(2)
    expect(1).to.equal(2)
.. admonition:: Failure
    :class: error

    Expected 1 to equal 2

.. code-block:: python

    expect(1).not_to.equal(1)
.. admonition:: Failure
    :class: error

    Expected 1 not to equal 1

false
-----

.. code-block:: python

    expect(False).to.be.false
    expect(True).not_to.be.false
    expect(True).to.be.false
.. admonition:: Failure
    :class: error

    Expected True to be False

.. code-block:: python

    expect(False).not_to.be.false
.. admonition:: Failure
    :class: error

    Expected False not to be False

have
----

.. code-block:: python

    lst = ['bar', 'baz]
    itr = iter(lst)
    
    expect(lst).to.have('bar')
    expect(lst).to.have('bar', 'baz')
    expect([{'foo': 1}, 'bar']).to.have({'foo': 1})
    expect(itr).to.have('bar')
    expect(itr).to.have('bar', 'baz')
    expect(lst).not_to.have('foo')
    expect(lst).not_to.have('foo', 'foobar')
    expect(['bar']).to.only.have('bar')
    expect(lst).to.only.have('bar', 'baz')
    expect(lst).to.have('bar', 'foo')
.. admonition:: Failure
    :class: error

    Expected ['bar', 'baz'] to have 'foo'

.. code-block:: python

    expect(itr).to.have('bar', 'foo')
.. admonition:: Failure
    :class: error

    Expected <listiterator object at 0x7ff289cb4310> to have 'foo'

.. code-block:: python

    expect(lst).not_to.have('bar', 'foo')
.. admonition:: Failure
    :class: error

    Expected ['bar', 'baz'] not to have 'bar'

.. code-block:: python

    expect(lst).to.only.have('foo')
.. admonition:: Failure
    :class: error

    Expected ['bar', 'baz'] to only have 'foo'

.. code-block:: python

    expect(lst).to.only.have('foo', 'fuu')
.. admonition:: Failure
    :class: error

    Expected ['bar', 'baz'] to only have 'foo' and 'fuu'

.. code-block:: python

    expect(lst).to.only.have('bar')
.. admonition:: Failure
    :class: error

    Expected ['bar', 'baz'] to only have 'bar'

.. code-block:: python

    expect(lst).to.only.have('bar', 'baz')
.. admonition:: Failure
    :class: error

    Expected ['bar', 'baz'] to only have 'bar' and 'baz'

.. code-block:: python

    expect(lst).to.only.have('bar', 'baz', 'foo')
.. admonition:: Failure
    :class: error

    Expected ['bar', 'baz'] to only have 'bar', 'baz' and 'foo'

key
---

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.key('bar')
    expect({'bar': 0, 'baz': 1}).to.have.key('bar', 0)
    expect({'bar': 0, 'baz': 1}).not_to.have.key('foo')
    expect({'bar': 0, 'baz': 1}).not_to.have.key('foo', 0)
    expect({'bar': 0, 'baz': 1}).not_to.have.key('bar', 1)
    expect('My foo string').not_to.have.key('foo', 0)
    expect({'bar': 0, 'baz': 1}).to.have.key('bar').with_value.equal(0)
    expect({'bar': 0, 'baz': 1}).to.have.key('bar').with_value.not_equal(1)
    expect({'bar': 0, 'baz': 1}).to.have.key('foo')
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'foo'

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.key('foo', 0)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'foo'

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.key('bar', 1)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'bar' with value 1 but was 0

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.key('bar', None)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'bar' with value None but was 0

.. code-block:: python

    expect('My foo string').to.have.key('foo', 0)
.. admonition:: Failure
    :class: error

    Expected 'My foo string' to have key 'foo' but not a dict

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to.have.key('bar')
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} not to have key 'bar'

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to.have.key('bar', 0)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} not to have key 'bar' with value 0 but was 0

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.key('bar').with_value.equal(1)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'bar' with value 0 equal 1

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.key('bar').with_value.not_equal(0)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'bar' with value 0 not equal 0

keys
----

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.keys('bar', 'baz')
    expect({'bar': 0, 'baz': 1}).to.have.keys(bar=0, baz=1)
    expect({'bar': 0, 'baz': 1}).to.have.keys('bar', baz=1)
    expect({'bar': 0, 'baz': 1}).to.have.keys({'bar': 0, 'baz': 1})
    expect({'bar': 0, 'baz': 1}).not_to.have.keys('foo', 'foobar')
    expect({'bar': 0, 'baz': 1}).not_to.have.keys(foo=0, foobar=1)
    expect({'bar': 0, 'baz': 1}).not_to.have.keys(foo=0, bar=1)
    expect({'bar': 0, 'baz': 1}).not_to.have.keys({'foo': 0, 'foobar': 1})
    expect({'bar': 0, 'baz': 1}).not_to.have.keys({'foo': 0, 'bar': 1})
    expect({'bar': 0, 'baz': 1}).to.have.keys('bar', 'foo')
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'foo'

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.keys(bar=0, foo=1)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'foo'

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.keys(bar=1, baz=1)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'bar' with value 1 but was 0

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.keys('foo', bar=0)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'foo'

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.keys('baz', bar=1)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'bar' with value 1 but was 0

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).to.have.keys({'bar': 1, 'baz': 1})
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} to have key 'bar' with value 1 but was 0

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to.have.keys('foo', 'bar')
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} not to have key 'bar'

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to.have.keys(baz=0, bar=0)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} not to have key 'bar' with value 0 but was 0

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to.have.keys('bar', baz=0)
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} not to have key 'bar'

.. code-block:: python

    expect({'bar': 0, 'baz': 1}).not_to.have.keys({'bar': 0, 'foo': 1})
.. admonition:: Failure
    :class: error

    Expected {'bar': 0, 'baz': 1} not to have key 'bar' with value 0 but was 0

length
------

.. code-block:: python

    expect('foo').to.have.length(3)
    expect(iter('foo')).to.have.length(3)
    expect('foo').not_to.have.length(2)
    expect('foo').to.have.length(2)
.. admonition:: Failure
    :class: error

    Expected 'foo' to have length 2 but was 3

.. code-block:: python

    expect(iter('foo')).to.have.length(2)
.. admonition:: Failure
    :class: error

    Expected <str_iterator object at 0x7fd4832d6950> to have length 2 but was 3

.. code-block:: python

    expect('foo').not_to.have.length(3)
.. admonition:: Failure
    :class: error

    Expected 'foo' not to have length 3 but was 3

match
-----

.. code-block:: python

    str_ = 'My foo string'

    expect(str_).to.match(r'My \w+ string')
    expect(str_).to.match(r'my [A-Z]+ strinG', re.I)
    expect(str_).not_to.match(r'My \W+ string')
    expect(str_).not_to.match(r'My \W+ string', re.I)
    expect(str_).to.match(pattern)
.. admonition:: Failure
    :class: error

    Expected 'My foo string' to match r'My \\W+ string'

.. code-block:: python

    expect(str_).not_to.match(r'My \w+ string')
.. admonition:: Failure
    :class: error

    Expected 'My foo string' not to match r'My \\w+ string'

none
----

.. code-block:: python

    expect(None).to.be.none
    expect('foo').not_to.be.none
    expect(True).to.be.none
.. admonition:: Failure
    :class: error

    Expected True to be None

.. code-block:: python

    expect(None).not_to.be.none
.. admonition:: Failure
    :class: error

    Expected None not to be None

properties
----------

.. code-block:: python

    class Foo(object):
        bar = 0
        baz = 1
    
    obj = Foo()
    
    expect(obj).to.have.properties('bar', 'baz')
    expect(obj).to.have.properties(bar=0, baz=1)
    expect(obj).to.have.properties('bar', baz=1)
    expect(obj).to.have.properties({'bar': 0, 'baz': 1})
    expect(obj).not_to.have.properties('foo', 'foobar')
    expect(obj).not_to.have.properties(foo=0, foobar=1)
    expect(obj).not_to.have.properties(foo=0, bar=1)
    expect(obj).not_to.have.properties({'foo': 0, 'foobar': 1})
    expect(obj).not_to.have.properties({'foo': 0, 'bar': 1})
    expect(obj).to.have.properties('bar', 'foo')
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'foo'

.. code-block:: python

    expect(obj).to.have.properties(bar=0, foo=1)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'foo'

.. code-block:: python

    expect(obj).to.have.properties(bar=1, baz=1)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'bar' with value 1 but was 0

.. code-block:: python

    expect(obj).to.have.properties('foo', bar=0)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'foo'

.. code-block:: python

    expect(obj).to.have.properties('baz', bar=1)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'bar' with value 1 but was 0

.. code-block:: python

    expect(obj).to.have.properties({'bar': 1, 'baz': 1})
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'bar' with value 1 but was 0

.. code-block:: python

    expect(obj).not_to.have.properties('foo', 'bar')
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to have property 'bar'

.. code-block:: python

    expect(obj).not_to.have.properties(baz=0, bar=0)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to have property 'bar' with value 0 but was 0

.. code-block:: python

    expect(obj).not_to.have.properties('bar', baz=0)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to have property 'bar'

.. code-block:: python

    expect(obj).not_to.have.properties('foo', bar=0)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to have property 'bar' with value 0 but was 0

.. code-block:: python

    expect(obj).not_to.have.properties({'bar': 0, 'foo': 1})
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to have property 'bar' with value 0 but was 0

property
--------

.. code-block:: python

    class Foo(object):
        bar = 0
        baz = 1
    
    obj = Foo()
    
    expect(obj).to.have.property('bar')
    expect(obj).to.have.property('bar', 0)
    expect(obj).not_to.have.property('foo')
    expect(obj).not_to.have.property('foo', 0)
    expect(obj).not_to.have.property('bar', 1)
    expect(obj).to.have.property('bar').with_value.equal(0)
    expect(obj).to.have.property('bar').with_value.not_equal(1)
    expect(expect(obj).to.have.property('bar', 0)).to.be.none
    expect(obj).to.have.property('foo')
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'foo'

.. code-block:: python

    expect(obj).to.have.property('foo', 0)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'foo'

.. code-block:: python

    expect(obj).to.have.property('bar', 1)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'bar' with value 1 but was 0

.. code-block:: python

    expect(obj).to.have.property('bar', None)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'bar' with value None but was 0

.. code-block:: python

    expect(obj).not_to.have.property('bar')
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to have property 'bar'

.. code-block:: python

    expect(obj).not_to.have.property('bar', 0)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> not to have property 'bar' with value 0 but was 0

.. code-block:: python

    expect(obj).to.have.property('bar').with_value.equal(1)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'bar' with value 0 equal 1

.. code-block:: python

    expect(obj).to.have.property('bar').with_value.not_equal(0)
.. admonition:: Failure
    :class: error

    Expected <Foo object at 0x7ff289cb4310> to have property 'bar' with value 0 not equal 0

raise_error
-----------

.. code-block:: python

    def callback():
        raise AttributeError('error message')

    expect(callback).to.raise_error(AttributeError)
    expect(callback).to.raise_error(AttributeError, 'error message')
    expect(callback).to.raise_error(AttributeError, r'error \w+')

    def callback():
        raise KeyError()

    expect(callback).to.raise_error(AttributeError)
.. admonition:: Failure
    :class: error

    Expected <function callback at 0x7fe70cb103b0> to raise AttributeError but KeyError raised

.. code-block:: python

    expect(lambda: None).to.raise_error(AttributeError)
.. admonition:: Failure
    :class: error

    Expected <function <lambda> at 0x7f3e670863b0> to raise AttributeError but not raised

.. code-block:: python

    def callback():
        raise AttributeError('bar')

    expect(callback).to.raise_error(AttributeError, 'foo')
.. admonition:: Failure
    :class: error

    Expected callback to raise AttributeError with message 'foo' but message was 'bar'

true
----

.. code-block:: python

    expect(True).to.be.true
    expect(False).not_to.be.true
    expect(False).to.be.true
.. admonition:: Failure
    :class: error

    Expected False to be True

.. code-block:: python

    expect(True).not_to.be.true
.. admonition:: Failure
    :class: error

    Expected True not to be True

within
------

.. code-block:: python

    expect(5).to.be.within(4, 7)
    expect(1).not_to.be.within(4, 7)
    expect(1).to.be.within(4, 7)
.. admonition:: Failure
    :class: error

    Expected 1 to be within 4, 7

.. code-block:: python

    expect(5).not_to.be.within(4, 7)
.. admonition:: Failure
    :class: error

    Expected 5 not to be within 4, 7

