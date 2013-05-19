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

    @property
    def negative(self):
        return self._parent.negative

    def _assert(self, result, error_message):
        assert not result if self.negative else result, error_message


class Equal(Expectation):
    def __call__(self, expected):
        self._assert(self.actual == expected, self.error_message(repr(expected)))

    def error_message(self, tail):
        return self._parent.error_message('equal {}'.format(tail))


class Be(Expectation):
    def init(self):
        self.equal = Equal(self)

    def __call__(self, expected):
        self._assert(self.actual is expected, self.error_message(repr(expected)))

    @property
    def true(self):
        self(True)

    @property
    def false(self):
        self(False)

    def error_message(self, tail):
        return self._parent.error_message('be {}'.format(tail))


class Have(Expectation):
    def property(self, *args):
        name = args[0]

        def error_message(tail):
            return self.error_message('property {}'.format(tail))

        self._assert(hasattr(self.actual, name), error_message(repr(name)))

        try:
            expected = args[1]
        except IndexError:
            pass
        else:
            value = getattr(self.actual, name)

            self._assert(value == expected, error_message('{} with value {} but was {}'.format(
                repr(name), repr(expected), repr(value))))

    def error_message(self, tail):
        return self._parent.error_message('have {}'.format(tail))


class RaiseError(Expectation):
    def __call__(self, expected, message=None):
        assertion = self._build_assertion(expected, message)

        if assertion is not None:
            self._assert(*assertion)

    def _build_assertion(self, expected, message):
        def error_message(tail):
            return self.error_message('{} {}'.format(
                expected.__name__, tail))

        try:
            self.actual()
        except expected as exc:
            exc_message = str(exc)

            if message is not None:
                return message == exc_message, error_message(
                    'with message {} but message was {}'.format(repr(message), repr(exc_message)))
            else:
                return True, error_message('but {} raised'.format(type(exc).__name__))
        except Exception as err:
            return False, error_message('but {} raised'.format(type(err).__name__))
        else:
            return False, error_message('but {} raised'.format(None))

    def error_message(self, tail):
        return self._parent.error_message('raise {}'.format(tail))


class To(Expectation):
    def init(self):
        self.be = Be(self)
        self.have = Have(self)
        self.equal = Equal(self)
        self.raise_error = RaiseError(self)

    def error_message(self, tail):
        message = 'not to' if self.negative else 'to'

        return self._parent.error_message('{} {}'.format(message, tail))
