# -*- coding: utf-8 -*-
"""Module for constructing <frame> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_attribute_values, validate_url
from ...templates.html.tags import frame

ATTRIBUTES = {
    'frameborder': {
        'description': 'Specifies whether or not to display a border '
                       'around a frame',
        'values': ['0', '1']
    },
    'longdesc': {
        'description': 'Specifies a page that contains a long '
                       'description of the content of a frame',
        'values': None
    },
    'marginheight': {
        'description': 'Specifies the top and bottom margins of a '
                       'frame',
        'values': None
    },
    'marginwidth': {
        'description': 'Specifies the left and right margins of a '
                       'frame',
        'values': None
    },
    'name': {
        'description': 'Specifies the name of a frame',
        'values': None
    },
    'noresize': {
        'description': 'Specifies that a frame is not resizable',
        'values': ['noresize']
    },
    'scrolling': {
        'description': 'Specifies whether or not to display scrollbars'
                       ' in a frame',
        'values': ['yes', 'no', 'auto']
    },
    'src': {
        'description': 'Specifies the URL of the document to show in a'
                       ' frame',
        'values': None
    }
}


class Frame(object):
    """Class for constructing <frame> tag.

    Args:
        frameborder (str): Specifies whether or not to display a border around
            a frame.
        longdesc (str): Specifies a page that contains a long description of
            the content of a frame.
        marginheight (str): Specifies the top and bottom margins of a frame.
        marginwidth (str): Specifies the left and right margins of a frame.
        name (str): Specifies the name of a frame.
        noresize (str): Specifies that a frame is not resizable.
        scrolling (str): Specifies whether or not to display scrollbars in a
            frame.
        src (str): Specifies the URL of the document to show in a frame.

    .. versionadded:: 0.2.0

    .. versionchanged:: 0.3.1
        Added URL validation for src attribute.
    """
    def __init__(self,
                 frameborder=None,
                 longdesc=None,
                 marginheight=None,
                 marginwidth=None,
                 name=None,
                 noresize=None,
                 scrolling=None,
                 src=None):
        self.tag = 'frame'
        validate_attribute_values(
            tag=self.tag,
            attribute_name='frameborder',
            attribute_value=frameborder,
            default_values=ATTRIBUTES['frameborder']['values'])
        validate_attribute_values(
            tag=self.tag,
            attribute_name='noresize',
            attribute_value=noresize,
            default_values=ATTRIBUTES['noresize']['values'])
        validate_attribute_values(
            tag=self.tag,
            attribute_name='scrolling',
            attribute_value=scrolling,
            default_values=ATTRIBUTES['scrolling']['values'])
        validate_url(attribute_name='src', url=src)
        self.values = {'frameborder': frameborder,
                       'longdesc': longdesc,
                       'marginheight': marginheight,
                       'marginwidth': marginwidth,
                       'name': name,
                       'noresize': noresize,
                       'scrolling': scrolling,
                       'src': src}

    def construct(self):
        """Returns the constructed tag <frame>."""
        return frame.render(self.values)
