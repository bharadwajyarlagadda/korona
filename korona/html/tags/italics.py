# -*- coding: utf-8 -*-
"""Module for constructing <i> tag."""

from __future__ import absolute_import

from ...templates.html.tags import italics_tag


class I(object):
    """Class for constructing <i> tag.

    Args:
        text (str): Specifies the italics text. (As in <i>{text}</i>)

    .. versionadded:: 0.4.0
    """
    def __init__(self, text=None):
        self.tag = 'i'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed italics tag <i>."""
        return italics_tag.render(self.values)
