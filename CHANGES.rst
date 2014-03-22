Changes
=======

0.2.1 (not released yet)
------------------------

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
