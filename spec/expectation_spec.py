# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.expects import Expectation, Negable


with describe(Expectation) as _:
    with context('#descriptor'):
        def it_should_return_class_if_accessed_from_class():
            expect(_.cls.to).to.be.a(type(Expectation))

        def it_should_return_instance_if_accesed_from_instance():
            expect(_.obj.to).to.be.an(Expectation)

    with context('#assert'):
        def it_should_pass_if_expectation_is_true():
            _.obj.to.have(True)

        def it_should_pass_if_expectation_is_true_and_negated_twice():
            _.obj.not_to.not_have(True)

        def it_should_fail_if_expectation_is_true_and_negated():
            expect(lambda: _.obj.to.not_have(True)).to.raise_error(
                AssertionError)

        def it_should_fail_if_expectation_is_true_and_parent_negated():
            expect(lambda: _.obj.not_to.have(True)).to.raise_error(
                AssertionError)

    with context('#error_message'):
        def it_should_be_expectation_name_lowercase():
            expectation = _.obj.to.have

            expect(expectation.error_message).to.equal(
                'Expected [...] to have ')

        with context('#negated'):
            def it_should_start_with_not():
                expectation = _.obj.not_to.have

                expect(expectation.error_message).to.equal(
                   'Expected [...] not to have ')

            def it_should_have_a_not_in_the_proper_place():
                expectation = _.obj.to.not_have

                expect(expectation.error_message).to.equal(
                   'Expected [...] to not have ')

    with context('#not_prefix'):
        def it_should_raise_attribute_error_if_not_an_expectation():
            expect(lambda: _.obj.to.not_negated).to.raise_error(
                AttributeError, 'not_negated')

        def it_should_raise_attribute_error_if_attribute_does_not_exists():
            expect(lambda: _.obj.to.not_foo).to.raise_error(
                AttributeError, 'not_foo')

    @before.each
    def fixtures():
        class Foo(Negable):
            error_message = 'Expected [...] '

            class to(Expectation):
                class have(Expectation):
                    def __call__(self, expected):
                        self._expect_value(expected)

                    def _expect_value(self, value):
                            self._assert(value, '')

        _.cls = Foo
        _.obj = _.cls()
