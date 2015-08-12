# -*- coding: utf-8 -*-

from expects import *
from expects.testing import failure


with describe('failure'):
    with context('without message'):
        with it('passes if assertion error raised'):
            with failure:
                raise AssertionError()

        with it('fails if assertion error not raised'):
            def callback():
                with failure:
                    pass

            expect(callback).to(raise_error(AssertionError))

        with it('fails if another exception raised'):
            def callback():
                with failure:
                    raise KeyError()

            expect(callback).to(raise_error(AssertionError))

    with context('with message'):
        with before.each:
            self.message = "to be 'bar'"
            self.pattern = "to be '\w+'"

        with it('passes if assertion raised and message ends with'):
            with failure(self.message):
                raise AssertionError("Expected 'foo' {0}".format(self.message))

        with it('passes if assertion error raised and message matches'):
            with failure(match(self.pattern)):
                raise AssertionError("Expected 'foo' {0}".format(self.message))

        with it('passes if assertion error raised and message has length 0'):
            with failure(have_length(0)):
                raise AssertionError('')

        with it('fails if assertion error not raised'):
            def callback():
                with failure(self.message):
                    pass

            expect(callback).to(raise_error(AssertionError))

        with it('fails if assertion error raised and message does not match'):
            def callback():
                with failure(self.message):
                    raise AssertionError('foo')

            expect(callback).to(raise_error(AssertionError))

        with it('fails if another exception raised'):
            def callback():
                with failure(self.message):
                    raise KeyError()

            expect(callback).to(raise_error(AssertionError))

        with it('fails if assertion error raised but message has not length 0'):
            def callback():
                with failure(have_length(0)):
                    raise AssertionError('foo')

            expect(callback).to(raise_error(AssertionError, contain('have length 0')))
