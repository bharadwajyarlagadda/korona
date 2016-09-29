# -*- coding: utf-8 -*-
"""Module for constructing <input> tag."""


from __future__ import absolute_import

from ...lib.utils import (
    validate_attribute_values,
    validate_boolean_attribute,
    validate_date_attribute,
    validate_time_attribute,
    validate_number_attribute,
    validate_url,
)
from ...templates.html.tags import input

INPUT_TYPES_FOR_ATTRIBUTES = {
    'accept': {
        'types': ['file'],
        'error': 'accept attribute can only be used with <input type="file">'
    },
    'align': {
        'types': ['image'],
        'error': 'align attribute is only used with <input type="image">'
    },
    'alt': {
        'types': ['image'],
        'error': 'alt attribute can only be used with <input type="image">'
    },
    'autocomplete': {
        'types': ['text',
                  'search',
                  'url',
                  'tel',
                  'email',
                  'password',
                  'range',
                  'color'],
        'error': 'autocomplete attribute works with the following <input> '
                 'types: text, search, url, tel, email, password, datepickers,'
                 ' range, and color.'
    },
    'checked': {
        'types': ['checkbox', 'radio'],
        'error': 'checked attribute can be used with <input type="checkbox"> '
                 'and <input type="radio">'
    },
    'formaction': {
        'types': ['submit', 'image'],
        'error': 'formaction attribute is used with type="submit" and '
                 'type="image"'
    },
    'formenctype': {
        'types': ['submit', 'image'],
        'error': 'formenctype attribute is used with type="submit" and '
                 'type="image"'
    },
    'formmethod': {
        'types': ['submit', 'image'],
        'error': 'formmethod attribute can be used with type="submit" and '
                 'type="image"'
    },
    'formnovalidate': {
        'types': ['submit'],
        'error': 'formnovalidate attribute can be used with type="submit"'
    },
    'formtarget': {
        'types': ['submit', 'image'],
        'error': 'formtarget attribute can be used with type="submit" and '
                 'type="image"'
    },
    'height': {
        'types': ['image'],
        'error': 'height attribute is used only with <input type="image">'
    },
    'max': {
        'types': ['number',
                  'range',
                  'date',
                  'datetime',
                  'datetime-local',
                  'month',
                  'time',
                  'week'],
        'error': 'max attribute works with the following input types: number,'
                 ' range, date, datetime, datetime-local, month, time and week'
    },
    'min': {
        'types': ['number',
                  'range',
                  'date',
                  'datetime',
                  'datetime-local',
                  'month',
                  'time',
                  'week'],
        'error': 'min attribute works with the following input types: number,'
                 ' range, date, datetime, datetime-local, month, time and week'
    },
    'multiple': {
        'types': ['email', 'file'],
        'error': 'multiple attribute works with the following input types: '
                 'email, and file'
    },
    'pattern': {
        'types': ['text', 'date', 'search', 'url', 'tel', 'email', 'password'],
        'error': 'pattern attribute works with the following input types: '
                 'text, date, search, url, tel, email, and password'
    },
    'placeholder': {
        'types': ['text', 'search', 'url', 'tel', 'email', 'password'],
        'error': 'placeholder attribute works with the following input types: '
                 'text, search, url, tel, email, and password'
    },
    'required': {
        'types': ['text',
                  'search',
                  'url',
                  'tel',
                  'email',
                  'password',
                  'date pickers',
                  'number',
                  'checkbox',
                  'radio',
                  'file'],
        'error': 'required attribute works with the following input types: '
                 'text, search, url, tel, email, password, date pickers, '
                 'number, checkbox, radio, and file'
    },
    'size': {
        'types': ['text', 'search', 'tel', 'url', 'email', 'password'],
        'error': 'size attribute works with the following input types: text, '
                 'search, tel, url, email, and password'
    },
    'src': {
        'types': ['image'],
        'error': 'src attribute is required for <input type="image">, and can '
                 'only be used with <input type="image">'
    },
    'step': {
        'types': ['number',
                  'range',
                  'date',
                  'datetime',
                  'datetime-local',
                  'month',
                  'time',
                  'week'],
        'error': 'step attribute works with the following input types: number,'
                 ' range, date, datetime, datetime-local, month, time and week'
    },
    'width': {
        'types': ['image'],
        'error': 'width attribute is used only with <input type="image">'
    }
}

