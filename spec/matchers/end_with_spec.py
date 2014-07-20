# -*- coding: utf-8 -*

from collections import OrderedDict

from mamba import describe, context, before

from expects import expect
from expects.matchers import *
from expects.testing import failure

IRRELEVANT_ARGS = (1, 2)


with describe('end_with') as self:
    @before.each
    def fixtures():
        self.str = 'My foo string'
        self.lst = [1, 2, 3]
        self.dct = {'bar': 0, 'baz': 1}
        self.ordered_dct = OrderedDict([('bar', 0), ('baz', 1)])

    def it_should_pass_if_string_ends_with_string():
        expect(self.str).to(end_with(self.str[5:]))

    def it_should_pass_if_list_ends_with_arg():
        expect(self.lst).to(end_with(self.lst[-1]))

    def it_should_pass_if_list_ends_with_args():
        expect(self.lst).to(end_with(*reversed(self.lst[-2:])))

    def it_should_pass_if_ordered_dict_ends_with_keys():
        expected_args = reversed(list(self.ordered_dct)[:2])

        expect(self.ordered_dct).to(end_with(*expected_args))

    def it_should_fail_if_string_does_not_end_with_string():
        expected = self.str[:5]

        with failure('to end with {!r}'.format(expected)):
            expect(self.str).to(end_with(expected))

    def it_should_fail_if_list_ends_with_first_arg_but_not_second():
        expected_args = self.lst[-1], self.lst[-1]

        with failure('to end with {!r} and {!r}'.format(*expected_args)):
            expect(self.lst).to(end_with(*expected_args))

    def it_should_fail_if_subject_is_a_dict():
        with failure('to end with {!r} and {!r} '
                     'but it does not have ordered keys'.format(*IRRELEVANT_ARGS)):

            expect(self.dct).to(end_with(*IRRELEVANT_ARGS))

    with context('#negated'):
        def it_should_pass_if_string_does_not_end_with_string():
            expect(self.str).not_to(end_with(self.str[:5]))

        def it_should_pass_if_list_does_not_end_with_args():
            expect(self.lst).not_to(end_with(*self.lst[:2]))

        def it_should_pass_if_list_ends_with_first_arg_but_not_second():
            expected_args = self.lst[-1], self.lst[-1]

            expect(self.lst).not_to(end_with(*expected_args))

        # TODO: Review this example
        #def it_should_fail_if_subject_is_a_dict_():
            #with failure('not to end with {!r} and {!r} '
                         #'but it does not have ordered keys'.format(*IRRELEVANT_ARGS)):

                #expect(self.dct).not_to(end_with(*IRRELEVANT_ARGS))
