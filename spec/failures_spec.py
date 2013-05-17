# -*- coding: utf-8 -*

from mamba import describe
from spec.helpers import failure

from expects import expect


with describe('expect failures') as _:
    def it_should_show_quoted_strings_on_failure():
        with failure('foo', "to be 'bar'"):
            expect('foo').to.be('bar')

    def it_should_show_object_repr_on_failure():
        obj1, obj2 = object(), object()

        with failure(obj1, "to be {}".format(obj2)):
            expect(obj1).to.be(obj2)
