# -*- coding: utf-8 -*-

from datetime import date, time

import pytest

from ..fixtures import parametrize

from korona.html.tags import Input
from korona.templates.html.tags import input as tag
from korona.exceptions import TagAttributeError


@parametrize('attributes', [
    # accept attribute
    ({'accept': 'audio/*', 'type': 'file'}),

    # align attribute
    ({'align': 'left', 'type': 'image'}),
    ({'align': 'right', 'type': 'image'}),
    ({'align': 'top', 'type': 'image'}),
    ({'align': 'bottom', 'type': 'image'}),
    ({'align': 'middle', 'type': 'image'}),

    # alt attribute
    ({'alt': 'temp', 'type': 'image'}),

    # autocomplete attribute
    ({'autocomplete': 'on', 'type': 'email'}),
    ({'autocomplete': 'off', 'type': 'password'}),

    # autofocus attribute
    ({'autofocus': True}),

    # checked attribute
    ({'checked': True, 'type': 'radio'}),
    ({'checked': True, 'type': 'checkbox'}),

    # dirname attribute
    ({'name': 'fname', 'dirname': 'fname.dir'}),

    # disabled attribute
    ({'disabled': True}),

    # form attribute
    ({'form': 'form1'}),

    # formaction attribute
    ({'formaction': 'demo.asp', 'type': 'submit'}),
    ({'formaction': 'demo.asp', 'type': 'image'}),

    # formenctype attribute
    ({'formenctype': 'application/x-www-form-urlencoded', 'type': 'submit'}),
    ({'formenctype': 'multipart/form-data', 'type': 'image'}),
    ({'formenctype': 'text/plain', 'type': 'image'}),

    # formmethod attribute
    ({'formmethod': 'get', 'type': 'submit'}),
    ({'formmethod': 'post', 'type': 'image'}),

    # formnovalidate attribute
    ({'formnovalidate': True, 'type': 'submit'}),

    # formtarget attribute
    ({'formtarget': '_parent', 'type': 'submit'}),
    ({'formtarget': '_blank', 'type': 'image'}),

    # height attribute
    ({'height': '200', 'type': 'image'}),

    # list attribute
    ({'list': 'list1'}),

    # max attribute
    ({'max': date.today(), 'type': 'date'}),
    ({'max': '5', 'type': 'number'}),
    ({'max': 5.45, 'type': 'number'}),
    ({'max': '12', 'type': 'month'}),
    ({'max': time(12, 30), 'type': 'time'}),

    # maxlength attribute
    ({'maxlength': '5'}),

    # min attribute
    ({'min': date.today(), 'type': 'date'}),
    ({'min': '5', 'type': 'number'}),
    ({'min': 5.45, 'type': 'number'}),
    ({'min': '12', 'type': 'month'}),
    ({'min': time(12, 30), 'type': 'time'}),

    # multiple attribute
    ({'multiple': True, 'type': 'file'}),
    ({'multiple': True, 'type': 'email'}),

    # name attribute
    ({'name': 'name1'}),

    # pattern attribute
    ({'pattern': '[A-Za-z]{3}', 'type': 'email'}),

    # placeholder attribute
    ({'placeholder': 'Full name', 'type': 'text'}),

    # readonly attribute
    ({'readonly': True}),

    # required attribute
    ({'required': True, 'type': 'search'}),
    ({'required': False, 'type': 'email'}),

    # size attribute
    ({'size': '10', 'type': 'password'}),
    ({'size': 10, 'type': 'email'}),
    ({'size': 10.567, 'type': 'email'}),

    # src attribute
    ({'src': 'demo.asp', 'type': 'image'}),
    ({'src': 'www.google.com/images/a.jpeg', 'type': 'image'}),

    # step attribute
    ({'step': 1, 'type': 'range'}),
    ({'step': 1.56, 'type': 'range'}),

    # type attribute
    ({'type': 'submit'}),

    # value attribute
    ({'value': 'value1'}),

    # width attribute
    ({'width': '100', 'type': 'image'}),
    ({'width': 100, 'type': 'image'}),
    ({'width': 125.50, 'type': 'image'})
])
def test_construct_input_tag(attributes):
    """Test for validating whether the input tag is constructed correctly or
    not.
    """
    input = Input(**attributes)
    assert input.construct() == tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    # accept attribute
    ({'accept': 'audio/*'},
     AttributeError,
     'can only be used with <input type="file"'),
    ({'accept': 'audio/*', 'type': 'submit'},
     AttributeError,
     'can only be used with <input type="file"'),

    # align attribute
    ({'align': 'abcd', 'type': 'image'},
     TagAttributeError,
     'align attribute values should be one of these:'),
    ({'align': 'top'},
     AttributeError,
     'align attribute is only used with <input type="image">'),

    # alt attribute
    ({'alt': 'temp'},
     AttributeError,
     'can only be used with <input type="image">'),
    ({'alt': 'temp', 'type': 'submit'},
     AttributeError,
     'can only be used with <input type="image">'),

    # autocomplete attribute
    ({'autocomplete': 'off', 'type': 'submit'},
     AttributeError,
     'autocomplete attribute works with the following <input> types:'),
    ({'autocomplete': 'n/a', 'type': 'email'},
     TagAttributeError,
     'autocomplete attribute values should be one of these:'),
    ({'autocomplete': 'on'},
     AttributeError,
     'autocomplete attribute works with the following <input> types:'),

    # autofocus attribute
    ({'autofocus': 'temp'},
     AttributeError,
     'autofocus attribute should be a boolean value'),

    # checked attribute
    ({'checked': True, 'type': 'email'},
     AttributeError,
     'checked attribute can be used with'),
    ({'checked': 'temp', 'type': 'radio'},
     AttributeError,
     'checked attribute should be a boolean value'),
    ({'checked': True},
     AttributeError,
     'checked attribute can be used with'),

    # dirname attribute
    ({'dirname': 'fname.dir'},
     AttributeError,
     "The dirname attribute's value is always the name of the input field, "
     "followed by '.dir'"),
    ({'name': 'lname', 'dirname': 'fname.dir'},
     AttributeError,
     "The dirname attribute's value is always the name of the input field, "
     "followed by '.dir'"),

    # disabled attribute
    ({'disabled': 'temp'},
     AttributeError,
     'disabled attribute should be a boolean value'),

    # formaction attribute
    ({'formaction': 'demo.asp', 'type': 'email'},
     AttributeError,
     'formaction attribute is used with type'),
    ({'formaction': 'demo.asp'},
     AttributeError,
     'formaction attribute is used with type'),
    ({'formaction': 123, 'type': 'submit'},
     ValueError,
     'is not a valid url'),

    # formenctype attribute
    ({'formenctype': 'temp', 'type': 'submit'},
     TagAttributeError,
     'formenctype attribute values should be one of these'),
    ({'formenctype': 'text/plain', 'type': 'email'},
     AttributeError,
     'formenctype attribute is used with type'),
    ({'formenctype': 'text/plain'},
     AttributeError,
     'formenctype attribute is used with type'),

    # formmethod attribute
    ({'formmethod': 'get', 'type': 'email'},
     AttributeError,
     'formmethod attribute can be used with type'),
    ({'formmethod': 'get'},
     AttributeError,
     'formmethod attribute can be used with type'),
    ({'formmethod': 'PUT', 'type': 'submit'},
     TagAttributeError,
     'formmethod attribute values should be one of these'),

    # formnovalidate attribute
    ({'formnovalidate': True, 'type': 'email'},
     AttributeError,
     'formnovalidate attribute can be used with type'),
    ({'formnovalidate': True},
     AttributeError,
     'formnovalidate attribute can be used with type'),
    ({'formnovalidate': 'temp', 'type': 'submit'},
     AttributeError,
     'formnovalidate attribute should be a boolean value'),

    # formtarget attribute
    ({'formtarget': '_parent', 'type': 'emali'},
     AttributeError,
     'formtarget attribute can be used with type'),
    ({'formtarget': '_balnk'},
     AttributeError,
     'formtarget attribute can be used with type'),

    # height attribute
    ({'height': '200', 'type': 'submit'},
     AttributeError,
     'height attribute is used only with'),
    ({'height': '200'},
     AttributeError,
     'height attribute is used only with'),
    ({'height': 'temp', 'type': 'image'},
     AttributeError,
     'height attribute should be an integer or float value'),

    # max attribute
    ({'max': date.today(), 'type': 'submit'},
     AttributeError,
     'max attribute works with the following'),
    ({'max': date.today()},
     AttributeError,
     'max attribute works with the following'),
    ({'max': date.today(), 'type': 'number'},
     AttributeError,
     'attribute should be an integer or float value'),
    ({'max': '5', 'type': 'date'},
     AttributeError,
     'attribute should be a date/datetime value'),
    ({'max': '5', 'type': 'time'},
     AttributeError,
     'attribute should be a time value'),

    # maxlength attribute
    ({'maxlength': 'temp'},
     AttributeError,
     'attribute should be an integer or float value'),

    # min attribute
    ({'min': date.today(), 'type': 'submit'},
     AttributeError,
     'min attribute works with the following'),
    ({'min': date.today()},
     AttributeError,
     'min attribute works with the following'),
    ({'min': date.today(), 'type': 'number'},
     AttributeError,
     'attribute should be an integer or float value'),
    ({'min': '5', 'type': 'date'},
     AttributeError,
     'attribute should be a date/datetime value'),
    ({'min': '5', 'type': 'time'},
     AttributeError,
     'attribute should be a time value'),

    # multiple attribute
    ({'multiple': True, 'type': 'submit'},
     AttributeError,
     'multiple attribute works with the following'),

    # pattern attribute
    ({'pattern': '[A-Za-z]{3}', 'type': 'submit'},
     AttributeError,
     'pattern attribute works with the following'),
    ({'pattern': '[A-Za-z]{3}'},
     AttributeError,
     'pattern attribute works with the following'),

    # placeholder attribute
    ({'placeholder': 'Full name', 'type': 'submit'},
     AttributeError,
     'placeholder attribute works with the following'),
    ({'placeholder': 'Full name'},
     AttributeError,
     'placeholder attribute works with the following'),

    # readonly attribute
    ({'readonly': 'temp'},
     AttributeError,
     'should be a boolean'),

    # required attribute
    ({'required': True, 'type': 'submit'},
     AttributeError,
     'required attribute works with the following'),
    ({'required': True},
     AttributeError,
     'required attribute works with the following'),
    ({'required': 'temp', 'type': 'email'},
     AttributeError,
     'should be a boolean'),

    # size attribute
    ({'size': '10', 'type': 'submit'},
     AttributeError,
     'size attribute works with the following'),
    ({'size': '10'},
     AttributeError,
     'size attribute works with the following'),
    ({'size': 'temp', 'type': 'email'},
     AttributeError,
     'should be an integer or float value'),

    # src attribute
    ({'src': 'demo.asp', 'type': 'submit'},
     AttributeError,
     'src attribute is required for'),
    ({'src': 'demo.asp'},
     AttributeError,
     'src attribute is required for'),

    # step attribute
    ({'step': 1, 'type': 'submit'},
     AttributeError,
     'step attribute works with the following'),
    ({'step': 1},
     AttributeError,
     'step attribute works with the following'),
    ({'step': 'temp', 'type': 'range'},
     AttributeError,
     'should be an integer or float value'),

    # type attribute
    ({'type': 'temp'},
     TagAttributeError,
     'type attribute values should be one of these'),

    # value attribute
    ({'value': 'value1', 'type': 'file'},
     AttributeError,
     'value attribute cannot be used with'),

    # width attribute
    ({'width': '100', 'type': 'submit'},
     AttributeError,
     'width attribute is used only with'),
    ({'width': '100'},
     AttributeError,
     'width attribute is used only with'),
    ({'width': 'temp', 'type': 'image'},
     AttributeError,
     'should be an integer or float value')
])
def test_construct_input_tag_error(attributes, exception, error_msg):
    """Test for validating input tag's attributes."""
    with pytest.raises(exception) as exc:
        Input(**attributes)

    assert error_msg in str(exc)
