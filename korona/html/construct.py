# -*- coding: utf-8 -*-
"""Html Tags construct module.
"""


from __future__ import absolute_import

from ..lib.utils import validate_tag_attribute_value
from .attributes import TAG_ATTRIBUTES
from ..templates.html import (
    anchor_tag,
    abbr_tag,
    acronym_tag,
    area_tag,
    bold_tag,
    base_tag,
    canvas_tag,
    caption_tag,
    cite_tag
)

RECTANGLE_SHAPE_COORDINATES = 4
CIRCLE_SHAPE_COORDINATES = 3


class A(object):
    """Class for constructing anchor tag.

    Args:
        charset (str): Specifies the character-set of a linked document.
        coords (mixed): A list/tuple/string of coordinate values.
        download (str): Specifies that the target will be downloaded when a
            user clicks on the hyper link.
        href (str): Specifies the URL of the page the link goes to.
        hreflang (str): Specifies the language of the linked document.
        name (str): Specifies the name of an anchor.
        rel (str): Specifies the relationship between the current document
            and the linked document.
        rev (str): Specifies the relationship between the linked document and
            the current document.
        shape (str): Specifies the shape of a link.
        target(str): Specifies where to open the linked document.
        type (str): Specifies the media type of the linked document.
        text (str): Anchor tag text. (Ex. <a>text</a>)
    """
    def __init__(self,
                 charset=None,
                 coords=None,
                 download=None,
                 href=None,
                 hreflang=None,
                 name=None,
                 rel=None,
                 rev=None,
                 shape=None,
                 target=None,
                 type=None,
                 text=None):
        self.tag = 'a'

        # Series of validation methods for validating all the attribute values
        # given.
        self.validate_string(value=charset)
        coordinates = self.get_coords(shape=shape, coords=coords)
        self.pre_validate(href=href, attribute_name='download', value=download)
        self.validate_string(value=href)
        self.pre_validate(href=href, attribute_name='hreflang', value=hreflang)
        self.validate_string(value=name)
        self.validate_values(href=href, attribute_name='rel', value=rel)
        self.validate_values(href=href, attribute_name='rev', value=rev)
        self.validate_values(href=href, attribute_name='shape', value=shape)
        self.validate_string(value=target)
        self.pre_validate(href=href, attribute_name='type', value=type)

        # Assign all the values in a dictionary.
        self.values = {'charset': charset,
                       'coords': coordinates,
                       'download': download,
                       'href': href,
                       'hreflang': hreflang,
                       'name': name,
                       'rel': rel,
                       'rev': rev,
                       'shape': shape,
                       'target': target,
                       'type': type,
                       'text': text}

    def construct_tag(self):
        """Returns the constructed anchor tag <a></a>."""
        return anchor_tag.render(self.values)

    def validate_string(self, value):
        """Validates whether the given value is a string or not."""
        if not value:
            return

        # If the attribute value is not a string raise a ValueError.
        if not isinstance(value, str):
            raise ValueError('<a>: {0} should be a string'.format(value))

    def get_coords(self, shape, coords):
        """Returns coordinates after a series of validations.

        Args:
            shape (str): Shape of a link (Ex. rect/circle/poly/etc.)
            coords (mixed): A list/tuple/str of coordinate values.

        Returns:
            str: A string of coordinate values.
        """
        if not coords:
            return

        if (coords and not shape) or (shape and not coords):
            raise AttributeError('<a>: shape attribute should be present when '
                                 'coords are specified.')

        if isinstance(coords, str):
            coords = coords.split(',')

        if isinstance(coords, dict):
            raise ValueError('<a>: {0} should be either list/tuple/str not a '
                             'dictionary'
                             .format(coords))

        if shape == 'rect' and len(coords) != RECTANGLE_SHAPE_COORDINATES:
            raise ValueError('<a>: {0} coordinates should be given for '
                             'rectangle shape'
                             .format(RECTANGLE_SHAPE_COORDINATES))

        if shape == 'circle' and len(coords) != CIRCLE_SHAPE_COORDINATES:
            raise ValueError('<a>: {0} coordinates should be given for '
                             'circle shape'
                             .format(CIRCLE_SHAPE_COORDINATES))

        return ','.join(str(coord) for coord in coords)

    def pre_validate(self, href, attribute_name, value):
        """Validates whether an attribute is dependant on another attribute or
        not. Some of the attributes requires href attribute to be set.
        """
        if not value:
            return

        if not href:
            raise AttributeError('<a>: {0} attribute is only used when '
                                 'href attribute is set.'
                                 .format(attribute_name))

        if not isinstance(value, str):
            raise ValueError('<a>: {0} should be a string'.format(value))

    def validate_values(self, href, attribute_name, value):
        """Validates whether the given attribute value is a valid value or not.
        Some of the attributes have confined values. Even if we give some
        other value, the html output would not be correct.
        """
        if not value:
            return

        if attribute_name == 'rel' and not href:
            raise AttributeError('<a>: {attribute_name} is only used when '
                                 'href attribute is set.'
                                 .format(attribute_name=attribute_name))

        if not isinstance(value, str):
            raise ValueError('<a>: {0} should be a string value.'
                             .format(attribute_name))

        attribute_values = TAG_ATTRIBUTES[self.tag][attribute_name]['values']

        if value not in attribute_values:
            raise AttributeError('<a>: {attribute_name} attribute values '
                                 'should be one of these: {values}'
                                 .format(attribute_name=attribute_name,
                                         values=','.join(attribute_values)))


