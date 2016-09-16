# -*- coding: utf-8 -*-
"""Module for constructing <embed> tag."""

from ...templates.html.tags import embed_tag


class Embed(object):
    """Class for constructing embed tag.

    Args:
        height (str): Specifies the height of the embedded content (in pixels).
        width (str): Specifies the width of the embedded content (in pixels).
        src (str): Specifies the address of the external file to embed.
        type (str): Specifies the media type of the embedded content.

    .. versionadded:: 0.2.0
    """
    def __init__(self, height=None, width=None, src=None, type=None):
        self.tag = 'embed'
        self.values = {'height': height,
                       'width': width,
                       'src': src,
                       'type': type}

    def construct(self):
        """Returns the constructed embed tag <embed>."""
        return embed_tag.render(self.values)
