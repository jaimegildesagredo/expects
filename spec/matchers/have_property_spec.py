# -*- coding: utf-8 -*-

from mamba import describe, context, before

from spec.fixtures import Foo

from expects import *
from expects.testing import failure


with describe('have_property') as _:
    def it_should_pass_if_object_has_property():
        expect(_.obj).to(have_property('bar'))

    def it_should_pass_if_object_has_property_with_value():
        expect(_.obj).to(have_property('bar', 0))

    def it_should_fail_if_object_does_not_have_property():
        with failure("to have property 'foo'"):
            expect(_.obj).to(have_property('foo'))

    def it_should_fail_if_object_hasnt_property_with_value():
        with failure("to have property 'foo' equal 0"):
            expect(_.obj).to(have_property('foo', 0))

    def it_should_fail_if_object_has_property_without_value():
        with failure("to have property 'bar' equal 1"):
            expect(_.obj).to(have_property('bar', 1))

    def it_should_fail_if_object_has_property_without_none_value():
        with failure("to have property 'bar' equal None"):
            expect(_.obj).to(have_property('bar', None))

    with context('#negated'):
        def it_should_pass_if_object_does_not_have_property():
            expect(_.obj).not_to(have_property('foo'))

        def it_should_pass_if_object_does_not_have_property_with_value():
            expect(_.obj).not_to(have_property('foo', 0))

        def it_should_pass_if_object_has_property_without_value():
            expect(_.obj).not_to(have_property('bar', 1))

        def it_should_fail_if_object_has_property():
            with failure("not to have property 'bar'"):
                expect(_.obj).not_to(have_property('bar'))

        def it_should_fail_if_object_has_property_with_value():
            with failure("not to have property 'bar' equal 0"):
                expect(_.obj).not_to(have_property('bar', 0))

    with context('#composition'):
        def it_should_pass_if_object_has_property_beloq_1():
            expect(_.obj).to(have_property('bar', be_below(1)))

        def it_should_fail_if_object_has_property_above_1():
            with failure("to have property 'bar' be above 1"):
                expect(_.obj).to(have_property('bar', be_above(1)))

    @before.each
    def fixtures():
        _.obj = Foo()
