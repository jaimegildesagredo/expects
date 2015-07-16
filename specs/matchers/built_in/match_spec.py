# -*- coding: utf-8 -*

import re

from expects import *
from expects.testing import failure


with describe('match'):
    with before.all:
        self.str = 'My foo string'

    with it('passes if string matches expected regexp'):
        expect(self.str).to(match(r'My \w+ string'))

    with it('passes if part of the string matches expected regexp'):
        expect(self.str).to(match(r'\w+ string'))

    with it('passes if string matches expected regexp with re flags'):
        expect(self.str).to(match(r'my [A-Z]+ strinG', re.I))

    with it('fails if string does not match expected regexp'):
        with failure("to match 'My \\\\W+ string'"):
            expect(self.str).to(match(r'My \W+ string'))

    with context('when negated'):
        with it('passes if string does not match expected regexp'):
            expect(self.str).not_to(match(r'My \W+ string'))

        with it('passes if string does not match expected regexp with re flags'):
            expect(self.str).not_to(match(r'My \W+ string', re.I))

        with it('fails if string matches expected regexp'):
            with failure("not to match 'My \\\\w+ string'"):
                expect(self.str).not_to(match(r'My \w+ string'))