class Abbr(object):
    """Class for constructing abbr tag.

    Args:
        text (str): Abbr tag text. (Ex. <abbr>text</abbr>)
    """
    def __init__(self, text=None):
        self.tag = 'abbr'
        self.values = {'text': text}

    def construct_tag(self):
        """Returns the constructed abbr tag <abbr></abbr>."""
        return abbr_tag.render(self.values)


class Acronym(object):
    """Class for constructing acronym tag.

    Args:
        text (str): Acronym tag text. (Ex. <acronym>text</acronym>)
    """
    def __init__(self, text=None):
        self.tag = 'acronym'
        self.values = {'text': text}

    def construct_tag(self):
        """Returns the constructed acronym tag <acronym></acronym>."""
        return acronym_tag.render(self.values)


class Area(object):
    """Class for constructing area tag.

    Args:
        alt (str): Specifies an alternate text for the area. Required if the
            href attribute is present.
        coords (mixed): Specifies the coordinates of the area.
        download (str): Specifies that the target will be downloaded when a
            user clicks on the hyper link.
        href (str): Specifies the hyperlink target for the area.
        hreflang (str): Specifies the language of the target URL.
        media (str): Specifies what media/device the target URL is optimized
            for.
        nohref(bool): Specifies that an area has no associated link.
        rel (str): Specifies the relationship between the current document
            and the target URL.
        shape (str): Specifies the shape of the area.
        target(str): Specifies where to open the target URL.
        type (str): Specifies the media type of the target URL.
    """
    def __init__(self,
                 alt=None,
                 coords=None,
                 download=None,
                 href=None,
                 hreflang=None,
                 media=None,
                 nohref=False,
                 rel=None,
                 shape=None,
                 target=None,
                 type=None):
        self.tag = 'area'
        self.validate_alt(href=href, attribute_name='alt', value=alt)
        coordinates = self.get_coords(shape=shape, coords=coords)
        self.pre_validate(href=href, attribute_name='download', value=download)
        self.validate_string(value=href)
        self.pre_validate(href=href, attribute_name='hreflang', value=hreflang)
        self.pre_validate(href=href, attribute_name='media', value=media)
        self.validate_values(href=href, attribute_name='rel', value=rel)
        self.validate_values(href=href, attribute_name='shape', value=shape)
        self.pre_validate(href=href, attribute_name='targte', value=target)
        self.pre_validate(href=href, attribute_name='type', value=type)
        self.values = {'alt': alt,
                       'coords': coordinates,
                       'download': download,
                       'href': href,
                       'hreflang': hreflang,
                       'media': media,
                       'nohref': nohref,
                       'rel': rel,
                       'shape': shape,
                       'target': target,
                       'type': type}

    def construct_tag(self):
        """Returns the constructed area tag <area></area>."""
        return area_tag.render(self.values)

    def validate_string(self, value):
        """Validates whether the given value is a string or not."""
        if not value:
            return

        # If the attribute value is not a string raise a ValueError.
        if not isinstance(value, str):
            raise ValueError('<area>: {0} should be a string'.format(value))

    def validate_alt(self, href, attribute_name, value):
        """Validates area's alt attribute."""
        if href and not value:
            raise AttributeError('<area>: {0} attribute is required if the '
                                 'href attribute is present.'
                                 .format(attribute_name))

        if not href and value:
            raise AttributeError('<area>: {0} attribute is only used when '
                                 'href attribute is set.'
                                 .format(attribute_name))

        if value and not isinstance(value, str):
            raise ValueError('<area>: {0} should be a string'.format(value))

    def pre_validate(self, href, attribute_name, value):
        """Validates whether an attribute is dependant on another attribute or
        not. Some of the attributes requires href attribute to be set.
        """
        if not value:
            return

        if not href:
            raise AttributeError('<area>: {0} attribute is only used when '
                                 'href attribute is set.'
                                 .format(attribute_name))

        if not isinstance(value, str):
            raise ValueError('<area>: {0} should be a string'.format(value))

    def get_coords(self, shape, coords):
        """Returns coordinates after a series of validations.

        Args:
            shape (str): Shape of a link (Ex. rect/circle/poly/etc.)
            coords (mixed): A list/tuple/str of coordinate values.

        Returns:
            str: A string of coordinate values.
        """
        if not coords:
            return

        if (coords and not shape) or (shape and not coords):
            raise AttributeError('<area>: shape attribute should be present '
                                 'when coords are specified.')

        if isinstance(coords, str):
            coords = coords.split(',')

        if isinstance(coords, dict):
            raise ValueError('<area>: {0} should be either list/tuple/str not '
                             'a dictionary'
                             .format(coords))

        if shape == 'rect' and len(coords) != RECTANGLE_SHAPE_COORDINATES:
            raise ValueError('<area>: {0} coordinates should be given for '
                             'rectangle shape'
                             .format(RECTANGLE_SHAPE_COORDINATES))

        if shape == 'circle' and len(coords) != CIRCLE_SHAPE_COORDINATES:
            raise ValueError('<area>: {0} coordinates should be given for '
                             'circle shape'
                             .format(CIRCLE_SHAPE_COORDINATES))

        return ','.join(str(coord) for coord in coords)

    def validate_values(self, href, attribute_name, value):
        """Validates whether the given attribute value is a valid value or not.
        Some of the attributes have confined values. Even if we give some
        other value, the html output would not be correct.
        """
        if not value:
            return

        if attribute_name == 'rel' and not href:
            raise AttributeError('<area>: {attribute_name} is only used when '
                                 'href attribute is set.'
                                 .format(attribute_name=attribute_name))

        if not isinstance(value, str):
            raise ValueError('<area>: {0} should be a string value.'
                             .format(attribute_name))

        attribute_values = TAG_ATTRIBUTES[self.tag][attribute_name]['values']

        if value not in attribute_values:
            raise AttributeError('<area>: {attribute_name} attribute values '
                                 'should be one of these: {values}'
                                 .format(attribute_name=attribute_name,
                                         values=','.join(attribute_values)))


