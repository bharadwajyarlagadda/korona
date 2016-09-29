# -*- coding: utf-8 -*-

from future.moves.urllib.parse import urlparse
import datetime

from ..exceptions import AttributeValueError, TagAttributeError
from ..html.root.tags import TAGS


def validate_tag(tag=None):
    """Validates whether the given tag is supported by korona or not."""
    if not tag:
        raise AttributeError('Tag cannot be empty')

    if tag not in TAGS:
        raise ValueError('{0} tag is not supported')


def validate_string_attribute(tag, attribute_name, attribute_value):
    """Validates whether the given value is a string or not."""
    if not attribute_value:
        return

    if not isinstance(attribute_value, str):
        raise AttributeValueError('<{tag}>: {attribute_name} should be a '
                                  'string value.'
                                  .format(tag=tag,
                                          attribute_name=attribute_name))


def validate_attribute_values(tag,
                              attribute_name,
                              attribute_value,
                              default_values):
    """Validates whether the given attribute value is a valid value or not.
    Some of the attributes have confined values. Even if we give some
    other value, the html output would not be correct.
    """
    if not attribute_value:
        return

    if attribute_value not in default_values:
        raise TagAttributeError('<{tag}>: {attribute_name} attribute '
                                'values should be one of these: {values}'
                                .format(tag=tag,
                                        attribute_name=attribute_name,
                                        values=','.join(default_values)))


def validate_boolean_attribute(tag, attribute_name, attribute_value):
    """Validates whether the given attribute value is boolean or not."""
    if not attribute_value:
        return

    if not isinstance(attribute_value, bool):
        raise AttributeError('<{tag}>: {attribute_name} attribute should be a '
                             'boolean value.'
                             .format(tag=tag, attribute_name=attribute_name))


def validate_number_attribute(tag, attribute_name, attribute_value):
    """Validates whether the given attribute value is an integer or float
    value.
    """
    if not attribute_value:
        return

    # If the given attribute value is either integer/float, then return the
    # value.
    if isinstance(attribute_value, (int, float)):
        return attribute_value
    # Give attribute value can be a string. For example, the given attribute
    # value can be '1'. When we do int('1') --> returns 1. The same logic
    # works in float values also. So, if we do float('1.23') --> returns 1.23.
    # If both the cases fail, then we raise an AttributeError.
    elif isinstance(attribute_value, str):
        try:
            return int(attribute_value)
        except ValueError:
            try:
                return float(attribute_value)
            except ValueError:
                raise AttributeError('<{tag}>: {attribute} attribute should '
                                     'be an integer or float value'
                                     .format(tag=tag,
                                             attribute=attribute_name))
    else:
        # In rest all the cases, the attirbute value is not a valid int/float
        # value.
        raise AttributeError('<{tag}>: {attribute} attribute should be an '
                             'integer or float value'
                             .format(tag=tag, attribute=attribute_name))


def validate_date_attribute(tag, attribute_name, attribute_value):
    """Validates whether the given attribute values is a datetime value or
    not.
    """
    if not attribute_value:
        return

    # TODO: This can be extended to multiple datetime types. For example,
    # packages like zulu, Arrow, etc. have their own types but they all are
    # valid datetime types. Those can be added in the future.
    if isinstance(attribute_value, (datetime.datetime, datetime.date)):
        return attribute_value
    else:
        raise AttributeError('<{tag}>: {attribute} attribute should be a '
                             'date/datetime value.'
                             .format(tag=tag, attribute=attribute_name))


def validate_time_attribute(tag, attribute_name, attribute_value):
    """Validates whether the given attribute values is a time value or not."""
    if not attribute_value:
        return

    # TODO: This can be extended to multiple time types. For example,
    # packages like zulu, Arrow, etc. have their own types but they all are
    # valid time types. Those can be added in the future.
    if isinstance(attribute_value, datetime.time):
        return attribute_value
    else:
        raise AttributeError('<{tag}>: {attribute} attribute should be a '
                             'time value.'
                             .format(tag=tag, attribute=attribute_name))


def validate_url(attribute_name, url):
    """Validates whether the given string is a URL or not."""
    if not url:
        return

    try:
        result = urlparse(url=url)
        if [result.scheme, result.netloc, result.path]:
            return True
    except:
        raise ValueError('{attribute_name}: The given string {url} is not a '
                         'valid url.'
                         .format(attribute_name=attribute_name, url=url))
