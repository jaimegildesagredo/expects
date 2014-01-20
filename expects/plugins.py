# -*- coding: utf-8 -*

from pkg_resources import iter_entry_points


def load():
    return {e.name: e.load() for e in
            iter_entry_points('expects.plugins')}
