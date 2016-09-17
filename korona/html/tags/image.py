# -*- coding: utf-8 -*-
"""Module for constructing <img> tag."""


from __future__ import absolute_import

from ...lib.utils import validate_attribute_values, validate_url
from ...templates.html.tags import img


class Img(object):
    """Class for constructing <img> tag.

    Args:
        align (str): Specifies the alignment of an image according to
            surrounding elements.
        alt (str): Specifies an alternate text for an image.
        border (str): Specifies the width of the border around an image.
        crossorigin (str): Allow images from third-party sites that allow
            cross-origin access to be used with canvas.
        height (str): Specifies the height of an image.
        hspace (str): Specifies the whitespace on left and right side of an
            image.
        ismap (bool): Specifies an image as a server-side image-map.
        longdesc (str): Specifies a URL to a detailed description of an image.
        src (str): Specifies the URL of an image.
        usemap (str): Specifies an image as a client-side image-map.
        vspace (str): Specifies the whitespace on top and bottom of an image.
        width (str): Specifies the width of an image.

    .. versionadded:: 0.4.0
    """
    def __init__(self,
                 align=None,
                 alt=None,
                 border=None,
                 crossorigin=None,
                 height=None,
                 hspace=None,
                 ismap=False,
                 longdesc=None,
                 src=None,
                 usemap=None,
                 vspace=None,
                 width=None):
        self.tag = 'img'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        # TODO: Add validation for ismap attribute.
        validate_url(attribute_name='longdesc', url=longdesc)
        validate_url(attribute_name='src', url=src)
        # TODO: Add validation for usemap attribute.
        self.values = {'align': align,
                       'alt': alt,
                       'border': border,
                       'crossorigin': crossorigin,
                       'height': height,
                       'hspace': hspace,
                       'ismap': ismap,
                       'longdesc': longdesc,
                       'src': src,
                       'usemap': usemap,
                       'vspace': vspace,
                       'width': width}

    def construct(self):
        """Returns the constructed image tag <img>."""
        return img.render(self.values)
