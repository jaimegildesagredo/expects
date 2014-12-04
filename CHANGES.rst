Changes
=======

0.7.0 (Not released yet)
------------------------

Backwards-incompatible
^^^^^^^^^^^^^^^^^^^^^^

* The ``failure`` context manager now uses the ``end_with`` matcher as default matcher for failure message instead of the previously used ``contain`` matcher. Example::

    >>> from expects.testing import failure
    >>> with failure('foo'):
    ...     raise AssertionError('A foo message')
    AssertionError: Expected message 'A foo message' to end with 'foo'

    >>> with failure('message'):
    ...     raise AssertionError('A foo message')


0.6.1 (Nov 30, 2014)
--------------------

Bug fixes
^^^^^^^^^

* Now the ``contain`` and ``contain_exactly`` matchers fail with a proper message when used with a non-sequence type. See `GH-21 <https://github.com/jaimegildesagredo/expects/issues/21>`_.

0.6.0 (Nov 24, 2014)
--------------------

Highlights
^^^^^^^^^^

* Now the ``raise_error`` matcher can be used without specifying an exception class for writing less strict assertions::

    expect(lambda: foo).to(raise_error)

* Implemented the ``Matcher._match_value`` method to help develop custom matchers that receive another matchers. See the `docs <http://expects.readthedocs.org/en/latest/custom-matchers.html#expects.matchers.Matcher._match_value>`_ for more info.

* The ``specs`` and ``docs`` directories are now distributed with the source tarball. See `GH-20 <https://github.com/jaimegildesagredo/expects/pull/20>`_.

0.5.0 (Sep 20, 2014)
--------------------

Highlights
^^^^^^^^^^

* Now the ``&`` and ``|`` operators can be used to write simpler assertions::

    expect('Foo').to(have_length(3) & start_with('F'))
    expect('Foo').to(equal('Foo') | equal('Bar'))

* The ``testing.failure`` context manager can be used even without calling it with the failure message as argument::

    with failure:
        expect('foo').to(be_empty)

* Also can receive matchers as argument::

    with failure(end_with('empty')):
        expect('foo').to(be_empty)

.. note:: See also backwards-incompatible changes for ``testing.failure``.

* Added the ``be_callable`` matcher.
* Published a list of `3rd Party Matchers libraries <http://expects.readthedocs.org/en/latest/3rd-party-matchers.html>`_.


Bug fixes
^^^^^^^^^

* The ``be_within`` matcher now supports float values.
* In some places ``bytes`` were not being treated as a string type in python 3.

Backwards-incompatible
^^^^^^^^^^^^^^^^^^^^^^

* The ``match`` matcher now passes if matches a part of the subject string instead of all of it. Previously used the :func:`re.match` and now uses :func:`re.search`. If your tests depended on this you can migrate them by adding a ``'^'`` and ``'$'`` at the beginning and end of your regular expression.
* The ``testing.failure`` context manager not longer tries to match regular expressions. Instead you can pass the ``match`` matcher with your regexp.

0.4.2 (Ago 16, 2014)
--------------------

Highlights
^^^^^^^^^^

* Added the ``not_`` matcher to negate another matcher when composing matchers.

0.4.1 (Ago 16, 2014)
--------------------

Bug fixes
^^^^^^^^^

* Now ``from expects import *`` only imports the ``expect`` callable and *built in* matchers.

0.4.0 (Ago 15, 2014)
--------------------

Warnings
^^^^^^^^

This release *does not* maintain backwards compatibility with the previous version because a *new syntax was implemented* based on matchers. Matchers have been implemented maintaining compatibility with its equivalent assertions (and those that break compatibility are listed below). For most users upgrade to this version will only involve a migration to the new syntax.

Highlights
^^^^^^^^^^

* Improved failure message for ``have_keys`` and ``have_properties`` matchers.
* The ``raise_error`` matcher now can receive any other matcher as the second argument.

Bug fixes
^^^^^^^^^