class B(object):
    """Class for constructing bold tag.

    Args:
        text (str): Bold tag text. (Ex. <b>text</b>)
    """
    def __init__(self, text=None):
        self.tag = 'b'
        self.values = {'text': text}

    def construct_tag(self):
        """Returns the constructed bold tag <b></b>."""
        return bold_tag.render(self.values)


class Base(object):
    """Class for constructing base tag.

    Args:
        href (str): Specifies the base URL for all relative URLs in the page.
        target (str): Specifies the default target for all hyperlinks and
            forms in the page.
    """
    def __init__(self, href=None, target=None):
        # TODO: Add in the main api method where it can check that there
        # should be only one base tag in the whole html document.
        self.tag = 'base'
        self.validate_values(href=href, target=target)
        self.values = {'href': href, 'target': target}

    def construct_tag(self):
        """Returns the constructed base tag <base>."""
        return base_tag.render(self.values)

    def validate_values(self, href, target):
        """Validates the following:
            - Either of href or target attribute value is given.
            - CHeck whether both href and target attribute values are strings
                or not.
        """
        if not href and not target:
            raise AttributeError('<base>: base tag must have either a href '
                                 'attribute or a target attribute, or both.')

        if href and not isinstance(href, str):
            raise ValueError('<base>: href attribute value should be string')

        if target and not isinstance(target, str):
            raise ValueError('<base>: target attribute value should be '
                             'string')


class Canvas(object):
    """Class for constructing canvas tag.

    Args:
        height (str): Specifies the height of the canvas.
        width (str): Specifies the width of the canvas.
    """
    def __init__(self, height=None, width=None):
        # TODO: Possible add the canvas text attribute.
        self.tag = 'canvas'
        validate_tag_attribute_value(tag=self.tag, value=height)
        validate_tag_attribute_value(tag=self.tag, value=width)
        self.values = {'height': height, 'width': width}

    def construct_tag(self):
        """Returns the constructed canvas tag <canvas>."""
        return canvas_tag.render(self.values)


class Caption(object):
    """Class for constructing caption tag.

    Args:
        align (str): Defines the alignment of the caption.
        text (str): Specifies the caption text.
    """
    def __init__(self, align=None, text=None):
        self.tag = 'caption'
        self.validate_values(attribute_name='align', value=align)
        self.values = {'align': align, 'text': text}

    def construct_tag(self):
        """Returns the constructed caption tag <caption>."""
        return caption_tag.render(self.values)

    def validate_values(self, attribute_name, value):
        """Validates whether the given attribute value is a valid value or not.
        Some of the attributes have confined values. Even if we give some
        other value, the html output would not be correct.
        """
        if not value:
            return

        if not isinstance(value, str):
            raise ValueError('<caption>: {0} should be a string value.'
                             .format(attribute_name))

        attribute_values = TAG_ATTRIBUTES[self.tag][attribute_name]['values']

        if value not in attribute_values:
            raise AttributeError('<caption>: {attribute_name} attribute '
                                 'values should be one of these: {values}'
                                 .format(attribute_name=attribute_name,
                                         values=','.join(attribute_values)))


class Cite(object):
    """Class for constructing cite tag.

    Args:
        text (str): Specifies the citation text.
    """
    def __init__(self, text):
        self.tag = 'cite'
        self.values = {'text': text}

    def construct_tag(self):
        """Returns the constructed cite tag <cite>."""
        return cite_tag.render(self.values)
