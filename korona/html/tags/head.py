# -*- coding: utf-8 -*-
"""Module for constructing <head> tag."""

from __future__ import absolute_import

from ...templates.html.tags import head_tag


class Head(object):
    """Class for constructing <head> tag.

    Args:
        text (str): Specifies the head text. (As in <head>{text}</head>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, text=None):
        # TODO: Add the ability to validate which inner tags can go into the
        # <head> tag.
        self.tag = 'head'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed tag <head>."""
        return head_tag.render(self.values)
