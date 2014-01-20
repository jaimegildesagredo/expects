# -*- coding: utf-8 -*

from . import factory, plugins


expect = factory.ExpectFactory(plugins.load())
