# -*- coding: utf-8 -*

import re

from mamba import describe, context, before

from expects import expect
from expects.matchers import *
from expects.testing import failure


with describe('match') as _:
    def it_should_pass_if_string_matches_expected_regexp():
        expect(_.str).to(match(r'My \w+ string'))

    def it_should_pass_if_string_matches_expected_regexp_with_re_flags():
        expect(_.str).to(match(r'my [A-Z]+ strinG', re.I))

    def it_should_fail_if_string_does_not_match_expected_regexp():
        with failure("to match 'My \\\\W+ string'"):
            expect(_.str).to(match(r'My \W+ string'))

    with context('#negated'):
        def it_should_pass_if_string_does_not_match_expected_regexp():
            expect(_.str).not_to(match(r'My \W+ string'))

        def it_should_pass_if_string_does_not_match_expected_regexp_with_re_flags():
            expect(_.str).not_to(match(r'My \W+ string', re.I))

        def it_should_fail_if_string_matches_expected_regexp():
            with failure("not to match 'My \\\\w+ string'"):
                expect(_.str).not_to(match(r'My \w+ string'))

    @before.all
    def fixtures():
        _.str = 'My foo string'
