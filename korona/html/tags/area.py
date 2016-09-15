# -*- coding: utf-8 -*-
"""Module for constructing <area> tag."""

from ..root.attributes import TAG_ATTRIBUTES

from ...lib.utils import validate_url

from ...templates.html.tags import area_tag

RECTANGLE_SHAPE_COORDINATES = 4
CIRCLE_SHAPE_COORDINATES = 3


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

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.

    .. versionchanged:: 0.3.1
        Added URL validation for href attribute.
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
        validate_url(attribute_name='href', url=href)
        self.pre_validate(href=href, attribute_name='hreflang', value=hreflang)
        self.pre_validate(href=href, attribute_name='media', value=media)
        self.validate_values(href=href, attribute_name='rel', value=rel)
        self.validate_values(href=href, attribute_name='shape', value=shape)
        self.pre_validate(href=href, attribute_name='target', value=target)
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

    def construct(self):
        """Returns the constructed area tag <area></area>."""
        return area_tag.render(self.values)

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
