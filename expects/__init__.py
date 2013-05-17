# -*- coding: utf-8 -*


class expect(object):
    def __init__(self, actual):
        self._actual = actual

        self.to = To(self._actual)


class To(object):
    def __init__(self, actual):
        self._actual = actual

        self.be = Be(self._actual)

    def equal(self, expected):
        assert self._actual == expected, 'Expected {} to equal {}'.format(
            repr(self._actual), repr(expected))


class Be(object):
    def __init__(self, actual):
        self._actual = actual

    def __call__(self, expected):
        assert self._actual is expected, 'Expected {} to be {}'.format(
            repr(self._actual), repr(expected))

    @property
    def true(self):
        assert self._actual, 'Expected {} to be True'.format(repr(self._actual))

    @property
    def false(self):
        assert not self._actual, 'Expected {} to be False'.format(repr(self._actual))