* The ``have_key`` and ``have_keys`` always fail if the subject is not a dict.
* Fixed ``contain`` matcher behavior when negated. See `this commit <https://github.com/jaimegildesagredo/expects/commit/b240f14256c72fb1c53619ce19392bb28da77d88>`_.

Backwards-incompatible
^^^^^^^^^^^^^^^^^^^^^^

* The ``end_with`` matcher should receive args in the right order and not reversed. See `this commit <https://github.com/jaimegildesagredo/expects/commit/3be83da4e0c335efa02931e19b30233e1021fec3>`_.
* The ``to.have`` and ``to.have.only`` assertions have been remamed to ``contain`` and ``contain_exactly`` matchers.
* Assertion chaining has been replaced by *matcher composition* in all places where was possible in the previous version.
* The ``testing.failure`` context manager now only receives a string matching the failure message.

0.3.0 (Jun 29, 2014)
--------------------

Highlights
^^^^^^^^^^

* The `start_with <http://expects.readthedocs.org/en/v0.3.0/reference.html#start-with>`_ and `end_with <http://expects.readthedocs.org/en/v0.3.0/reference.html#end-with>`_ assertions now support lists, iterators and ordered dicts. `GH-16 <https://github.com/jaimegildesagredo/expects/issues/16>`_.

Bug fixes
^^^^^^^^^

* Fixes a regression in the ``raise_error`` assertion introduced in v0.2.2 which caused some tests to fail. See `GH-17 <https://github.com/jaimegildesagredo/expects/issues/17>`_ for more info.

0.2.3 (Jun 4, 2014)
-------------------

Highlights
^^^^^^^^^^

* Added the `start_with <http://expects.readthedocs.org/en/v0.2.3/reference.html#start-with>`_ and `end_with <http://expects.readthedocs.org/en/v0.2.3/#end-with>`_ assertions. `GH-14 <https://github.com/jaimegildesagredo/expects/issues/14>`_.

0.2.2 (May 20, 2014)
--------------------

Bug fixes
^^^^^^^^^

* `to.raise_error` now works with a non-string object as second arg. See docs for `examples <http://expects.readthedocs.org/en/0.2.2/reference.html#raise-error>`_.

0.2.1 (Mar 22, 2014)
--------------------

Highlights
^^^^^^^^^^

* Added a `testing` module with the `failure` contextmanager.
* Added a `matchers` module and the `key` matcher.

Bug fixes
^^^^^^^^^

* `to.have` and `to.only.have` now work properly when actual is a string.

0.2.0 (Feb 5, 2014)
-------------------

Highlights
^^^^^^^^^^

* Added initial plugins support. See `plugins docs <http://expects.readthedocs.org/en/0.2.0/plugins.html>`_ for more info.
* The ``key`` and ``property`` expectations now return a new ``Expects`` object that can be used to chain expectations.
* Now every expectation part can be prefixed with ``not_`` in order to negate an expectation. Ex: ``expect('foo').not_to.be.empty`` is the same than ``expect('foo').to.not_be.empty``.
* Added the ``only.have`` expectation to test that the subject *only* has the given items.

Backwards-incompatible
^^^^^^^^^^^^^^^^^^^^^^

* The ``greater_than``, ``greater_or_equal_to``, ``less_than`` and ``less_or_equal_to`` expectations are renamed to ``above``, ``above_or_equal``, ``below`` and ``below_or_equal``.

0.1.1 (Ago 20, 2013)
--------------------

Bug fixes
^^^^^^^^^

* `to.have` when iterable items are not hashable (`Issue #8 <https://github.com/jaimegildesagredo/expects/issues/8>`_).
* `to.have.key` weird behavior when actual is not a `dict` (`Issue #10 <https://github.com/jaimegildesagredo/expects/issues/10>`_).

0.1.0 (Ago 11, 2013)
--------------------

Highlights
^^^^^^^^^^

* First `expects` release.
