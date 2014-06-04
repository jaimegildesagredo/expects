# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.testing import failure


with describe('start_with') as self:
    @before.each
    def fixtures():
        self.str = 'My foo string'

    def it_should_pass_if_actual_starts_with_string():
        expect(self.str).to.start_with(self.str[:5])

    def it_should_fail_if_actual_does_not_start_with_string():
        expected = self.str[5:]

        with failure(self.str, 'to start with {!r}'.format(expected)):
            expect(self.str).to.start_with(expected)

    with context('#negated'):
        def it_should_pass_if_actual_does_not_start_with_string():
            expect(self.str).to.not_start_with(self.str[5:])
