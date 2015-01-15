# -*- coding: utf-8 -*

from expects import *
from expects.aliases import *
from expects.testing import failure


with describe('have_key'):
    with before.all:
        self.dct = {'bar': 0, 'baz': 1}
        self.str = 'My foo string'

    with it('should pass if actual has expected key'):
        expect(self.dct).to(have_key('bar'))

    with it('should pass if actual has key and value'):
        expect(self.dct).to(have_key('bar', 0))

    with it('should fail if actual does not have expected key'):
        with failure("to have key 'foo'"):
            expect(self.dct).to(have_key('foo'))

    with it('should fail if actual does not have key with value'):
        with failure("to have key 'foo' equal 0"):
            expect(self.dct).to(have_key('foo', 0))

    with it('should fail if actual has key without expected value'):
        with failure("to have key 'bar' equal 1"):
            expect(self.dct).to(have_key('bar', 1))

    with it('should fail if actual has key without none value'):
        with failure("to have key 'bar' equal None"):
            expect(self.dct).to(have_key('bar', None))

    with it('should fail if actual is not a dict'):
        # issue-10

        with failure("to have key 'foo' equal 0 but is not a dict"):
            expect(self.str).to(have_key('foo', 0))

    with context('#negated'):
        with it('should pass if actual does not have expected key'):
            expect(self.dct).not_to(have_key('foo'))

        with it('should pass if actual does not have expected key with value'):
            expect(self.dct).not_to(have_key('foo', 0))

        with it('should pass if actual has expected key without value'):
            expect(self.dct).not_to(have_key('bar', 1))

        with it('should fail if actual has expected key'):
            with failure("not to have key 'bar'"):
                expect(self.dct).not_to(have_key('bar'))

        with it('should fail if actual has expected key with value'):
            with failure("not to have key 'bar' equal 0"):
                expect(self.dct).not_to(have_key('bar', 0))

        with it('should fail if actual is not a dict'):
            # issue-10

            with failure("not to have key 'foo' equal 0 but is not a dict"):
                expect(self.str).not_to(have_key('foo', 0))

    with context('#composed'):
        with it('should pass if actual has key below 1'):
            expect(self.dct).to(have_key('bar', be_below(1)))

        with it('should fail if actual does not have key above 1'):
            with failure("to have key 'bar' above 1"):
                expect(self.dct).to(have_key('bar', above(1)))
