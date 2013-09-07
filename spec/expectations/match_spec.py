# -*- coding: utf-8 -*

import re

from mamba import describe, context, before

from spec.helpers import failure

from expects import expect


with describe('to.match') as _:
    def it_should_pass_if_actual_matches_expected_regexp():
        expect(_.str).to.match(r'My \w+ string')

    def it_should_pass_if_actual_matches_expected_regexp_with_re_flags():
        expect(_.str).to.match(r'my [A-Z]+ strinG', re.I)

    def it_should_fail_if_actual_does_not_match_expected_regexp():
        pattern = r'My \W+ string'

        with failure(_.str, 'to match {}'.format(repr(pattern))):
            expect(_.str).to.match(pattern)

    with context('#negated'):
        def it_should_pass_if_actual_does_not_match_expected_regexp():
            expect(_.str).not_to.match(r'My \W+ string')

        def it_should_pass_if_actual_does_not_match_expected_regexp_with_re_flags():
            expect(_.str).not_to.match(r'My \W+ string', re.I)

        def it_should_fail_if_actual_matches_expected_regexp():
            pattern = r'My \w+ string'

            with failure(_.str, 'not to match {}'.format(repr(pattern))):
                expect(_.str).not_to.match(pattern)

    @before.all
    def fixtures():
        _.str = 'My foo string'
