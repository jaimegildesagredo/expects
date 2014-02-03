# -*- coding: utf-8 -*

from mamba import describe, context, before

from ..helpers import failure
from ..fixtures import Foo

from expects import expect


with describe('an') as _:
    def it_should_pass_if_actual_is_an_instance_of_the_expected_class_():
        expect(_.obj).to.be.an(object)

    def it_should_fail_if_actual_is_not_an_instance_of_the_expected_class_():
        class Object(object):
            pass

        with failure(_.obj, 'to be an Object instance'):
            expect(_.obj).to.be.an(Object)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_an_instance_of_the_expected_class_():
            class Object(object):
                pass

            expect(_.obj).not_to.be.an(Object)

        def it_should_fail_if_actual_is_an_instance_of_the_expected_class_():
            with failure(_.obj, 'not to be an object instance'):
                expect(_.obj).not_to.be.an(object)

    @before.each
    def fixtures():
        _.obj = Foo()
