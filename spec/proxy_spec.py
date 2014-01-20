# -*- coding: utf-8 -*

from mamba import describe, before

from spec.fixtures import Foo

from expects import expect
from expects.expectation import Proxy


with describe(Proxy) as _:
    def it_should_get_proxied_object_attribute():
        expect(_.proxy.bar).to.be(_.proxied.bar)

    def it_should_get_proxy_attribute_if_overridden():
        _.proxy.bar = _.proxied.bar +1

        expect(_.proxy.bar).not_to.be(_.proxied.bar)


    @before.each
    def fixtures():
        _.proxied = Foo()
        _.proxy = Proxy(_.proxied)
