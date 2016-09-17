# -*- coding: utf-8 -*-
"""Module for constructing <figure> tag."""

from __future__ import absolute_import

from ...templates.html.tags import figure


class Figure(object):
    """Class for constructing figure tag.

    Args:
        text (str): Specifies the figure text. (As in <figure>{text}</figure>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        # TODO: Add support for inner tags.
        self.tag = 'figure'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed figure tag <figure></figure>."""
        return figure.render(self.values)
