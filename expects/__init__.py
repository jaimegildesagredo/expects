# -*- coding: utf-8 -*


class Expectation(object):
    def __init__(self, parent):
        self._parent = parent

        self.init()

    def init(self):
        pass

    @property
    def actual(self):
        return self._parent.actual


class Equal(Expectation):
    def __call__(self, expected):
        assert self.actual == expected, self.error_message(repr(expected))

    def error_message(self, tail):
        return self._parent.error_message('equal {}'.format(tail))


class Be(Expectation):
    def init(self):
        self.equal = Equal(self)

    def __call__(self, expected):
        assert self.actual is expected, self.error_message(repr(expected))

    @property
    def true(self):
        assert self.actual, self.error_message(True)

    @property
    def false(self):
        assert not self.actual, self.error_message(False)

    def error_message(self, tail):
        return self._parent.error_message('be {}'.format(tail))


class Have(Expectation):
    def property(self, *args):
        name = args[0]

        def error_message(tail):
            return self.error_message('property {}'.format(tail))

        assert hasattr(self.actual, name), error_message(repr(name))

        try:
            expected = args[1]
        except IndexError:
            pass
        else:
            value = getattr(self.actual, name)

            assert value == expected, error_message('{} with value {} but was {}'.format(
                repr(name), repr(expected), repr(value)))

    def error_message(self, tail):
        return self._parent.error_message('have {}'.format(tail))


class To(Expectation):
    def init(self):
        self.be = Be(self)
        self.have = Have(self)
        self.equal = Equal(self)

    def raise_error(self, expected, message=None):
        def error_message(tail):
            return self.error_message('raise {} {}'.format(
                expected.__name__, tail))

        try:
            self.actual()
        except expected as exc:
            exc_message = str(exc)

            if message is not None and message != exc_message:
                raise AssertionError(error_message('with message {} but was {}'.format(
                    repr(message), repr(exc_message))))
        except Exception as err:
            raise AssertionError(error_message('but {} raised'.format(type(err).__name__)))
        else:
            raise AssertionError(error_message('but {} raised'.format(None)))

    def error_message(self, tail):
        return self._parent.error_message('to {}'.format(tail))


class expect(object):
    def __init__(self, actual):
        self.actual = actual
        self.to = To(self)

    def error_message(self, tail):
        return 'Expected {} {}'.format(repr(self.actual), tail)
