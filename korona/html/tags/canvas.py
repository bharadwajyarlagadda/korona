# -*- coding: utf-8 -*-
"""Module for constructing <canvas> tag."""

from ...lib.utils import validate_tag_attribute_value
from ...templates.html.tags import canvas_tag


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
        validate_tag_attribute_value(tag=self.tag, value=height)
        validate_tag_attribute_value(tag=self.tag, value=width)
        self.values = {'height': height, 'width': width}

    def construct(self):
        """Returns the constructed canvas tag <canvas>."""
        return canvas_tag.render(self.values)
