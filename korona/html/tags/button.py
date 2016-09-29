# -*- coding: utf-8 -*-
"""Module for constructing <button> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_attribute_values
from ...templates.html.tags import button

ATTRIBUTES = {
    'autofocus': {
        'description': 'Specifies that a button should automatically '
                       'get focus when the page loads',
        'values': None
    },
    'disabled': {
        'description': 'Specifies that a button should be disabled',
        'values': None
    },
    'form': {
        'description': 'Specifies one or more forms the button '
                       'belongs to',
        'values': None
    },
    'formaction': {
        'description': 'Specifies where to send the form-data when a '
                       'form is submitted. Only for type "submit"',
        'values': None
    },
    'formenctype': {
        'description': 'Specifies how form-data should be encoded '
                       'before sending it to a server. Only for '
                       'type "submit"',
        'values': ['application/x-www-form-urlencoded',
                   'multipart/form-data',
                   'text/plain']
    },
    'formmethod': {
        'description': 'Specifies how to send the form-data (which '
                       'HTTP method to use). Only for type "submit"',
        'values': ['get', 'post']
    },
    'formnovalidate': {
        'description': 'Specifies that the form-data should not be '
                       'validated on submission. Only for type '
                       '"submit"',
        'values': None
    },
    'formtarget': {
        'description': 'Specifies where to display the response after '
                       'submitting the form. Only for type "submit"',
        'values': None
    },
    'name': {
        'description': 'Specifies a name for the button',
        'values': None
    },
    'type': {
        'description': 'Specifies the type of button',
        'values': ['button', 'reset', 'submit']
    },
    'value': {
        'descirption': 'Specifies an initial value for the button',
        'values': None
    }
}


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

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.

    .. versionchanged:: 0.4.3-dev
        Removed :func:`validate_values` method.
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
        validate_attribute_values(
            tag=self.tag,
            attribute_name='formenctype',
            attribute_value=formenctype,
            default_values=ATTRIBUTES['formenctype']['values'])
        self.pre_validate(type=type,
                          attribute_name='formmethod',
                          value=formmethod)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='formmethod',
            attribute_value=formmethod,
            default_values=ATTRIBUTES['formmethod']['values'])
        self.pre_validate(type=type,
                          attribute_name='formnovalidate',
                          value=formnovalidate)
        self.pre_validate(type=type,
                          attribute_name='formtarget',
                          value=formtarget)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='type',
                                  attribute_value=type,
                                  default_values=ATTRIBUTES['type']['values'])

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

    def construct(self):
        """Returns the constructed base tag <button>."""
        return button.render(self.values)

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
