# -*- coding: utf-8 -*-
"""Module for constructing <base> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_url
from ...templates.html.tags import base_tag


class Base(object):
    """Class for constructing base tag.

    Args:
        href (str): Specifies the base URL for all relative URLs in the page.
        target (str): Specifies the default target for all hyperlinks and
            forms in the page.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.

    .. versionchanged:: 0.3.1
        Added URL validation for href attribute.
    """
    def __init__(self, href=None, target=None):
        # TODO: Add in the main api method where it can check that there
        # should be only one base tag in the whole html document.
        self.tag = 'base'
        validate_url(attribute_name='href', url=href)
        self.validate_values(href=href, target=target)
        self.values = {'href': href, 'target': target}

    def construct(self):
        """Returns the constructed base tag <base>."""
        return base_tag.render(self.values)

    def validate_values(self, href, target):
        """Validates the following:
            - Either of href or target attribute value is given.
            - Check whether both href and target attribute values are strings
            or not.
        """
        if not href and not target:
            raise AttributeError('<base>: base tag must have either a href '
                                 'attribute or a target attribute, or both.')

        if target and not isinstance(target, str):
            raise ValueError('<base>: target attribute value should be '
                             'string')
