# -*- coding: utf-8 -*-

from expects import *
from expects.testing import failure


with describe('failure'):
    with before.each:
        self.message = "to be 'bar'"
        self.pattern = "to be '\w+'"

    with it('should pass if assertion error raised'):
        with failure():
            raise AssertionError("Expected 'foo' {}".format(self.message))

    with it('should pass if assertion error raised and message matches'):
        with failure(self.message):
            raise AssertionError("Expected 'foo' {}".format(self.message))

    with it('should pass if assertion error raised and pattern matches'):
        with failure(self.pattern):
            raise AssertionError("Expected 'foo' {}".format(self.message))

    with it('should fail if assertion error not raised'):
        def callback():
            with failure(self.message):
                pass

        expect(callback).to(raise_error(AssertionError))

    with it('should fail if assertion error raised and message does not match'):
        def callback():
            with failure(self.message):
                raise AssertionError('foo')

        expect(callback).to(raise_error(AssertionError))

    with it('should fail if another exception raised'):
        def callback():
            with failure(self.message):
                raise KeyError()

        expect(callback).to(raise_error(AssertionError))
