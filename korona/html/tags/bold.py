# -*- coding: utf-8 -*-
"""Module for constructing <b> tag."""

from __future__ import absolute_import

from ...templates.html.tags import bold_tag


class B(object):
    """Class for constructing bold tag.

    Args:
        text (str): Bold tag text. (Ex. <b>text</b>)

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text=None):
        self.tag = 'b'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed bold tag <b></b>."""
        return bold_tag.render(self.values)
