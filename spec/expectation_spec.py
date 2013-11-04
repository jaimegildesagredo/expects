# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.expects import Expectation


with describe(Expectation) as _:
    # TODO: Check the context name
    with context('#descriptor'):
        def it_should_return_class_if_accessed_from_class():
            expect(_.cls.expectation).to.be(Expectation)

        def it_should_return_instance_if_accesed_from_instance():
            expect(_.obj.expectation).to.be.an(Expectation)

    with context('#error_message'):
        def it_should_be_expectation_name_lowercase():
            expectation = _.obj.expectation

            expect(expectation.error_message).to.equal(
                'Expected [...] expectation ')

    @before.all
    def fixtures():
        class Foo(object):
            error_message = 'Expected [...] '
            expectation = Expectation

        _.cls = Foo
        _.obj = _.cls()
