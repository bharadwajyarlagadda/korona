# -*- coding: utf-8 -*-
"""Module for constructing <canvas> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_string_attribute
from ...templates.html.tags import canvas


class Canvas(object):
    """Class for constructing canvas tag.

    Args:
        height (str): Specifies the height of the canvas.
        width (str): Specifies the width of the canvas.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, height=None, width=None):
        # TODO: Possible add the canvas text attribute.
        self.tag = 'canvas'
        validate_string_attribute(tag=self.tag,
                                  attribute_name='height',
                                  attribute_value=height)
        validate_string_attribute(tag=self.tag,
                                  attribute_name='width',
                                  attribute_value=width)
        self.values = {'height': height, 'width': width}

    def construct(self):
        """Returns the constructed canvas tag <canvas>."""
        return canvas.render(self.values)
