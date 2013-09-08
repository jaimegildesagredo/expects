# -*- coding: utf-8 -*

from mamba import describe, before

from spec.fixtures import DefaultExpect, BarExpect

from expects import expect, ExpectFactory


with describe(ExpectFactory) as _:
    def it_should_raise_type_error_if_passed_arg_and_kwarg():
        expect(lambda: _.expect(1, foo=2)).to.raise_error(TypeError,
            "expect() got an unexpected keyword argument 'foo'")

    def it_should_raise_type_error_if_passed_multiple_kwargs():
        expect(lambda: _.expect(foo=1, bar=2)).to.raise_error(TypeError,
            'expect()')

    def it_should_raise_type_error_if_passed_multiple_args():
        expect(lambda: _.expect(1, 2)).to.raise_error(TypeError,
            'expect() takes 1 positional argument but 2 were given')

    def it_should_raise_type_error_if_no_arg_nor_kwarg_passed():
        expect(lambda: _.expect()).to.raise_error(TypeError,
            'expect() takes 1 required positional argument')

    def it_should_return_default_expectation_instance_if_passed_arg():
        result = _.expect(1)

        expect(result).to.be.a(DefaultExpect)
        expect(result).to.have.property('actual', 1)

    def it_should_return_given_expectation_instance_if_passed_kwarg():
        result = _.expect(bar=1)

        expect(result).to.be.a(BarExpect)
        expect(result).to.have.property('actual', 1)

    @before.each
    def subject():
        _.expect = ExpectFactory({
            'default': DefaultExpect,
            'bar': BarExpect
        })
