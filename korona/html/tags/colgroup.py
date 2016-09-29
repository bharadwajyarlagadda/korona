# -*- coding: utf-8 -*-
"""Module for constructing <colgroup> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_attribute_values
from ...templates.html.tags import colgroup

ATTRIBUTES = {
    'align': {
        'description': 'Aligns the content in a column group',
        'values': ['left', 'right', 'center', 'justify', 'char']
    },
    'char': {
        'description': 'Aligns the content in a column group to a '
                       'character',
        'values': None
    },
    'charoff': {
        'description': 'Sets the number of characters the content '
                       'will be aligned from the character specified '
                       'by the char attribute',
        'values': None
    },
    'span': {
        'description': 'Specifies the number of columns a column '
                       'group should span',
        'values': None
    },
    'valign': {
        'description': 'Vertical aligns the content in a column group',
        'values': ['top', 'middle', 'bottom', 'baseline']
    },
    'width': {
        'description': 'Specifies the width of a column group',
        'values': None
    }
}


class ColGroup(object):
    """Class for constructing colgroup tag.

    Args:
        align (str): Aligns the content in a column group.
        char (str): Aligns the content in a column group to a character.
        charoff (int): Sets the number of characters the content will be
            aligned from the character specified by the char attribute.
        span (int): Specifies the number of columns a column group should span.
        valign (str): Vertical aligns the content in a column group.
        width (str): Specifies the width of a column group.

    .. versionadded:: 0.2.0
    """
    def __init__(self,
                 align=None,
                 char=None,
                 charoff=None,
                 span=None,
                 valign=None,
                 width=None):
        self.tag = 'colgroup'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  attribute_value=align,
                                  default_values=ATTRIBUTES['align']['values'])
        self.validate_char_attribute(align=align, value=char)
        self.validate_charoff_attribute(align=align, char=char, value=charoff)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='valign',
            attribute_value=valign,
            default_values=ATTRIBUTES['valign']['values'])
        self.values = {'align': align,
                       'char': char,
                       'charoff': charoff,
                       'span': span,
                       'valign': valign,
                       'width': width}

    def construct(self):
        """Returns the constructed colgroup tag <colgroup>."""
        return colgroup.render(self.values)

    def validate_char_attribute(self, align, value):
        """Validates char attribute. The char attribute can only be used if
        the align attribute is set to "char".
        """
        if not value:
            return

        if value and align != 'char':
            raise AttributeError('<colgroup>: The char attribute can only be '
                                 'used if the align attribute is set to '
                                 '"char".')

    def validate_charoff_attribute(self, align, char, value):
        """Validates charoff attribute. The charoff attribute can only be
        used if the char attribute is specified and the align attribute is
        set to "char".
        """
        if not value:
            return

        if value and (not char or align != 'char'):
            raise AttributeError('<colgroup>: The charoff attribute can only '
                                 'be used if the char attribute is specified '
                                 'and the align attribute is set to "char".')
