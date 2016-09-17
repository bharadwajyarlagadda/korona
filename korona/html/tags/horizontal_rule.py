# -*- coding: utf-8 -*-
"""Module for constructing <hr> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_attribute_values
from ...templates.html.tags import hr


class HR(object):
    """Class for constructing hr tag.

    Args:
        align (str): Specifies the alignment of a <hr> element.
        noshade (bool): Specifies that a <hr> element should render in one
            solid color (noshaded), instead of a shaded color.
        size (str): Specifies the height of a <hr> element.
        width (str): Specifies the width of a <hr> element

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, noshade=False, size=None, width=None):
        self.tag = 'hr'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align,
                       'noshade': noshade,
                       'size': size,
                       'width': width}

    def construct(self):
        """Returns the constructed hr tag <hr>."""
        return hr.render(self.values)
