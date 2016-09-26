# -*- coding: utf-8 -*-
"""Custom exceptions for Korona."""


class KoronaError(Exception):
    """Main exception class for korona package."""
    pass


class TagAttributeError(KoronaError):
    """Exception class for HTML tag attributes. We raise this exception when
    there are errors in the HTML tag attributes while constructing the HTML
    tags.

    The possible errors can be:

      - Some of the attributes will be having confined values. For example, the
        shape attribute in anchor tag has confined values: default, rect,
        circle, poly; and the user can't specify a value outside the confined
        values. Even if the user specifies a different value, the html
        rendered output will not have any effect. So, we restrict the user to
        give only one in the given confined values.
      - Some of the attributes depend on the others. For example, hreflang
        attribute will not have any effect until and unless href attribute is
        specified. So, we restrict the user to specify the href attribute
        before using hreflang attribute.
    """
    pass


class AttributeValueError(KoronaError):
    """Exception class for HTML tag attribute value. We raise this exception
    when there are errors in HTML tag attribute values while constructing the
    HTML tags.

    The possible errors can be:

      - Most of the attributes of HTML tags are strings. But, some of the
        attributes can be integer/float/list/tuple/date/time/etc. This
        exception will be raised when the type of the given value is a
        mismatch with the attribute's type.
    """
    pass