ATTRIBUTES = {
    'accept': {
        'description': 'Specifies the types of files that the server '
                       'accepts (only for type="file")',
        'values': None
    },
    'align': {
        'description': 'Specifies the alignment of an image input '
                       '(only for type="image")',
        'values': ['left', 'right', 'top', 'middle', 'bottom']
    },
    'alt': {
        'description': 'Specifies an alternate text for images (only '
                       'for type="image")',
        'values': None
    },
    'autocomplete': {
        'description': 'Specifies whether an <input> element should '
                       'have autocomplete enabled',
        'values': ['on', 'off']
    },
    'autofocus': {
        'description': 'Specifies that an <input> element should '
                       'automatically get focus when the page loads',
        'values': None
    },
    'checked': {
        'description': 'Specifies that an <input> element should be '
                       'pre-selected when the page loads (for '
                       'type="checkbox" or type="radio")',
        'values': None
    },
    'dirname': {
        'description': 'Specifies that the text direction will be '
                       'submitted',
        'values': None
    },
    'disabled': {
        'description': 'Specifies that an <input> element should be '
                       'disabled',
        'values': None
    },
    'form': {
        'description': 'Specifies one or more forms the <input> '
                       'element belongs to',
        'values': None
    },
    'formaction': {
        'description': 'Specifies the URL of the file that will '
                       'process the input control when the form is '
                       'submitted (for type="submit" and '
                       'type="image")',
        'values': None
    },
    'formenctype': {
        'description': 'Specifies how the form-data should be encoded '
                       'when submitting it to the server (for type='
                       '"submit" and type="image")',
        'values': ['application/x-www-form-urlencoded',
                   'multipart/form-data',
                   'text/plain']
    },
    'formmethod': {
        'description': 'Defines the HTTP method for sending data to '
                       'the action URL (for type="submit" and type='
                       '"image")',
        'values': ['get', 'post']
    },
    'formnovalidate': {
        'description': 'Defines that form elements should not be '
                       'validated when submitted',
        'values': None
    },
    'formtarget': {
        'description': 'Specifies where to display the response that '
                       'is received after submitting the form (for '
                       'type="submit" and type="image")',
        'values': None
    },
    'height': {
        'description': 'Specifies the height of an <input> element '
                       '(only for type="image")',
        'values': None
    },
    'list': {
        'description': 'Refers to a <datalist> element that contains '
                       'pre-defined options for an <input> element',
        'values': None
    },
    'max': {
        'description': 'Specifies the maximum value for an <input> '
                       'element',
        'values': None
    },
    'maxlength': {
        'description': 'Specifies the maximum number of characters '
                       'allowed in an <input> element',
        'values': None
    },
    'min': {
        'description': 'Specifies a minimum value for an <input> '
                       'element',
        'values': None
    },
    'multiple': {
        'description': 'Specifies that a user can enter more than one '
                       'value in an <input> element',
        'values': None
    },
    'name': {
        'description': 'Specifies the name of an <input> element',
        'values': None
    },
    'pattern': {
        'description': "Specifies a regular expression that an <input>"
                       " element's value is checked against",
        'values': None
    },
    'placeholder': {
        'description': 'Specifies a short hint that describes the '
                       'expected value of an <input> element',
        'values': None
    },
    'readonly': {
        'description': 'Specifies that an input field is read-only',
        'values': None
    },
    'required': {
        'description': 'Specifies that an input field must be filled '
                       'out before submitting the form',
        'values': None
    },
    'size': {
        'description': 'Specifies the width, in characters, of an '
                       '<input> element',
        'values': None
    },
    'src': {
        'description': 'Specifies the URL of the image to use as a '
                       'submit button (only for type="image")',
        'values': None
    },
    'step': {
        'description': 'Specifies the legal number intervals for an '
                       'input field',
        'values': None
    },
    'type': {
        'description': 'Specifies the type <input> element to display',
        'values': ['button',
                   'checkbox',
                   'color',
                   'date',
                   'datetime',
                   'datetime-local',
                   'email',
                   'file',
                   'hidden',
                   'image',
                   'month',
                   'number',
                   'password',
                   'radio',
                   'range',
                   'reset',
                   'search',
                   'submit',
                   'tel',
                   'text',
                   'time',
                   'url',
                   'week']
    },
    'value': {
        'description': 'Specifies the value of an <input> element',
        'values': None
    },
    'width': {
        'description': 'Specifies the width of an <input> element '
                       '(only for type="image")',
        'values': None
    }
}


