# -*- coding: utf-8 -*-
"""Module for constructing anchor <a> tag."""

from __future__ import absolute_import

from ..root.attributes import TAG_ATTRIBUTES
from ...lib.utils import validate_tag_attribute_value, validate_url
from ...templates.html.tags import anchor

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

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.

    .. versionchanged:: 0.3.1
        Added URL validation for href attribute.
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
        validate_tag_attribute_value(tag=self.tag, value=charset)
        coordinates = self.get_coords(shape=shape, coords=coords)
        self.pre_validate(href=href, attribute_name='download', value=download)
        validate_url(attribute_name='href', url=href)
        self.pre_validate(href=href, attribute_name='hreflang', value=hreflang)
        self.validate_values(href=href, attribute_name='rel', value=rel)
        self.validate_values(href=href, attribute_name='rev', value=rev)
        self.validate_values(href=href, attribute_name='shape', value=shape)
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

    def construct(self):
        """Returns the constructed anchor tag <a></a>."""
        return anchor.render(self.values)

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
