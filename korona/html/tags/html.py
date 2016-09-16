# -*- coding: utf-8 -*-
"""Module for constructing <html> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_url
from ...templates.html.tags import html_tag


class Html(object):
    """Class for constructing html tag.

    Args:
        manifest (str): Specifies the address of the document's cache manifest
            (for offline browsing)
        xmlns (str): Specifies the XML namespace attribute (If you need your
            content to conform to XHTML)
        text (str): Specifies the html text. (As in <html>{text}</html>)

    .. versionadded:: 0.4.0-dev
    """
    def __init__(self, manifest=None, xmlns=None, text=None):
        # TODO: Add support for inner tags.
        self.tag = 'html'
        validate_url(attribute_name='manifest', url=manifest)
        self.values = {'manifest': manifest,
                       'xmlns': xmlns,
                       'text': text}

    def construct(self):
        """Returns the constructed html tag <html>."""
        return html_tag.render(self.values)