class Input(object):
    """Class for constructing <input> tag.

    Args:
        accept(str): Specifies the types of files that the server accepts
            (only for type="file").
        align (str): Specifies the alignment of an image input (only for
            type="image").
        alt (str): Specifies an alternate text for images (only for type=
            "image").
        autocomplete (str): Specifies whether an <input> element should have
            autocomplete enabled.
        autofocus (bool): Specifies that an <input> element should
            automatically get focus when the page loads.
        checked (bool): Specifies that an <input> element should be
            pre-selected when the page loads (for type="checkbox" or
            type="radio").
        dirname (str): Specifies that the text direction will be submitted.
        disabled (bool): Specifies that an <input> element should be disabled.
        form (str): Specifies one or more forms the <input> element belongs to.
        formaction (str): Specifies the URL of the file that will process the
            input control when the form is submitted (for type="submit" and
            type="image").
        formenctype (str): Specifies how the form-data should be encoded when
            submitting it to the server (for type="submit" and type="image").
        formmethod (str): Defines the HTTP method for sending data to the
            action URL (for type="submit" and type="image").
        formnovalidate (bool): Defines that form elements should not be
            validated when submitted.
        formtarget (str): Specifies where to display the response that is
            received after submitting the form (for type="submit" and
            type="image").
        height (int/float): Specifies the height of an <input> element (only
            for type="image").
        list (str): Refers to a <datalist> element that contains pre-defined
            options for an <input> element.
        max (int/date/time): Specifies the maximum value for an <input>
            element.
        maxlength (int): Specifies the maximum number of characters
            allowed in an <input> element.
        min (int/date/time): Specifies a minimum value for an <input> element.
        multiple (bool): Specifies that a user can enter more than one value
            in an <input> element.
        name (str): Specifies the name of an <input> element.
        pattern (str): Specifies a regular expression that an <input>
            element's value is checked against.
        placeholder (str): Specifies a short hint that describes the expected
            value of an <input> element.
        readonly (bool): Specifies that an input field is read-only.
        required (bool): Specifies that an input field must be filled out
            before submitting the form.
        size (int): Specifies the width, in characters, of an <input> element.
        src (str): Specifies the URL of the image to use as a submit button
            (only for type="image").
        step (int): Specifies the legal number intervals for an input field.
        type (str): Specifies the type <input> element to display.
        value (str): Specifies the value of an <input> element.
        width (int/float): Specifies the width of an <input> element (only for
            type="image").

    .. versionadded:: 0.4.2

    .. versionchanged:: 0.4.3-dev
        Renamed the method :func:`validate_value` to
        :func:`validate_value_attribute`.
    """
    def __init__(self,
                 accept=None,
                 align=None,
                 alt=None,
                 autocomplete=None,
                 autofocus=False,
                 checked=False,
                 name=None,
                 dirname=None,
                 disabled=False,
                 form=None,
                 formaction=None,
                 formenctype=None,
                 formmethod=None,
                 formnovalidate=False,
                 formtarget=None,
                 height=None,
                 list=None,
                 max=None,
                 min=None,
                 maxlength=None,
                 multiple=False,
                 pattern=None,
                 placeholder=None,
                 readonly=False,
                 required=False,
                 size=None,
                 src=None,
                 step=None,
                 type=None,
                 value=None,
                 width=None):
        self.tag = 'input'

        # Series of validation methods for all the input tag's attributes.
        # Validation method for 'accept' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='accept',
                                      attribute_value=accept)

        # Validation method for 'align' attribute.
        validate_attribute_values(
            tag=self.tag,
            attribute_name='align',
            attribute_value=align,
            default_values=ATTRIBUTES['align']['values'])
        self.validate_input_attribute(type=type,
                                      attribute_name='align',
                                      attribute_value=align)

        # Validation method for 'alt' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='alt',
                                      attribute_value=alt)

        # Validation methods for 'autocomplete' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='autocomplete',
                                      attribute_value=autocomplete)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='autocomplete',
            attribute_value=autocomplete,
            default_values=ATTRIBUTES['autocomplete']['values'])

        # Validation method for 'autofocus' attribute.
        validate_boolean_attribute(tag=self.tag,
                                   attribute_name='autofocus',
                                   attribute_value=autofocus)

        # Validation method for 'checked' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='checked',
                                      attribute_value=checked)
        validate_boolean_attribute(tag=self.tag,
                                   attribute_name='checked',
                                   attribute_value=checked)

        # Validation method for 'dirname' attribute.
        self.validate_dirname(name=name, dirname=dirname)

        # Validation method for 'disabled' attribute.
        validate_boolean_attribute(tag=self.tag,
                                   attribute_name='disabled',
                                   attribute_value=disabled)

        # Validation method for 'formaction' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='formaction',
                                      attribute_value=formaction)
        validate_url(attribute_name='formaction', url=formaction)

        # Validation method for 'formenctype' attribute.
        validate_attribute_values(
            tag=self.tag,
            attribute_name='formenctype',
            attribute_value=formenctype,
            default_values=ATTRIBUTES['formenctype']['values'])
        self.validate_input_attribute(type=type,
                                      attribute_name='formenctype',
                                      attribute_value=formenctype)

        # Validation methods for 'formmethod' attribute.
        validate_attribute_values(
            tag=self.tag,
            attribute_name='formmethod',
            attribute_value=formmethod,
            default_values=ATTRIBUTES['formmethod']['values'])
        self.validate_input_attribute(type=type,
                                      attribute_name='formmethod',
                                      attribute_value=formmethod)

        # Validation methods for 'formnovalidate' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='formnovalidate',
                                      attribute_value=formnovalidate)
        validate_boolean_attribute(tag=self.tag,
                                   attribute_name='formnovalidate',
                                   attribute_value=formnovalidate)

        # Validation method for 'formtarget' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='formtarget',
                                      attribute_value=formtarget)

        # Validation methods for 'height' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='height',
                                      attribute_value=height)
        validate_number_attribute(tag=self.tag,
                                  attribute_name='height',
                                  attribute_value=height)

        # Validation method for 'max' attribute.
        self.validate_max_min_attributes(type=type,
                                         attribute_name='max',
                                         attribute_value=max)

        # Validation method for 'maxlength' attribute.
        validate_number_attribute(tag=self.tag,
                                  attribute_name='maxlength',
                                  attribute_value=maxlength)

        # Validation method for 'min' attribute.
        self.validate_max_min_attributes(type=type,
                                         attribute_name='min',
                                         attribute_value=min)

        # Validation method for 'multiple' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='multiple',
                                      attribute_value=multiple)

        # Validation method for 'pattern' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='pattern',
                                      attribute_value=pattern)

        # Validation method for 'placeholder' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='placeholder',
                                      attribute_value=placeholder)

        # Validation method for 'readonly' attribute.
        validate_boolean_attribute(tag=self.tag,
                                   attribute_name='readonly',
                                   attribute_value=readonly)

        # Validation method for 'required' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='required',
                                      attribute_value=required)
        validate_boolean_attribute(tag=self.tag,
                                   attribute_name='required',
                                   attribute_value=required)

        # Validation method for 'size' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='size',
                                      attribute_value=size)
        validate_number_attribute(tag=self.tag,
                                  attribute_name='size',
                                  attribute_value=size)

        # Validation method for 'src' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='src',
                                      attribute_value=src)
        validate_url(attribute_name='src', url=src)

        # Validation method for 'step' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='step',
                                      attribute_value=step)
        validate_number_attribute(tag=self.tag,
                                  attribute_name='step',
                                  attribute_value=step)

        # Validation method for 'type' attribute.
        validate_attribute_values(
            tag=self.tag,
            attribute_name='type',
            attribute_value=type,
            default_values=ATTRIBUTES['type']['values'])

        # Validation method for 'value' attribute.
        self.validate_value_attribute(type=type, value=value)

        # Validation method for 'width' attribute.
        self.validate_input_attribute(type=type,
                                      attribute_name='width',
                                      attribute_value=width)
        validate_number_attribute(tag=self.tag,
                                  attribute_name='width',
                                  attribute_value=width)

        self.values = {'accept': accept,
                       'align': align,
                       'alt': alt,
                       'autocomplete': autocomplete,
                       'autofocus': autofocus,
                       'checked': checked,
                       'name': name,
                       'dirname': dirname,
                       'disabled': disabled,
                       'form': form,
                       'formaction': formaction,
                       'formenctype': formenctype,
                       'formmethod': formmethod,
                       'formnovalidate': formnovalidate,
                       'formtarget': formtarget,
                       'height': height,
                       'list': list,
                       'max': max,
                       'min': min,
                       'maxlength': maxlength,
                       'multiple': multiple,
                       'pattern': pattern,
                       'placeholder': placeholder,
                       'readonly': readonly,
                       'required': required,
                       'size': size,
                       'src': src,
                       'step': step,
                       'type': type,
                       'value': value,
                       'width': width}

    def construct(self):
        """Constructs the <input> tag."""
        return input.render(self.values)

    def validate_input_attribute(self, type, attribute_name, attribute_value):
        """Validates input tag attribute. Some of the input attributes depend
        on the input type given by the consumer.

        For example, max and min attributes works with the following input
        types: number, range, date, datetime, datetime-local, month, time and
        week.
        """
        if not attribute_value:
            return

        # Get all the input types for that input attribute without which the
        # attribute wouldn't function properly.
        input_types = INPUT_TYPES_FOR_ATTRIBUTES[attribute_name]['types']

        # Get the error message for that attribute. If the input types are
        # not in the specific list then we throw this error to the user.
        error = INPUT_TYPES_FOR_ATTRIBUTES[attribute_name]['error']

        if attribute_value and not type:
            raise AttributeError('<{tag}>: {error}'
                                 .format(tag=self.tag, error=error))

        if type and type not in input_types and attribute_value:
            raise AttributeError('<{tag}>: {error}'
                                 .format(tag=self.tag, error=error))

    def validate_dirname(self, name, dirname):
        """Validates the dirname attribute for <input> tag. The dirname
        attribute's value should always have the name of the input field,
        followed by ".dir".
        """
        if not dirname:
            return

        if (not name and dirname) or (dirname != '{0}.dir'.format(name)):
            raise AttributeError("<input>: The dirname attribute's value is "
                                 "always the name of the input field, followed"
                                 " by '.dir'.")

    def validate_max_min_attributes(self,
                                    type,
                                    attribute_name,
                                    attribute_value):
        """Validates the max attribute whether it is an integer/float/datetime
        value.
        """
        self.validate_input_attribute(type=type,
                                      attribute_name=attribute_name,
                                      attribute_value=attribute_value)

        # There are 3 cases to be considered as part of this method. max/min
        # attributes can be integer/float/date/time values.
        #
        # Case #1: If the input type is number/range/month/week, then the max
        # attribute value should be an integer/float.
        # Case #2: If the input type is date/datetime/datetime-local, then the
        # max attribute value should be an date/datetime value.
        # Case #3: If the input type is time, then the max attribute value
        # should be a time value.
        if type in ['number', 'range', 'month', 'week']:
            validate_number_attribute(tag=self.tag,
                                      attribute_name=attribute_name,
                                      attribute_value=attribute_value)
        elif type in ['date', 'datetime', 'datetime-local']:
            validate_date_attribute(tag=self.tag,
                                    attribute_name=attribute_name,
                                    attribute_value=attribute_value)
        elif type in ['time']:
            validate_time_attribute(tag=self.tag,
                                    attribute_name=attribute_name,
                                    attribute_value=attribute_value)

    def validate_value_attribute(self, type, value):
        """Validates the value attribute for <input> tag. The value attribute
        cannot be used with <input type="file">.
        """
        if not value:
            return

        if type == 'file' and value:
            raise AttributeError('<input>: value attribute cannot be used with'
                                 ' <input type="file">.')
