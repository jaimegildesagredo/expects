# -*- coding: utf-8 -*

from . import factory, plugins


expect = factory.ExpectFactory(
    named_plugins=plugins.load_named(),
    type_plugins=plugins.load_typed())
