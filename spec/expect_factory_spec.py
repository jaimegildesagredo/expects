# -*- coding: utf-8 -*

from mamba import describe, before

from expects import expect, errors, _compat
from expects.factory import ExpectFactory


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

    def it_should_return_default_plugin_instance_if_passed_arg():
        result = _.expect(1)

        expect(result).to.be.a(DefaultExpect)
        expect(result).to.have.property('actual', 1)

    def it_should_return_default_plugin_with_initial_message():
        result = _.expect(1)

        expect(result).to.have.property('message', ['Expected', repr(1)])

    def it_should_return_named_plugin_instance_if_passed_kwarg():
        result = _.expect(bar=1)

        expect(result).to.be.a(BarExpect)
        expect(result).to.have.property('actual', 1)

    def it_should_return_named_plugin_with_message_and_plugin_name():
        result = _.expect(bar=1)

        expect(result).to.have.property('actual', 1)
        expect(result).to.have.property('message',
                                        ['Expected', 'bar', repr(1)])

    def it_should_raise_if_named_plugin_is_not_found():
        expect(lambda: _.expect(foo=1)).to.raise_error(
            errors.PluginError, "Plugin 'foo' not found")

    def it_should_return_type_plugin_instance_if_passed_object_of_its_type():
        actual = object()

        instance = _.expect(actual)

        expect(instance).to.be.a(TypeExpect)
        expect(instance).to.have.property('actual', actual)
        expect(instance).to.have.property('message', ['Expected', repr(actual)])

    @before.each
    def subject():
        _.expect = ExpectFactory(
            named_plugins={
                'default': DefaultExpect,
                'bar': BarExpect
            },
            type_plugins={
                _plugin_id_for_object(): TypeExpect
            }
        )


def _plugin_id_for_object():
    package = '__builtin__' if _compat.IS_PY2 else 'builtin'

    return package + '.' + 'object'


class _Expect(object):
    def __init__(self, actual, *message):
        self.actual = actual
        self.message = list(message)


class DefaultExpect(_Expect):
    pass


class BarExpect(_Expect):
    pass


class TypeExpect(_Expect):
    pass
