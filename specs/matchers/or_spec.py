# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('matcher | matcher'):
    with it('passes if both matchers match'):
        expect(True).to(be_true | be_true)

    with it('passes if one matcher does not match'):
        expect(True).to(be_false | be_true)

    with it('fails if both matchers do not match'):
        with failure('be below 0 or equal 2'):
            expect(1).to(be_below(0) | equal(2))

with describe('matcher | matcher | matcher'):
    with it('passes if all matchers match'):
        expect(True).to(be_true | be_true | be_true)

    with it('passes if one matcher matchs'):
        expect(True).to(be_false | be_false | be_true)

    with it('fails if all matchers do not match'):
        with failure('be below 0, equal 2 or be a str'):
            expect(1).to(be_below(0) |
                         equal(2) |
                         be_a(str))
