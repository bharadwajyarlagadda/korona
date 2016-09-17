# -*- coding: utf-8 -*-
"""Module for constructing <acronym> tag."""


from __future__ import absolute_import

from ...templates.html.tags import acronym


class Acronym(object):
    """Class for constructing acronym tag.

    Args:
        text (str): Acronym tag text. (Ex. <acronym>text</acronym>)

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text=None):
        self.tag = 'acronym'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed acronym tag <acronym></acronym>."""
        return acronym.render(self.values)
