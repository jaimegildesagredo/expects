# -*- coding: utf-8 -*

from pkg_resources import iter_entry_points


def load_named():
    return {e.name: e.load() for e in
            iter_entry_points('expects.plugins')}


def load_typed():
    return {e.name: e.load() for e in
            iter_entry_points('expects.type_plugins')}
