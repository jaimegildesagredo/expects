# -*- coding: utf-8 -*-

from mamba import describe, context, before

from spec.fixtures import Foo

from expects import expect
from expects.testing import failure


with describe('properties') as _:
    def it_should_pass_if_actual_has_properties_in_args():
        expect(_.obj).to.have.properties('bar', 'baz')

    def it_should_pass_if_actual_has_properties_in_kwargs():
        expect(_.obj).to.have.properties(bar=0, baz=1)

    def it_should_pass_if_actual_has_properties_in_args_and_kwargs():
        expect(_.obj).to.have.properties('bar', baz=1)

    def it_should_pass_if_actual_has_properties_in_dict():
        expect(_.obj).to.have.properties({'bar': 0, 'baz': 1})

    def it_should_fail_if_actual_does_not_have_property_in_args():
        with failure(_.obj, "to have property 'foo'"):
            expect(_.obj).to.have.properties('bar', 'foo')

    def it_should_fail_if_actual_does_not_have_property_in_kwargs():
        with failure(_.obj, "to have property 'foo'"):
            expect(_.obj).to.have.properties(bar=0, foo=1)

    def it_should_fail_if_actual_has_property_without_value_in_kwargs():
        with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
            expect(_.obj).to.have.properties(bar=1, baz=1)

    def it_should_fail_if_actual_does_not_have_property_in_args_but_in_kwargs():
        with failure(_.obj, "to have property 'foo'"):
            expect(_.obj).to.have.properties('foo', bar=0)

    def it_should_fail_if_actual_has_property_in_args_and_kwargs_without_value():
        with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
            expect(_.obj).to.have.properties('baz', bar=1)

    def it_should_fail_if_actual_has_property_without_value_in_dict():
        with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
            expect(_.obj).to.have.properties({'bar': 1, 'baz': 1})

    with context('#negated'):
        def it_should_pass_if_actual_does_not_have_properties_in_args():
            expect(_.obj).not_to.have.properties('foo', 'foobar')

        def it_should_pass_if_actual_does_not_have_properties_in_kwargs():
            expect(_.obj).not_to.have.properties(foo=0, foobar=1)

        def it_should_pass_if_actual_has_property_without_value_in_kwargs():
            expect(_.obj).not_to.have.properties(foo=0, bar=1)

        def it_should_pass_if_actual_does_not_have_properties_in_dict():
            expect(_.obj).not_to.have.properties({'foo': 0, 'foobar': 1})

        def it_should_pass_if_actual_has_property_without_value_in_dict():
            expect(_.obj).not_to.have.properties({'foo': 0, 'bar': 1})

        def it_should_fail_if_actual_has_property_in_args():
            with failure(_.obj, "not to have property 'bar'"):
                expect(_.obj).not_to.have.properties('foo', 'bar')

        def it_should_fail_if_actual_has_property_in_kwargs_with_value():
            with failure(_.obj, "not to have property 'bar' with value 0 but was 0"):
                expect(_.obj).not_to.have.properties(baz=0, bar=0)

        def it_should_fail_if_actual_has_property_in_args_but_not_in_kwargs():
            with failure(_.obj, "not to have property 'bar'"):
                expect(_.obj).not_to.have.properties('bar', baz=0)

        def it_should_fail_if_actual_has_property_in_kwargs_but_not_in_args():
            with failure(_.obj, "not to have property 'bar' with value 0 but was 0"):
                expect(_.obj).not_to.have.properties('foo', bar=0)

        def it_should_fail_if_actual_has_property_in_dict_with_value():
            with failure(_.obj, "not to have property 'bar' with value 0 but was 0"):
                expect(_.obj).not_to.have.properties({'bar': 0, 'foo': 1})

    @before.each
    def fixtures():
        _.obj = Foo()
