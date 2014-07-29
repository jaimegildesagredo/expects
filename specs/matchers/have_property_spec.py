# -*- coding: utf-8 -*-

from specs.fixtures import Foo

from expects import *
from expects.testing import failure


with describe('have_property'):
    with before.each:
        self.obj = Foo()

    with it('should_pass_if_object_has_property'):
        expect(self.obj).to(have_property('bar'))

    with it('should_pass_if_object_has_property_with_value'):
        expect(self.obj).to(have_property('bar', 0))

    with it('should_fail_if_object_does_not_have_property'):
        with failure("to have property 'foo'"):
            expect(self.obj).to(have_property('foo'))

    with it('should_fail_if_object_hasnt_property_with_value'):
        with failure("to have property 'foo' equal 0"):
            expect(self.obj).to(have_property('foo', 0))

    with it('should_fail_if_object_has_property_without_value'):
        with failure("to have property 'bar' equal 1"):
            expect(self.obj).to(have_property('bar', 1))

    with it('should_fail_if_object_has_property_without_none_value'):
        with failure("to have property 'bar' equal None"):
            expect(self.obj).to(have_property('bar', None))

    with context('#negated'):
        with it('should_pass_if_object_does_not_have_property'):
            expect(self.obj).not_to(have_property('foo'))

        with it('should_pass_if_object_does_not_have_property_with_value'):
            expect(self.obj).not_to(have_property('foo', 0))

        with it('should_pass_if_object_has_property_without_value'):
            expect(self.obj).not_to(have_property('bar', 1))

        with it('should_fail_if_object_has_property'):
            with failure("not to have property 'bar'"):
                expect(self.obj).not_to(have_property('bar'))

        with it('should_fail_if_object_has_property_with_value'):
            with failure("not to have property 'bar' equal 0"):
                expect(self.obj).not_to(have_property('bar', 0))

    with context('#composition'):
        with it('should_pass_if_object_has_property_below_1'):
            expect(self.obj).to(have_property('bar', be_below(1)))

        with it('should_fail_if_object_has_property_above_1'):
            with failure("to have property 'bar' be above 1"):
                expect(self.obj).to(have_property('bar', be_above(1)))
