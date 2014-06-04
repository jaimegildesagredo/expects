# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.testing import failure


with describe('end_with') as self:
    @before.each
    def fixtures():
        self.str = 'My foo string'

    def it_should_pass_if_actual_ends_with_string():
        expect(self.str).to.end_with(self.str[5:])

    def it_should_fail_if_actual_does_not_end_with_string():
        expected = self.str[:5]

        with failure(self.str, 'to end with {!r}'.format(expected)):
            expect(self.str).to.end_with(expected)

    with context('#negated'):
        def it_should_pass_if_actual_does_not_end_with_string():
            expect(self.str).to.not_end_with(self.str[:5])
