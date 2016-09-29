# -*- coding: utf-8 -*-
"""Module for constructing anchor <a> tag."""

from __future__ import absolute_import

from ...warning import warn
from ...exceptions import TagAttributeError, AttributeValueError

from ..root.global_attributes import GlobalAttributes
from ...lib.utils import (
    validate_url,
    validate_string_attribute,
    validate_attribute_values
)
from ...templates.html.tags import anchor

RECTANGLE_SHAPE_COORDINATES = 4
CIRCLE_SHAPE_COORDINATES = 3
CHARACTER_SETS = ['UTF-8', 'ISO-8859-1']

ATTRIBUTES = {
    'charset': {
        'description': 'Specifies the character-set of a linked '
                       'document.',
        'values': None
    },
    'coords': {
        'description': 'Specifies the coordinates of a link.',
        'values': None
    },
    'download': {
        'description': 'Specifies that the target will be downloaded '
                       'when a user clicks on the hyper link.',
        'values': None
    },
    'href': {
        'descirption': 'Specifies the URL of the page the link goes '
                       'to.',
        'values': None
    },
    'hreflang': {
        'description': 'Specifies the language of the linked '
                       'document.',
        'values': None
    },
    # TODO: Add media attribute.
    'name': {
        'description': 'Specifies the name of an anchor.',
        'values': None
    },
    'rel': {
        'description': 'Specifies the relationship between the current'
                       ' document and the linked document.',
        'values': ['alternate',
                   'author',
                   'bookmark',
                   'help',
                   'license',
                   'next',
                   'nofollow',
                   'noreferrer',
                   'prefetch',
                   'prev',
                   'search',
                   'tag']
    },
    'rev': {
        'description': 'Specifies the relationship between the linked '
                       'document and the current document.',
        'values': ['alternate',
                   'stylesheet',
                   'start',
                   'next',
                   'prev',
                   'contents',
                   'index',
                   'glossary',
                   'copyright',
                   'chapter',
                   'section',
                   'subsection',
                   'appendix',
                   'help',
                   'bookmark',
                   'nofollow']
    },
    'shape': {
        'description': 'Specifies the shape of a link.',
        'values': ['default', 'rect', 'circle', 'poly']
    },
    'target': {
        'description': 'Specifies where to open the linked document.',
        'values': None
    },
    'type': {
        'description': 'Specifies the media type of the linked '
                       'document.',
        'values': None
    }
}


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

    .. versionchanged:: 0.4.3-dev
        Now the user can be displayed with warnings for charset attribute.
        Used custom exceptions for all the attributes. Removed the method
        :func:`validate_values()`.
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

        self.validate_charset(charset)
        coordinates = self.get_coords(shape=shape, coords=coords)
        self.pre_validate(href=href, attribute_name='download', value=download)
        validate_url(attribute_name='download', url=download)
        validate_url(attribute_name='href', url=href)
        self.pre_validate(href=href, attribute_name='hreflang', value=hreflang)
        self.pre_validate(href=href, attribute_name='rel', value=rel)
        validate_string_attribute(tag=self.tag,
                                  attribute_name='rel',
                                  attribute_value=rel)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='rel',
            attribute_value=rel,
            default_values=ATTRIBUTES['rel']['values'])
        validate_string_attribute(tag=self.tag,
                                  attribute_name='rev',
                                  attribute_value=rev)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='rev',
            attribute_value=rev,
            default_values=ATTRIBUTES['rev']['values'])
        validate_string_attribute(tag=self.tag,
                                  attribute_name='shape',
                                  attribute_value=shape)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='shape',
            attribute_value=shape,
            default_values=ATTRIBUTES['shape']['values'])
        self.pre_validate(href=href, attribute_name='type', value=type)

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

    def validate_charset(self, charset):
        """Validates charset attribute. Warn the user showing the common
        character sets used.
        """
        if not charset:
            return

        # If the attribute value is not a string raise a AttributeValueError.
        if not isinstance(charset, str):
            raise AttributeValueError('<{tag}>: {value} should be a string'
                                      .format(tag=self.tag, value=charset))

        if charset.upper() not in CHARACTER_SETS:
            warn('Common character sets used are: {charsets}'
                 .format(charsets=','.join(CHARACTER_SETS)))

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
            raise TagAttributeError('<a>: shape attribute should be present '
                                    'when coords are specified.')

        if isinstance(coords, str):
            coords = coords.split(',')

        if isinstance(coords, dict):
            raise AttributeValueError('<a>: {0} should be either '
                                      'list/tuple/str not a dictionary'
                                      .format(coords))

        if shape == 'rect' and len(coords) != RECTANGLE_SHAPE_COORDINATES:
            raise TagAttributeError('<a>: {0} coordinates should be given for '
                                    'rectangle shape'
                                    .format(RECTANGLE_SHAPE_COORDINATES))

        if shape == 'circle' and len(coords) != CIRCLE_SHAPE_COORDINATES:
            raise TagAttributeError('<a>: {0} coordinates should be given '
                                    'for circle shape'
                                    .format(CIRCLE_SHAPE_COORDINATES))

        return ','.join(str(coord) for coord in coords)

    def pre_validate(self, href, attribute_name, value):
        """Validates whether an attribute is dependant on another attribute or
        not. Some of the attributes requires href attribute to be set.
        """
        if not value:
            return

        if not href:
            raise TagAttributeError('<a>: {attribute_name} attribute is only '
                                    'used when href attribute is set.'
                                    .format(attribute_name=attribute_name))
