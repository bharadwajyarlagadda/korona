# -*- coding: utf-8 -*-
"""Module for constructing <frameset> tag."""

from __future__ import absolute_import

from ...templates.html.tags import frameset


class FrameSet(object):
    """Class for constructing <frameset> tag.

    Args:
        cols (str): Specifies the number and size of columns in a frameset.
        rows (str): Specifies the number and size of rows in a frameset.

    .. versionadded:: 0.2.0
    """
    def __init__(self, cols=None, rows=None):
        self.tag = 'frameset'
        self.values = {'cols': cols, 'rows': rows}

    def construct(self):
        """Returns the constructed tag <frameset>."""
        return frameset.render(self.values)
