# -*- coding: utf-8 -*-
"""Module for constructing <button> tag."""

from ..root.attributes import TAG_ATTRIBUTES
from ...templates.html.tags import button_tag


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

    def construct(self):
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
