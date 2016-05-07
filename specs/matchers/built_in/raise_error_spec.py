# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure

UNICODE_VALUE = u'an unicode value'
UNICODE_PATTERN = u'unicode'


with describe('raise_error'):
    with before.each:
        self.message = 'Foo error'

    with it('passes if callable raises any exception'):
        def callback():
            raise AttributeError()

        expect(callback).to(raise_error)

    with it('passes if callable raises expected exception'):
        def callback():
            raise AttributeError()

        expect(callback).to(raise_error(AttributeError))

    with it('passes if callable raises with message'):
        def callback():
            raise AttributeError(self.message)

        expect(callback).to(raise_error(AttributeError, self.message))

    with it('passes if callable raises with non string value'):
        def callback():
            raise AttributeError(1)

        expect(callback).to(raise_error(AttributeError, 1))

    with it('fails if callable does not raise any exception'):
        def callback():
            pass

        with failure('but: no exception raised'):
            expect(callback).to(raise_error)

    with it('fails if callable does not raise expected exception'):
        def callback():
            raise KeyError()

        with failure(contain('but: KeyError raised')):
            expect(callback).to(raise_error(AttributeError))

    with it('fails if callable does not raise exception'):
        with failure('but: no exception raised'):
            expect(lambda: None).to(raise_error(AttributeError))

    with it('fails if callable raises with different message'):
        def callback():
            raise AttributeError('bar')

        with failure("but: AttributeError raised with 'bar'"):
            expect(callback).to(raise_error(AttributeError, 'foo'))

    with it('fails if callable does not raise with none'):
        def callback():
            raise AttributeError('foo')

        with failure("but: AttributeError raised with 'foo'"):
            expect(callback).to(raise_error(AttributeError, None))

    with it('fails if callable does not raise with non string value'):
        def callback():
            raise AttributeError('foo')

        with failure("but: AttributeError raised with 'foo'"):
            expect(callback).to(raise_error(AttributeError, 1))

    with context('when negated'):
        with it('passes if callable does not raise expected exception'):
            def callback():
                raise AttributeError()

            expect(callback).not_to(raise_error(KeyError))

        with it('passes if callable does not raise exception'):
            expect(lambda: None).not_to(raise_error(AttributeError))

        with it('passes if callable raises expected exception with different message'):
            def callback():
                raise AttributeError('bar')

            expect(callback).not_to(raise_error(AttributeError, 'foo'))

        with it('fails if callable raises expected exception'):
            def callback():
                raise AttributeError()

            with failure('but: AttributeError raised'):
                expect(callback).not_to(raise_error(AttributeError))

        with it('fails if callable raises expected exception with message'):
            def callback():
                raise AttributeError('foo')

            with failure("but: AttributeError raised with 'foo'"):
                expect(callback).not_to(raise_error(AttributeError, 'foo'))

    with context('when combined'):
        with it('passes if callable raises exception and message matches'):
            def callback():
                raise AttributeError(self.message)

            expect(callback).to(raise_error(AttributeError, match(r'Foo \w+')))

        with it('fails if callable raises but message does not match'):
            def callback():
                raise AttributeError('foo')

            with failure("but: AttributeError raised with 'foo'"):
                expect(callback).to(raise_error(AttributeError, match(r'\d+')))
