# -*- coding: utf-8 -*-
"""Module for constructing <div> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_attribute_values
from ...templates.html.tags import div

ATTRIBUTES = {
    'align': {
        'description': 'Specifies the alignment of the content inside '
                       'a <div> element',
        'values': ['left', 'right', 'center', 'justify']
    }
}


class Div(object):
    """Class for constructing div tag.

    Args:
        align (str): Specifies the alignment of the content inside a <div>
            element.
        text (str): Specifies the div text. (As in <div>{text}</div>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'div'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  attribute_value=align,
                                  default_values=ATTRIBUTES['align']['values'])
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed div tag <div></div>."""
        return div.render(self.values)
