# -*- coding: utf-8 -*-
"""Module for constructing <article> tag."""

from __future__ import absolute_import

from ...templates.html.tags import article


class Article(object):
    """Class for constructing article tag.

    Args:
        text (str): Article tag text. (Ex. <article>text</article>)

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text=None):
        self.tag = 'article'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed article tag <article></article>."""
        return article.render(self.values)
