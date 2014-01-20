# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.expectation import Expectation


with describe(Expectation) as _:
    with describe('#assert'):
        def it_should_pass_if_expectation_is_true():
            _.obj.to.be(True)

        def it_should_pass_if_expectation_is_true_and_negated_twice():
            _.obj.not_to.not_be(True)

        def it_should_pass_if_property_expectation_is_true():
            _.obj.true

        def it_should_pass_if_property_expectation_is_true_and_negated_twice():
            _.obj.not_to.not_true

        def it_should_fail_if_expectation_is_false():
            expect(lambda: _.obj.to.be(False)).to.raise_error(
                AssertionError, 'to be')

        def it_should_fail_if_expectation_is_true_and_negated():
            expect(lambda: _.obj.to.not_be(True)).to.raise_error(
                AssertionError, 'to not be')

        def it_should_fail_if_expectation_is_true_and_parent_negated():
            expect(lambda: _.obj.not_to.be(True)).to.raise_error(
                AssertionError, 'not to be')

        def it_should_fail_if_property_expectation_is_true_and_negated():
            expect(lambda: _.obj.not_true).to.raise_error(
                AssertionError, 'not true')

        with describe('#failure message'):
            def it_should_join_message_parts():
                expect(lambda: _.obj.to.be(False)).to.raise_error(
                    AssertionError, 'to be')

            def it_should_join_message_with_extra_message():
                def callback():
                    _.obj.to.be(False, 'extra')

                expect(callback).to.raise_error(
                    AssertionError, 'to be extra')

            def it_should_join_message_with_extra_messages():
                def callback():
                    _.obj.to.be(False, 'more', 'extra')

                expect(callback).to.raise_error(
                    AssertionError, 'to be more extra')

            def it_should_convert_to_str_non_str_message_parts():
                def callback():
                    _.obj.to.be(False, 'extra', True)

                expect(callback).to.raise_error(
                    AssertionError, 'to be extra True')

    with describe('#message'):
        def it_should_contain_public_attribute_names():
            _.obj.to.have

            expect(_.obj._message).to.equal(['to', 'have'])

        def it_should_split_underscore_in_attribute_name():
            _.obj.be_equal

            expect(_.obj._message).to.equal(['be', 'equal'])

        def it_should_contain_extra_message_if_assertion_fails():
            try:
                _.obj.be(False, 'extra')
            except AssertionError:
                pass

            expect(_.obj._message).to.equal(['be', 'extra'])

        def it_should_contain_extra_messages_if_assertion_fails():
            try:
                _.obj.be(False, 'more', 'extra')
            except AssertionError:
                pass

            expect(_.obj._message).to.equal(['be', 'more', 'extra'])

        def it_shouldnt_contain_extra_message_if_assertion_success():
            _.obj.be(True, 'extra')

            expect(_.obj._message).to.equal(['be'])

        def it_should_start_with_message_passed_to_constructor():
            _.obj = SUT(None, 'Expected')
            _.obj.to.have

            expect(_.obj._message).to.equal(['Expected', 'to', 'have'])

        def it_should_start_with_messages_passed_to_constructor():
            _.obj = SUT(None, 'Expected', None)
            _.obj.to.have

            expect(_.obj._message).to.equal(['Expected', None, 'to', 'have'])

        with context('#negated'):
            def it_should_start_with_not():
                _.obj.not_to.have

                expect(_.obj._message).to.equal(['not', 'to', 'have'])

            def it_should_have_a_not_in_the_proper_place():
                _.obj.to.not_have

                expect(_.obj._message).to.equal(['to', 'not', 'have'])

            def it_should_split_underscore_in_attribute_name_():
                _.obj.not_be_equal

                expect(_.obj._message).to.equal(['not', 'be', 'equal'])

    with describe('#not_attribute_prefix'):
        def it_should_return_attribute_without_not_prefix():
            expect(_.obj.not_to).to.be(_.obj.to)

        def it_should_raise_attribute_error_if_protected_attribute():
            expect(_.obj.to).to.have.property('_negated')

            expect(lambda: _.obj.to.not__negated).to.raise_error(
                AttributeError, 'not__negated')

        def it_should_raise_attribute_error_if_attribute_does_not_exists():
            expect(_.obj.to).not_to.have.property('negated')

            expect(lambda: _.obj.to.not_negated).to.raise_error(
                AttributeError, 'not_negated')

    @before.each
    def fixtures():
        _.obj = SUT(None)


class SUT(Expectation):
    @property
    def to(self):
        return self

    @property
    def have(self):
        return self

    def be(self, value, *message):
        self._assert(value, *message)

    def be_equal(self, value):
        self._assert(value)

    @property
    def true(self):
        self._assert(True)
