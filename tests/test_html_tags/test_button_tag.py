# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Button
from korona.templates.html.tags import button


@parametrize('attributes', [
    ({'type': 'submit', 'autofocus': True}),
    ({'type': 'submit', 'disabled': True}),
    ({'type': 'submit', 'formnovalidate': True}),
    ({'type': 'submit', 'text': 'HTML'}),
    ({'type': 'submit', 'name': 'HTML', 'value': 'HTML', 'text': 'HTML'}),
    ({'type': 'submit',
      'text': 'HTML',
      'form': 'form1',
      'formaction': 'demo.asp',
      'formmethod': 'post',
      'formtarget': '_blank',
      'formenctype': 'multipart/form-data'})
])
def test_construct_button_tag(attributes):
    """Test for validating whether the button tag is constructed correctly or
    not.
    """
    button_ = Button(**attributes)
    assert button_.construct() == button.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({}, AttributeError, 'Button type should be specified'),
    ({'type': 'reset', 'formaction': 'demo.asp'},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'reset', 'formmethod': 'post'},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'reset', 'formtarget': '_blank'},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'reset', 'formenctype': 'multipart/form-data'},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'reset', 'formnovalidate': True},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'type': 'submit', 'formenctype': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'type': 'submit', 'formmethod': 'abc'},
     AttributeError,
     'attribute values should be one of these'),

])
def test_construct_button_tag_error(attributes, exception, error_msg):
    """Test for validating button tag's attributes."""
    with pytest.raises(exception) as exc:
        Button(**attributes)

    assert error_msg in str(exc)
