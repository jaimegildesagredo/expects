# -*- coding: utf-8 -*

from mamba import describe, context, before

from spec.fixtures import Foo

from expects import expect
from expects.testing import failure


with describe('a') as _:
    def it_should_pass_if_object_is_an_instance_of_the_expected_class():
        expect(_.obj).to.be(a(Foo))

    def it_should_pass_if_object_is_a_subclass_instance_of_the_expected_class():
        expect(_.obj).to.be(a(object))

    def it_should_fail_if_object_is_not_an_instance_of_the_expected_class():
        class Bar(object):
            pass

        with failure(''):
            expect(_.obj).to.be(a(Bar))

    with context('#negated'):
        def it_should_pass_if_object_is_not_an_instance_of_the_expected_class():
            class Bar(object):
                pass

            expect(_.obj).not_to.be(a(Bar))

        def it_should_fail_if_object_is_a_subclass_instance_of_the_expected_class():
            with failure(''):
                expect(_.obj).not_to.be(a(object))

        def it_should_fail_if_object_is_an_instance_of_the_expected_class():
            with failure(''):
                expect(_.obj).not_to.be(a(Foo))

    @before.each
    def fixtures():
        _.obj = Foo()
