# -*- coding: utf-8 -*-
"""Module for constructing delete tag <del>."""

from __future__ import absolute_import

from ...templates.html.tags import del_tag


class Del(object):
    """Class for constructing del tag.

    Args:
        cite (str): Specifies a URL to a document that explains the reason
            why the text was deleted.
        datetime (datetime): Specifies the date and time of when the text was
            deleted.

    .. versionadded:: 0.2.0
    """
    def __init__(self, cite=None, datetime=None, text=None):
        self.tag = 'del'
        # TODO: If possible, add validation for attribute cite
        self.values = {'cite': cite, 'datetime': datetime, 'text': text}

    def construct(self):
        """Returns the constructed del tag <del>."""
        return del_tag.render(self.values)
