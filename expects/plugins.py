# -*- coding: utf-8 -*

from pkg_resources import iter_entry_points


def load_matchers():
    return {e.name: e.load() for e in iter_entry_points('expects.matchers')}
