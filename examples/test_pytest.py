# -*- coding: utf-8 -*-

from expects import *


def test_failing():
    expect("foo").to(equal("bar"))
