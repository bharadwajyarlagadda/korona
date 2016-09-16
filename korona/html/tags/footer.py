# -*- coding: utf-8 -*-
"""Module for constructing <footer> tag."""

from ...templates.html.tags import footer_tag


class Footer(object):
    """Class for constructing the footer tag.

    Args:
        text (str): Specifies the footer text. (As in <footer>{text}</footer>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        # TODO: Add support for inner tags.
        self.tag = 'footer'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed footer tag <footer></footer>."""
        return footer_tag.render(self.values)
