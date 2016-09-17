# -*- coding: utf-8 -*-
"""Module for constructing <address> tag."""


from __future__ import absolute_import

from ...templates.html.tags import address


class Address(object):
    """Class for constructing address tag.

    Args:
        text (str): Address tag text. (Ex. <address>text</address>)

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text=None):
        self.tag = 'address'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed address tag <address></address>."""
        return address.render(self.values)
