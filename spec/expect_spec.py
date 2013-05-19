# -*- coding: utf-8 -*

from mamba import describe, before
from spec.helpers import failure

from expects import expect


with describe(expect) as _:
    with describe('to'):
        with describe('equal'):
            def it_should_pass_if_actual_equals_expected():
                expect(1).to.equal(1)

            def it_should_fail_if_actual_does_not_equal_expected():
                with failure(1, 'to equal 2'):
                    expect(1).to.equal(2)

        with describe('raise_error'):
            def it_should_pass_if_actual_raises_expected_exception():
                def callback():
                    raise AttributeError()

                expect(callback).to.raise_error(AttributeError)

            def it_should_fail_if_actual_does_not_raise_expected_exception():
                def callback():
                    raise KeyError()

                with failure(callback, 'to raise AttributeError but KeyError raised'):
                    expect(callback).to.raise_error(AttributeError)

            def it_should_fail_if_actual_does_not_raise_exception():
                callback = lambda: None

                with failure(callback, 'to raise AttributeError but None raised'):
                    expect(callback).to.raise_error(AttributeError)

            def it_should_pass_if_actual_raises_expected_exception_with_message():
                message = 'Foo error'

                def callback():
                    raise AttributeError(message)

                expect(callback).to.raise_error(AttributeError, message)

            def it_should_fail_if_actual_raises_expected_exception_with_different_message():
                def callback():
                    raise AttributeError('bar')

                with failure(callback, "to raise AttributeError with message 'foo' but was 'bar'"):
                    expect(callback).to.raise_error(AttributeError, 'foo')

        with describe('be'):
            def it_should_pass_if_actual_is_expected():
                value = 1
                expect(value).to.be(value)

            def it_should_fail_if_actual_is_not_expected():
                with failure(1, 'to be 2'):
                    expect(1).to.be(2)

            with describe('equal'):
                def it_should_pass_if_actual_equals_expected_():
                    expect(1).to.be.equal(1)

                def it_should_fail_if_actual_does_not_equal_expected_():
                    with failure(1, 'to be equal 2'):
                        expect(1).to.be.equal(2)

            with describe('true'):
                def it_should_pass_if_actual_is_true():
                    expect(True).to.be.true

                def it_should_fail_if_actual_is_false():
                    with failure(False, 'to be True'):
                        expect(False).to.be.true

            with describe('false'):
                def it_should_pass_if_actual_is_false():
                    expect(False).to.be.false

                def it_should_fail_if_actual_is_true():
                    with failure(True, 'to be False'):
                        expect(True).to.be.false

        with describe('have'):
            with describe('property'):
                @before.each
                def foo():
                    class Foo(object):
                        bar = 0

                    _.obj = Foo()

                def it_should_pass_if_actual_has_property():
                    expect(_.obj).to.have.property('bar')

                def it_should_fail_if_actual_does_not_have_property():
                    with failure(_.obj, "to have property 'foosplit'"):
                        expect(_.obj).to.have.property('foosplit')

                def it_should_pass_if_actual_has_property_with_value():
                    expect(_.obj).to.have.property('bar', 0)

                def it_should_fail_if_actual_has_property_without_value():
                    with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
                        expect(_.obj).to.have.property('bar', 1)

                def it_should_fail_if_actual_property_is_not_none():
                    with failure(_.obj, "to have property 'bar' with value None but was 0"):
                        expect(_.obj).to.have.property('bar', None)


    with describe('not_to'):
        with describe('equal'):
            def it_should_pass_if_actual_does_not_equal_expected():
                expect(1).not_to.equal(2)

            def it_should_fail_if_actual_equals_expected():
                with failure(1, 'not to equal 1'):
                    expect(1).not_to.equal(1)

        with describe('be'):
            def it_should_pass_if_actual_is_not_expected():
                expect(1).not_to.be(2)

            def it_should_fail_if_actual_is_expected():
                value = 1

                with failure(1, 'not to be 1'):
                    expect(value).not_to.be(value)

            with describe('equal'):
                def it_should_pass_if_actual_does_not_equal_expected_():
                    expect(1).not_to.be.equal(2)

                def it_should_fail_if_actual_equals_expected_():
                    with failure(1, 'not to be equal 1'):
                        expect(1).not_to.be.equal(1)
