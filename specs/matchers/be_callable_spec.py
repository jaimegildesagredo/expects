# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_callable'):
    with it('passes if subject is callable'):
        expect(lambda: None).to(be_callable)

    with it('fails if subject is not callable'):
        with failure:
            expect('foo').to(be_callable)
