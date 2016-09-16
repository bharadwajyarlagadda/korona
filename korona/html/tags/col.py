# -*- coding: utf-8 -*-
"""Module for constructing <col> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_attribute_values
from ...templates.html.tags import col_tag


class Col(object):
    """Class for constructing col tag.

    Args:
        align (str): Specifies the alignment of the content related to a <col>
            element.
        char (str): Specifies the alignment of the content related to a <col>
            element to a character.
        charoff (int): Specifies the number of characters the content will be
            aligned from the character specified by the char attribute.
        span (int): Specifies the number of columns a <col> element should
            span.
        valign (str): Specifies the vertical alignment of the content related
            to a <col> element.
        width (str): Specifies the width of a <col> element.

    .. versionadded:: 0.2.0
    """
    def __init__(self,
                 align=None,
                 char=None,
                 charoff=None,
                 span=None,
                 valign=None,
                 width=None):
        self.tag = 'col'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.validate_char_attribute(align=align, value=char)
        self.validate_charoff_attribute(align=align, char=char, value=charoff)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='valign',
                                  value=valign)
        self.values = {'align': align,
                       'char': char,
                       'charoff': charoff,
                       'span': span,
                       'valign': valign,
                       'width': width}

    def construct(self):
        """Returns the constructed col tag <col>."""
        return col_tag.render(self.values)

    def validate_char_attribute(self, align, value):
        """Validates char attribute. The char attribute can only be used if
        the align attribute is set to "char".
        """
        if not value:
            return

        if value and align != 'char':
            raise AttributeError('<col>: The char attribute can only be used '
                                 'if the align attribute is set to "char".')

    def validate_charoff_attribute(self, align, char, value):
        """Validates charoff attribute. The charoff attribute can only be
        used if the char attribute is specified and the align attribute is
        set to "char".
        """
        if not value:
            return

        if value and (not char or align != 'char'):
            raise AttributeError('<col>: The charoff attribute can only be '
                                 'used if the char attribute is specified and '
                                 'the align attribute is set to "char".')
