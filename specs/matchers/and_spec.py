# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('matcher & matcher'):
    with it('passes if both matchers match'):
        expect(True).to(be_true & be_true)

    with it('fails if one matcher does not match'):
        with failure(contain(' and ')):
            expect(1).to(be_above(0) & equal(2))
