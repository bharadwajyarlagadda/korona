# -*- coding: utf-8 -*-


from ..html.tags import TAGS


def validate_tag(tag=None):
    """Validates whether the given tag is supported by korona or not."""
    if not tag:
        raise AttributeError('Tag cannot be empty')

    if tag not in TAGS:
        raise ValueError('{0} tag is not supported')


def validate_tag_attribute_value(tag, value):
    """Validates whether the given value is a string or not."""
    if not value:
        return

    # If the attribute value is not a string raise a ValueError.
    if not isinstance(value, str):
        raise ValueError('<{tag}>: {value} should be a string'
                         .format(tag=tag, value=value))
