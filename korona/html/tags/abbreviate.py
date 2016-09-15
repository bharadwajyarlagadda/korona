# -*- coding: utf-8 -*-
"""Module for constructing abbreviate <abbr> tag."""

from __future__ import absolute_import

from ...templates.html import abbr_tag


class Abbr(object):
    """Class for constructing abbr tag.

    Args:
        text (str): Abbr tag text. (Ex. <abbr>text</abbr>)

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text=None):
        self.tag = 'abbr'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed abbr tag <abbr></abbr>."""
        return abbr_tag.render(self.values)
