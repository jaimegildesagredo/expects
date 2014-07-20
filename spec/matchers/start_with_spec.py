# -*- coding: utf-8 -*

from collections import OrderedDict

from mamba import describe, context, before

from expects import *
from expects.testing import failure

IRRELEVANT_ARGS = (1, 2)


with describe('start_with') as self:
    @before.each
    def fixtures():
        self.str = 'My foo string'
        self.lst = [1, 2, 3]
        self.dct = {'bar': 0, 'baz': 1}
        self.ordered_dct = OrderedDict([('bar', 0), ('baz', 1)])

    def it_should_pass_if_string_starts_with_string():
        expect(self.str).to(start_with(self.str[:5]))

    def it_should_pass_if_list_starts_with_arg():
        expect(self.lst).to(start_with(self.lst[0]))

    def it_should_pass_if_list_starts_with_args():
        expect(self.lst).to(start_with(*self.lst[:2]))

    def it_should_pass_if_ordered_dict_starts_with_keys():
        expected_args = list(self.ordered_dct)[:2]

        expect(self.ordered_dct).to(start_with(*expected_args))

    def it_should_pass_if_iter_starts_with_args():
        expect(iter(self.lst)).to(start_with(*self.lst[:2]))

    def it_should_fail_if_string_does_not_start_with_string():
        expected = self.str[5:]

        with failure('to start with {!r}'.format(expected)):
            expect(self.str).to(start_with(expected))

    def it_should_fail_if_list_does_not_start_with_arg():
        expected = self.lst[1]

        with failure('to start with {!r}'.format(expected)):
            expect(self.lst).to(start_with(expected))

    def it_should_fail_if_list_does_not_start_with_args():
        expected_args = self.lst[1:]

        with failure('to start with {!r} and {!r}'.format(*expected_args)):
            expect(self.lst).to(start_with(*expected_args))

    def it_should_fail_if_list_starts_with_first_arg_but_not_second():
        expected_args = self.lst[0], self.lst[0]

        with failure('to start with {!r} and {!r}'.format(*expected_args)):
            expect(self.lst).to(start_with(*expected_args))

    def it_should_fail_if_actual_is_a_dict():
        with failure('to start with {!r} and {!r} '
                     'but it does not have ordered keys'.format(*IRRELEVANT_ARGS)):

            expect(self.dct).to(start_with(*IRRELEVANT_ARGS))

    with context('#negated'):
        def it_should_pass_if_string_does_not_start_with_string():
            expect(self.str).not_to(start_with(self.str[5:]))

        def it_should_pass_if_list_does_not_start_with_args():
            expect(self.lst).not_to(start_with(*self.lst[2:]))

        def it_should_pass_if_list_starts_with_first_arg_but_not_second():
            expected_args = self.lst[0], self.lst[0]

            expect(self.lst).not_to(start_with(*expected_args))

        # TODO: Review this example
        #def it_should_fail_if_actual_is_a_dict_():
            #with failure('not to start with {!r} and {!r} '
                         #'but it does not have ordered keys'.format(*IRRELEVANT_ARGS)):

                #expect(self.dct).not_to(start_with(*IRRELEVANT_ARGS))
