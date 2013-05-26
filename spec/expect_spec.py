# -*- coding: utf-8 -*

import re

from mamba import describe, before
from spec.helpers import failure
from spec.fixtures import Foo

from expects import expect


with describe(expect) as _:
    with describe('to'):
        with describe('equal'):
            def it_should_pass_if_actual_equals_expected():
                expect(1).to.equal(1)

            def it_should_fail_if_actual_does_not_equal_expected():
                with failure(1, 'to equal 2'):
                    expect(1).to.equal(2)

        with describe('match'):
            def it_should_pass_if_actual_matches_expected_regexp():
                expect(_.str).to.match(r'My \w+ string')

            def it_should_pass_if_actual_matches_expected_regexp_with_re_flags():
                expect(_.str).to.match(r'my [A-Z]+ strinG', re.I)

            def it_should_fail_if_actual_does_not_match_expected_regexp():
                pattern = r'My \W+ string'

                with failure(_.str, 'to match {}'.format(repr(pattern))):
                    expect(_.str).to.match(pattern)

        with describe('raise_error'):
            def it_should_pass_if_actual_raises_expected_exception():
                def callback():
                    raise AttributeError()

                expect(callback).to.raise_error(AttributeError)

            def it_should_fail_if_actual_does_not_raise_expected_exception():
                def callback():
                    raise KeyError()

                with failure(callback, 'to raise AttributeError but KeyError raised'):
                    expect(callback).to.raise_error(AttributeError)

            def it_should_fail_if_actual_does_not_raise_exception():
                callback = lambda: None

                with failure(callback, 'to raise AttributeError but None raised'):
                    expect(callback).to.raise_error(AttributeError)

            def it_should_pass_if_actual_raises_expected_exception_with_message():
                message = 'Foo error'

                def callback():
                    raise AttributeError(message)

                expect(callback).to.raise_error(AttributeError, message)

            def it_should_fail_if_actual_raises_expected_exception_with_different_message():
                def callback():
                    raise AttributeError('bar')

                with failure(callback, "to raise AttributeError with message 'foo' but message was 'bar'"):
                    expect(callback).to.raise_error(AttributeError, 'foo')

        with describe('be'):
            def it_should_pass_if_actual_is_expected():
                value = 1
                expect(value).to.be(value)

            def it_should_fail_if_actual_is_not_expected():
                with failure(1, 'to be 2'):
                    expect(1).to.be(2)

            with describe('equal'):
                def it_should_pass_if_actual_equals_expected_():
                    expect(1).to.be.equal(1)

                def it_should_fail_if_actual_does_not_equal_expected_():
                    with failure(1, 'to be equal 2'):
                        expect(1).to.be.equal(2)

            with describe('a'):
                def it_should_pass_if_actual_is_an_instance_of_the_expected_class():
                    expect(_.obj).to.be.a(Foo)

                def it_should_pass_if_actual_is_a_subclass_instance_of_the_expected_class():
                    expect(_.obj).to.be.a(object)

                def it_should_fail_if_actual_is_not_an_instance_of_the_expected_class():
                    class Bar(object):
                        pass

                    with failure(_.obj, 'to be a Bar instance'):
                        expect(_.obj).to.be.a(Bar)

            with describe('an'):
                def it_should_pass_if_actual_is_an_instance_of_the_expected_class_():
                    expect(_.obj).to.be.an(object)

                def it_should_fail_if_actual_is_not_an_instance_of_the_expected_class_():
                    class Object(object):
                        pass

                    with failure(_.obj, 'to be an Object instance'):
                        expect(_.obj).to.be.an(Object)

            with describe('greater_than'):
                def it_should_pass_if_actual_is_greater_than_expected():
                    expect(5).to.be.greater_than(4)

                def it_should_fail_if_actual_is_not_greater_than_expected():
                    with failure(1, 'to be greater than 4'):
                        expect(1).to.be.greater_than(4)

            with describe('greater_or_equal_to'):
                def it_should_pass_if_actual_is_greater_than_expected_():
                    expect(5).to.be.greater_or_equal_to(4)

                def it_should_pass_if_actual_is_equal_to_expected():
                    expect(5).to.be.greater_or_equal_to(5)

                def it_should_fail_if_actual_is_not_greater_or_equal_to_expected():
                    with failure(1, 'to be greater or equal to 4'):
                        expect(1).to.be.greater_or_equal_to(4)

            with describe('less_than'):
                def it_should_pass_if_actual_is_less_than_expected():
                    expect(1).to.be.less_than(4)

                def it_should_fail_if_actual_is_not_less_than_expected():
                    with failure(4, 'to be less than 1'):
                        expect(4).to.be.less_than(1)

            with describe('less_or_equal_to'):
                def it_should_pass_if_actual_is_less_than_expected_():
                    expect(1).to.be.less_or_equal_to(4)

                def it_should_pass_if_actual_is_equal_to_expected_():
                    expect(5).to.be.less_or_equal_to(5)

                def it_should_fail_if_actual_is_not_less_or_equal_to_expected():
                    with failure(4, 'to be less or equal to 1'):
                        expect(4).to.be.less_or_equal_to(1)

            with describe('within'):
                def it_should_pass_if_actual_is_within_expected_range():
                    expect(5).to.be.within(4, 7)

                def it_should_fail_if_actual_is_not_within_expected_range():
                    with failure(1, 'to be within 4, 7'):
                        expect(1).to.be.within(4, 7)

            with describe('true'):
                def it_should_pass_if_actual_is_true():
                    expect(True).to.be.true

                def it_should_fail_if_actual_is_false():
                    with failure(False, 'to be True'):
                        expect(False).to.be.true

            with describe('false'):
                def it_should_pass_if_actual_is_false():
                    expect(False).to.be.false

                def it_should_fail_if_actual_is_true():
                    with failure(True, 'to be False'):
                        expect(True).to.be.false

            with describe('none'):
                def it_should_pass_if_actual_is_none():
                    expect(None).to.be.none

                def it_should_fail_if_actual_is_not_none():
                    with failure(True, 'to be None'):
                        expect(True).to.be.none

            with describe('empty'):
                def it_should_pass_if_actual_is_empty():
                    expect('').to.be.empty

                def it_should_fail_if_actual_is_not_empty():
                    actual = 'foo'

                    with failure(actual, 'to be empty'):
                        expect(actual).to.be.empty

        with describe('have'):
            def it_should_pass_if_actual_has_expected_item():
                expect(_.lst).to.have('bar')

            def it_should_pass_if_actual_has_expected_items():
                expect(_.lst).to.have('bar', 'baz')

            def it_should_fail_if_actual_does_not_have_expected_item():
                with failure(_.lst, "to have 'foo'"):
                    expect(_.lst).to.have('bar', 'foo')

            with describe('property'):
                def it_should_pass_if_actual_has_property():
                    expect(_.obj).to.have.property('bar')

                def it_should_pass_if_actual_has_property_with_value():
                    expect(_.obj).to.have.property('bar', 0)

                def it_should_fail_if_actual_does_not_have_property():
                    with failure(_.obj, "to have property 'foo'"):
                        expect(_.obj).to.have.property('foo')

                def it_should_fail_if_actual_does_not_have_property_with_value():
                    with failure(_.obj, "to have property 'foo'"):
                        expect(_.obj).to.have.property('foo', 0)

                def it_should_fail_if_actual_has_property_without_value():
                    with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
                        expect(_.obj).to.have.property('bar', 1)

                def it_should_fail_if_actual_has_property_without_none_value():
                    with failure(_.obj, "to have property 'bar' with value None but was 0"):
                        expect(_.obj).to.have.property('bar', None)

            with describe('properties'):
                def it_should_pass_if_actual_has_properties_in_args():
                    expect(_.obj).to.have.properties('bar', 'baz')

                def it_should_pass_if_actual_has_properties_in_kwargs():
                    expect(_.obj).to.have.properties(bar=0, baz=1)

                def it_should_pass_if_actual_has_properties_in_args_and_kwargs():
                    expect(_.obj).to.have.properties('bar', baz=1)

                def it_should_pass_if_actual_has_properties_in_dict():
                    expect(_.obj).to.have.properties({'bar': 0, 'baz': 1})

                def it_should_fail_if_actual_does_not_have_property_in_args():
                    with failure(_.obj, "to have property 'foo'"):
                        expect(_.obj).to.have.properties('bar', 'foo')

                def it_should_fail_if_actual_does_not_have_property_in_kwargs():
                    with failure(_.obj, "to have property 'foo'"):
                        expect(_.obj).to.have.properties(bar=0, foo=1)

                def it_should_fail_if_actual_has_property_without_value_in_kwargs():
                    with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
                        expect(_.obj).to.have.properties(bar=1, baz=1)

                def it_should_fail_if_actual_does_not_have_property_in_args_but_in_kwargs():
                    with failure(_.obj, "to have property 'foo'"):
                        expect(_.obj).to.have.properties('foo', bar=0)

                def it_should_fail_if_actual_has_property_in_args_and_kwargs_without_value():
                    with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
                        expect(_.obj).to.have.properties('baz', bar=1)

                def it_should_fail_if_actual_has_property_without_value_in_dict():
                    with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
                        expect(_.obj).to.have.properties({'bar': 1, 'baz': 1})

            with describe('key'):
                def it_should_pass_if_actual_has_expected_key():
                    expect(_.dct).to.have.key('bar')

                def it_should_pass_if_actual_has_key_and_value():
                    expect(_.dct).to.have.key('bar', 0)

                def it_should_fail_if_actual_does_not_have_expected_key():
                    with failure(_.dct, "to have key 'foo'"):
                        expect(_.dct).to.have.key('foo')

                def it_should_fail_if_actual_does_not_have_key_with_value():
                    with failure(_.dct, "to have key 'foo'"):
                        expect(_.dct).to.have.key('foo', 0)

                def it_should_fail_if_actual_has_key_without_expected_value():
                    with failure(_.dct, "to have key 'bar' with value 1 but was 0"):
                        expect(_.dct).to.have.key('bar', 1)

                def it_should_fail_if_actual_has_key_without_none_value():
                    with failure(_.dct, "to have key 'bar' with value None but was 0"):
                        expect(_.dct).to.have.key('bar', None)

            with describe('keys'):
                def it_should_pass_if_actual_has_keys_in_args():
                    expect(_.dct).to.have.keys('bar', 'baz')

                def it_should_pass_if_actual_has_keys_in_kwargs():
                    expect(_.dct).to.have.keys(bar=0, baz=1)

                def it_should_pass_if_actual_has_keys_in_args_and_kwargs():
                    expect(_.dct).to.have.keys('bar', baz=1)

                def it_should_pass_if_actual_has_keys_in_dict():
                    expect(_.dct).to.have.keys({'bar': 0, 'baz': 1})

                def it_should_fail_if_actual_does_not_have_key_in_args():
                    with failure(_.dct, "to have key 'foo'"):
                        expect(_.dct).to.have.keys('bar', 'foo')

                def it_should_fail_if_actual_does_not_have_key_in_kwargs():
                    with failure(_.dct, "to have key 'foo'"):
                        expect(_.dct).to.have.keys(bar=0, foo=1)

                def it_should_fail_if_actual_has_key_without_value_in_kwargs():
                    with failure(_.dct, "to have key 'bar' with value 1 but was 0"):
                        expect(_.dct).to.have.keys(bar=1, baz=1)

                def it_should_fail_if_actual_does_not_have_key_in_args_but_in_kwargs():
                    with failure(_.dct, "to have key 'foo'"):
                        expect(_.dct).to.have.keys('foo', bar=0)

                def it_should_fail_if_actual_has_key_in_args_and_kwargs_without_value():
                    with failure(_.dct, "to have key 'bar' with value 1 but was 0"):
                        expect(_.dct).to.have.keys('baz', bar=1)

                def it_should_fail_if_actual_has_key_without_value_in_dict():
                    with failure(_.dct, "to have key 'bar' with value 1 but was 0"):
                        expect(_.dct).to.have.keys({'bar': 1, 'baz': 1})

            with describe('length'):
                def it_should_pass_if_actual_has_the_expected_length():
                    expect('foo').to.have.length(3)

                def it_should_fail_if_actual_does_not_have_the_expected_length():
                    actual = 'foo'

                    with failure(actual, 'to have length 2 but was 3'):
                        expect(actual).to.have.length(2)

    with describe('not_to'):
        with describe('equal'):
            def it_should_pass_if_actual_does_not_equal_expected():
                expect(1).not_to.equal(2)

            def it_should_fail_if_actual_equals_expected():
                with failure(1, 'not to equal 1'):
                    expect(1).not_to.equal(1)

        with describe('match'):
            def it_should_pass_if_actual_does_not_match_expected_regexp():
                expect(_.str).not_to.match(r'My \W+ string')

            def it_should_pass_if_actual_does_not_match_expected_regexp_with_re_flags():
                expect(_.str).not_to.match(r'My \W+ string', re.I)

            def it_should_fail_if_actual_matches_expected_regexp():
                pattern = r'My \w+ string'

                with failure(_.str, 'not to match {}'.format(repr(pattern))):
                    expect(_.str).not_to.match(pattern)

        with describe('raise_error'):
            def it_should_pass_if_actual_does_not_raise_expected_exception():
                def callback():
                    raise AttributeError()

                expect(callback).not_to.raise_error(KeyError)

            def it_should_pass_if_actual_does_not_raise_exception():
                expect(lambda: None).not_to.raise_error(AttributeError)

            def it_should_pass_if_actual_raises_expected_exception_with_different_message():
                def callback():
                    raise AttributeError('bar')

                expect(callback).not_to.raise_error(AttributeError, 'foo')

            def it_should_fail_if_actual_raises_expected_exception():
                def callback():
                    raise AttributeError()

                with failure(callback, 'not to raise AttributeError but AttributeError raised'):
                    expect(callback).not_to.raise_error(AttributeError)

            def it_should_fail_if_actual_raises_expected_exception_with_message():
                message = 'Foo error'
                failure_message = 'not to raise AttributeError with message {} but message was {}'.format(
                    repr(message), repr(message))

                def callback():
                    raise AttributeError(message)

                with failure(callback, failure_message):
                    expect(callback).not_to.raise_error(AttributeError, message)

        with describe('be'):
            def it_should_pass_if_actual_is_not_expected():
                expect(1).not_to.be(2)

            def it_should_fail_if_actual_is_expected():
                value = 1

                with failure(1, 'not to be 1'):
                    expect(value).not_to.be(value)

            with describe('equal'):
                def it_should_pass_if_actual_does_not_equal_expected_():
                    expect(1).not_to.be.equal(2)

                def it_should_fail_if_actual_equals_expected_():
                    with failure(1, 'not to be equal 1'):
                        expect(1).not_to.be.equal(1)

            with describe('a'):
                def it_should_pass_if_actual_is_not_an_instance_of_the_expected_class():
                    class Bar(object):
                        pass

                    expect(_.obj).not_to.be.a(Bar)

                def it_should_fail_if_actual_is_a_subclass_instance_of_the_expected_class():
                    with failure(_.obj, 'not to be a object instance'):
                        expect(_.obj).not_to.be.a(object)

                def it_should_fail_if_actual_is_an_instance_of_the_expected_class():
                    with failure(_.obj, 'not to be a Foo instance'):
                        expect(_.obj).not_to.be.a(Foo)

            with describe('an'):
                def it_should_pass_if_actual_is_not_an_instance_of_the_expected_class_():
                    class Object(object):
                        pass

                    expect(_.obj).not_to.be.an(Object)

                def it_should_fail_if_actual_is_an_instance_of_the_expected_class_():
                    with failure(_.obj, 'not to be an object instance'):
                        expect(_.obj).not_to.be.an(object)

            with describe('greater_than'):
                def it_should_pass_if_actual_is_not_greater_than_expected():
                    expect(1).not_to.be.greater_than(4)

                def it_should_fail_if_actual_is_greater_than_expected():
                    with failure(5, 'not to be greater than 4'):
                        expect(5).not_to.be.greater_than(4)

            with describe('greater_or_equal_to'):
                def it_should_pass_if_actual_is_not_greater_or_equal_to_expected():
                    expect(1).not_to.be.greater_or_equal_to(4)

                def it_should_fail_if_actual_is_greater_than_expected_():
                    with failure(5, 'not to be greater or equal to 4'):
                        expect(5).not_to.be.greater_or_equal_to(4)

                def it_should_fail_if_actual_is_equal_to_expected():
                    with failure(5, 'not to be greater or equal to 5'):
                        expect(5).not_to.be.greater_or_equal_to(5)

            with describe('less_than'):
                def it_should_pass_if_actual_is_not_less_than_expected():
                    expect(4).not_to.be.less_than(1)

                def it_should_fail_if_actual_is_less_than_expected():
                    with failure(1, 'not to be less than 4'):
                        expect(1).not_to.be.less_than(4)

            with describe('less_or_equal_to'):
                def it_should_pass_if_actual_is_not_less_or_equal_to_expected():
                    expect(4).not_to.be.less_or_equal_to(1)

                def it_should_fail_if_actual_is_less_than_expected_():
                    with failure(1, 'not to be less or equal to 4'):
                        expect(1).not_to.be.less_or_equal_to(4)

                def it_should_fail_if_actual_is_equal_to_expected_():
                    with failure(5, 'not to be less or equal to 5'):
                        expect(5).not_to.be.less_or_equal_to(5)

            with describe('within'):
                def it_should_pass_if_actual_is_not_within_expected_range():
                    expect(1).not_to.be.within(4, 7)

                def it_should_fail_if_actual_is_within_expected_range():
                    with failure(5, 'not to be within 4, 7'):
                        expect(5).not_to.be.within(4, 7)

            with describe('true'):
                def it_should_pass_if_actual_is_not_true():
                    expect(False).not_to.be.true

                def it_should_fail_if_actual_is_true_():
                    with failure(True, 'not to be True'):
                        expect(True).not_to.be.true

            with describe('false'):
                def it_should_pass_if_actual_is_not_false():
                    expect(True).not_to.be.false

                def it_should_fail_if_actual_is_false_():
                    with failure(False, 'not to be False'):
                        expect(False).not_to.be.false

            with describe('none'):
                def it_should_pass_if_actual_is_not_none():
                    expect('foo').not_to.be.none

                def it_should_fail_if_actual_is_none():
                    with failure(None, 'not to be None'):
                        expect(None).not_to.be.none

            with describe('empty'):
                def it_should_pass_if_actual_is_not_empty():
                    expect('foo').not_to.be.empty

                def it_should_fail_if_actual_is_empty():
                    actual = ''

                    with failure(actual, 'not to be empty'):
                        expect(actual).not_to.be.empty

        with describe('have'):
            def it_should_pass_if_actual_does_not_have_expected_item():
                expect(_.lst).not_to.have('foo')

            def it_should_pass_if_actual_does_not_have_expected_items():
                expect(_.lst).not_to.have('foo', 'foobar')

            def it_should_fail_if_actual_has_expected_item():
                with failure(_.lst, "not to have 'bar'"):
                    expect(_.lst).not_to.have('bar', 'foo')

            with describe('property'):
                def it_should_pass_if_actual_does_not_have_property():
                    expect(_.obj).not_to.have.property('foo')

                def it_should_pass_if_actual_does_not_have_property_with_value():
                    expect(_.obj).not_to.have.property('foo', 0)

                def it_should_pass_if_actual_has_property_without_value():
                    expect(_.obj).not_to.have.property('bar', 1)

                def it_should_fail_if_actual_has_property():
                    with failure(_.obj, "not to have property 'bar'"):
                        expect(_.obj).not_to.have.property('bar')

                def it_should_fail_if_actual_has_property_with_value():
                    with failure(_.obj, "not to have property 'bar' with value 0 but was 0"):
                        expect(_.obj).not_to.have.property('bar', 0)

            with describe('properties'):
                def it_should_pass_if_actual_does_not_have_properties_in_args():
                    expect(_.obj).not_to.have.properties('foo', 'foobar')

                def it_should_pass_if_actual_does_not_have_properties_in_kwargs():
                    expect(_.obj).not_to.have.properties(foo=0, foobar=1)

                def it_should_pass_if_actual_has_property_without_value_in_kwargs():
                    expect(_.obj).not_to.have.properties(foo=0, bar=1)

                def it_should_pass_if_actual_does_not_have_properties_in_dict():
                    expect(_.obj).not_to.have.properties({'foo': 0, 'foobar': 1})

                def it_should_pass_if_actual_has_property_without_value_in_dict():
                    expect(_.obj).not_to.have.properties({'foo': 0, 'bar': 1})

                def it_should_fail_if_actual_has_property_in_args():
                    with failure(_.obj, "not to have property 'bar'"):
                        expect(_.obj).not_to.have.properties('foo', 'bar')

                def it_should_fail_if_actual_has_property_in_kwargs_with_value():
                    with failure(_.obj, "not to have property 'bar' with value 0 but was 0"):
                        expect(_.obj).not_to.have.properties(baz=0, bar=0)

                def it_should_fail_if_actual_has_property_in_args_but_not_in_kwargs():
                    with failure(_.obj, "not to have property 'bar'"):
                        expect(_.obj).not_to.have.properties('bar', baz=0)

                def it_should_fail_if_actual_has_property_in_kwargs_but_not_in_args():
                    with failure(_.obj, "not to have property 'bar' with value 0 but was 0"):
                        expect(_.obj).not_to.have.properties('foo', bar=0)

                def it_should_fail_if_actual_has_property_in_dict_with_value():
                    with failure(_.obj, "not to have property 'bar' with value 0 but was 0"):
                        expect(_.obj).not_to.have.properties({'bar': 0, 'foo': 1})

            with describe('key'):
                def it_should_pass_if_actual_does_not_have_expected_key():
                    expect(_.dct).not_to.have.key('foo')

                def it_should_pass_if_actual_does_not_have_expected_key_with_value():
                    expect(_.dct).not_to.have.key('foo', 0)

                def it_should_pass_if_actual_has_expected_key_without_value():
                    expect(_.dct).not_to.have.key('bar', 1)

                def it_should_fail_if_actual_has_expected_key():
                    with failure(_.dct, "not to have key 'bar'"):
                        expect(_.dct).not_to.have.key('bar')

                def it_should_fail_if_actual_has_expected_key_with_value():
                    with failure(_.dct, "not to have key 'bar' with value 0 but was 0"):
                        expect(_.dct).not_to.have.key('bar', 0)

            with describe('keys'):
                def it_should_pass_if_actual_does_not_have_keys_in_args():
                    expect(_.dct).not_to.have.keys('foo', 'foobar')

                def it_should_pass_if_actual_does_not_have_keys_in_kwargs():
                    expect(_.dct).not_to.have.keys(foo=0, foobar=1)

                def it_should_pass_if_actual_has_key_without_value_in_kwargs():
                    expect(_.dct).not_to.have.keys(foo=0, bar=1)

                def it_should_pass_if_actual_does_not_have_keys_in_dict():
                    expect(_.dct).not_to.have.keys({'foo': 0, 'foobar': 1})

                def it_should_pass_if_actual_has_key_without_value_in_dict():
                    expect(_.dct).not_to.have.keys({'foo': 0, 'bar': 1})

                def it_should_fail_if_actual_has_key_in_args():
                    with failure(_.dct, "not to have key 'bar'"):
                        expect(_.dct).not_to.have.keys('foo', 'bar')

                def it_should_fail_if_actual_has_key_in_kwargs_with_value():
                    with failure(_.dct, "not to have key 'bar' with value 0 but was 0"):
                        expect(_.dct).not_to.have.keys(baz=0, bar=0)

                def it_should_fail_if_actual_has_key_in_args_but_not_in_kwargs():
                    with failure(_.dct, "not to have key 'bar'"):
                        expect(_.dct).not_to.have.keys('bar', baz=0)

                def it_should_fail_if_actual_has_key_in_kwargs_but_not_in_args():
                    with failure(_.dct, "not to have key 'bar' with value 0 but was 0"):
                        expect(_.dct).not_to.have.keys('foo', bar=0)

                def it_should_fail_if_actual_has_key_in_dict_with_value():
                    with failure(_.dct, "not to have key 'bar' with value 0 but was 0"):
                        expect(_.dct).not_to.have.keys({'bar': 0, 'foo': 1})

            with describe('length'):
                def it_should_pass_if_actual_does_not_have_the_expected_length():
                    expect('foo').not_to.have.length(2)

                def it_should_fail_if_actual_has_the_expected_length():
                    actual = 'foo'

                    with failure(actual, 'not to have length 3 but was 3'):
                        expect(actual).not_to.have.length(3)

    @before.all
    def fixtures():
        _.obj = Foo()
        _.dct = {'bar': 0, 'baz': 1}
        _.lst = _.dct.keys()
        _.str = 'My foo string'
