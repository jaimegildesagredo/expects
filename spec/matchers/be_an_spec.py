# -*- coding: utf-8 -*

from mamba import describe, context, before

from spec.fixtures import Foo

from expects import expect
from expects.matchers import *
from expects.testing import failure


with describe('be_an') as _:
    def it_should_pass_if_object_is_an_instance_of_the_expected_class_():
        expect(_.obj).to(be_an(object))

    def it_should_fail_if_object_is_not_an_instance_of_the_expected_class_():
        class Object(object):
            pass

        with failure('to be an instance of Object'):
            expect(_.obj).to(be_an(Object))

    with context('#negated'):
        def it_should_pass_if_object_is_not_an_instance_of_the_expected_class_():
            class Object(object):
                pass

            expect(_.obj).not_to(be_an(Object))

        def it_should_fail_if_object_is_an_instance_of_the_expected_class_():
            with failure('not to be an instance of object'):
                expect(_.obj).not_to(be_an(object))

    @before.each
    def fixtures():
        _.obj = Foo()
