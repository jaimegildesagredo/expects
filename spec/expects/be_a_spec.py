# -*- coding: utf-8 -*

from mamba import describe, context, before

from spec.helpers import failure
from spec.fixtures import Foo

from expects import expect


with describe('to.be') as _:
    with describe('a'):
        def it_should_pass_if_actual_is_an_instance_of_the_expected_class():
            expect(_.obj).to.be.a(Foo)

        def it_should_pass_if_actual_is_a_subclass_instance_of_the_expected_class():
            expect(_.obj).to.be.a(object)

        def it_should_fail_if_actual_is_not_an_instance_of_the_expected_class():
            class Bar(object):
                pass

            with failure(_.obj, 'to be a Bar instance'):
                expect(_.obj).to.be.a(Bar)

    with describe('an'):
        def it_should_pass_if_actual_is_an_instance_of_the_expected_class_():
            expect(_.obj).to.be.an(object)

        def it_should_fail_if_actual_is_not_an_instance_of_the_expected_class_():
            class Object(object):
                pass

            with failure(_.obj, 'to be an Object instance'):
                expect(_.obj).to.be.an(Object)

    with context('#negated'):
        with describe('a'):
            def it_should_pass_if_actual_is_not_an_instance_of_the_expected_class():
                class Bar(object):
                    pass

                expect(_.obj).not_to.be.a(Bar)

            def it_should_fail_if_actual_is_a_subclass_instance_of_the_expected_class():
                with failure(_.obj, 'not to be a object instance'):
                    expect(_.obj).not_to.be.a(object)

            def it_should_fail_if_actual_is_an_instance_of_the_expected_class():
                with failure(_.obj, 'not to be a Foo instance'):
                    expect(_.obj).not_to.be.a(Foo)

        with describe('an'):
            def it_should_pass_if_actual_is_not_an_instance_of_the_expected_class_():
                class Object(object):
                    pass

                expect(_.obj).not_to.be.an(Object)

            def it_should_fail_if_actual_is_an_instance_of_the_expected_class_():
                with failure(_.obj, 'not to be an object instance'):
                    expect(_.obj).not_to.be.an(object)

    @before.all
    def fixtures():
        _.obj = Foo()
