# -*- coding: utf-8 -*

from mamba import describe, before

from expects import expect
from expects.expectations import Expectation


with describe(Expectation) as _:
    def it_should_return_class_if_accessed_from_class():
        expect(_.cls.expectation).to.be(Expectation)

    def it_should_return_instance_if_accesed_from_instance():
        expect(_.obj.expectation).to.be.an(Expectation)

    @before.all
    def fixtures():
        class Foo(object):
            expectation = Expectation

        _.cls = Foo
        _.obj = _.cls()
