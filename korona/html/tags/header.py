# -*- coding: utf-8 -*-
"""Module for constructing <header> tag."""

from __future__ import absolute_import

from ...templates.html.tags import header_tag


class Header(object):
    """Class for constructing the header tag.

    Args:
        text (str): Specifies the header text. (As in <header>{text}</header>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, text=None):
        # TODO: Add support for inner tags.
        self.tag = 'header'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed header tag <header></header>."""
        return header_tag.render(self.values)
