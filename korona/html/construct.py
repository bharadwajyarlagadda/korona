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
    address_tag,
    area_tag,
    article_tag,
    bold_tag,
    base_tag,
    button_tag,
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
        validate_tag_attribute_value(tag=self.tag, value=charset)
        coordinates = self.get_coords(shape=shape, coords=coords)
        self.pre_validate(href=href, attribute_name='download', value=download)
        # TODO: Validate href link
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

    def construct_tag(self):
        """Returns the constructed anchor tag <a></a>."""
        return anchor_tag.render(self.values)

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


class Address(object):
    """Class for constructing address tag.

    Args:
        text (str): Address tag text. (Ex. <address>text</address>)
    """
    def __init__(self, text=None):
        self.tag = 'address'
        self.values = {'text': text}

    def construct_tag(self):
        """Returns the constructed address tag <address></address>."""
        return address_tag.render(self.values)


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
        # TODO: Add validation for href link
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

    def construct_tag(self):
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


class Article(object):
    """Class for constructing article tag.

    Args:
        text (str): Article tag text. (Ex. <article>text</article>)
    """
    def __init__(self, text=None):
        self.tag = 'article'
        self.values = {'text': text}

    def construct_tag(self):
        """Returns the constructed article tag <article></article>."""
        return article_tag.render(self.values)


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
        # TODO: Add validation for href link.
        self.validate_values(href=href, target=target)
        self.values = {'href': href, 'target': target}

    def construct_tag(self):
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

        if href and not isinstance(href, str):
            raise ValueError('<base>: href attribute value should be string')

        if target and not isinstance(target, str):
            raise ValueError('<base>: target attribute value should be '
                             'string')


class Button(object):
    """Class for constructing button tag.

    Args:
        autofocus (bool): Specifies that a button should automatically get
            focus when the page loads.
        disabled (bool): Specifies that a button should be disabled.
        form (str): Specifies one or more forms the button belongs to.
        formaction (str): Specifies where to send the form-data when a form is
            submitted. Only for type="submit".
        formenctype (str): Specifies how form-data should be encoded before
            sending it to a server. Only for type="submit".
        formmethod (str): Specifies how to send the form-data (which HTTP
            method to use). Only for type="submit".
        formnovalidate (bool): Specifies that the form-data should not be
            validated on submission. Only for type="submit".
        formtarget (str): Specifies where to display the response after
            submitting the form. Only for type="submit".
        name (str): Specifies a name for the button.
        type (str): Specifies the type of button.
        value (str): Specifies an initial value for the button.
    """
    def __init__(self,
                 autofocus=False,
                 disabled=False,
                 form=None,
                 formaction=None,
                 formenctype=None,
                 formmethod=None,
                 formnovalidate=False,
                 formtarget=None,
                 name=None,
                 type=None,
                 value=None,
                 text=None):
        self.tag = 'button'
        self.validate_type(value=type)
        self.pre_validate(type=type,
                          attribute_name='formaction',
                          value=formaction)
        self.pre_validate(type=type,
                          attribute_name='formenctype',
                          value=formenctype)
        self.validate_values(attribute_name='formenctype', value=formenctype)
        self.pre_validate(type=type,
                          attribute_name='formmethod',
                          value=formmethod)
        self.validate_values(attribute_name='formmethod', value=formmethod)
        self.pre_validate(type=type,
                          attribute_name='formnovalidate',
                          value=formnovalidate)
        self.pre_validate(type=type,
                          attribute_name='formtarget',
                          value=formtarget)
        self.validate_values(attribute_name='type', value=type)

        self.values = {'autofocus': autofocus,
                       'disabled': disabled,
                       'form': form,
                       'formaction': formaction,
                       'formenctype': formenctype,
                       'formmethod': formmethod,
                       'formnovalidate': formnovalidate,
                       'formtarget': formtarget,
                       'name': name,
                       'type': type,
                       'value': value,
                       'text': text}

    def construct_tag(self):
        """Returns the constructed base tag <button>."""
        return button_tag.render(self.values)

    def validate_type(self, value):
        """Validate the type attribute for a <button> element. Different
        browsers use different default types for the <button> element.
        """
        if not value:
            raise AttributeError('<button>: Button type should be specified')

    def pre_validate(self, type, attribute_name, value):
        """Validates whether an attribute is dependant on another attribute or
        not. Some of the attributes requires type attribute to be set to
        'submit'.
        """
        if not value:
            return

        if value and type != 'submit':
            raise AttributeError('<button>: The {attribute_name} attribute is '
                                 'only used for buttons with type "submit"'
                                 .format(attribute_name=attribute_name))

    def validate_values(self, attribute_name, value):
        """Validates whether the given attribute value is a valid value or not.
        Some of the attributes have confined values. Even if we give some
        other value, the html output would not be correct.
        """
        if not value:
            return

        attribute_values = TAG_ATTRIBUTES[self.tag][attribute_name]['values']

        if value not in attribute_values:
            raise AttributeError('<button>: {attribute_name} attribute '
                                 'values should be one of these: {values}'
                                 .format(attribute_name=attribute_name,
                                         values=','.join(attribute_values)))


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
