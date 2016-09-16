# -*- coding: utf-8 -*-
"""Module for constructing Html Tags."""


from __future__ import absolute_import

from ..lib.utils import (
    validate_attribute_values,
    validate_url
)

from ..templates.html import (
    iframe_tag,
    img_tag
)


class IFrame(object):
    """Class for constructing <iframe> tag.

    Args:
        align (str): Specifies the alignment of an <iframe> according to
            surrounding elements.
        frameborder (str): Specifies whether or not to display a border around
            an <iframe>.
        height (str): Specifies the height of an <iframe>.
        longdesc (str): Specifies a page that contains a long description of
            the content of an <iframe>.
        marginheight (str): Specifies the top and bottom margins of the
            content of an <iframe>.
        marginwidth (str): Specifies the left and right margins of the content
            of an <iframe>.
        name (str): Specifies the name of an <iframe>.
        sandbox (str): Enables an extra set of restrictions for the content in
            an <iframe>.
        scrolling (str): Specifies whether or not to display scrollbars in an
            <iframe>.
        src (str): Specifies the address of the document to embed in the
            <iframe>.
        srcdoc (str): Specifies the HTML content of the page to show in the
            <iframe>.
        width (str): Specifies the width of an <iframe>.

    .. versionadded:: 0.4.0-dev
    """
    def __init__(self,
                 align=None,
                 frameborder=None,
                 height=None,
                 longdesc=None,
                 marginheight=None,
                 marginwidth=None,
                 name=None,
                 sandbox=None,
                 scrolling=None,
                 src=None,
                 srcdoc=None,
                 width=None):
        self.tag = 'iframe'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='frameborder',
                                  value=frameborder)
        validate_url(attribute_name='longdesc', url=longdesc)
        self.validate_sandbox(sandbox=sandbox)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='scrolling',
                                  value=scrolling)
        validate_url(attribute_name='src', url=src)
        self.values = {'align': align,
                       'frameborder': frameborder,
                       'height': height,
                       'longdesc': longdesc,
                       'marginheight': marginheight,
                       'marginwidth': marginwidth,
                       'name': name,
                       'sandbox': sandbox,
                       'scrolling': scrolling,
                       'src': src,
                       'srcdoc': srcdoc,
                       'width': width}

    def construct(self):
        """Returns the constructed iframe tag <iframe>."""
        return iframe_tag.render(self.values)

    def validate_sandbox(self, sandbox):
        """Validates sandbox attribute. The value of the sandbox attribute
        can either be just sandbox (then all restrictions are applied), or a
        space-separated list of pre-defined values that will REMOVE the
        particular restrictions.
        """
        if not sandbox:
            return

        parts = sandbox.split(' ')

        for part in parts:
            validate_attribute_values(tag=self.tag,
                                      attribute_name='sandbox',
                                      value=part)


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

    .. versionadded:: 0.4.0-dev
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
        return img_tag.render(self.values)
