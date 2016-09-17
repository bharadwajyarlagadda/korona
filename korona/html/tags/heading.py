# -*- coding: utf-8 -*-
"""Module for constructing <h1>-<h6> tags."""

from __future__ import absolute_import

from ...lib.utils import validate_attribute_values
from ...templates.html.tags import h1, h2, h3, h4, h5, h6


class H1(object):
    """Class for constructing <h1> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h1> text. (As in <h1>{text}</h1>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h1'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h1>."""
        return h1.render(self.values)


class H2(object):
    """Class for constructing <h2> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h2> text. (As in <h2>{text}</h2>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h2'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h2>."""
        return h2.render(self.values)


class H3(object):
    """Class for constructing <h3> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h3> text. (As in <h3>{text}</h3>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h3'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h3>."""
        return h3.render(self.values)


class H4(object):
    """Class for constructing <h4> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h4> text. (As in <h4>{text}</h4>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h4'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h4>."""
        return h4.render(self.values)


class H5(object):
    """Class for constructing <h5> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h5> text. (As in <h5>{text}</h5>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h5'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h5>."""
        return h5.render(self.values)


class H6(object):
    """Class for constructing <h6> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h6> text. (As in <h6>{text}</h6>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h6'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h6>."""
        return h6.render(self.values)
