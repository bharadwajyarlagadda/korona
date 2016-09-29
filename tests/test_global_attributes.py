# -*- coding: utf-8 -*-

import pytest

from .fixtures import parametrize

from korona.html.root.global_attributes import GlobalAttributes
from korona.templates.html.global_attributes import global_attributes
from korona.exceptions import AttributeValueError, TagAttributeError


@parametrize('data', [
    ({'accesskey': 'h'}),
    ({'class': 'class1'}),
    ({'contenteditable': 'true'}),
    ({'contextmenu': 'context'}),
    ({'dir': 'rtl'}),
    ({'draggable': 'true'}),
    ({'dropzone': 'copy'}),
    ({'hidden': True}),
    ({'id': 'global'}),
    ({'lang': 'en'}),
    ({'spellcheck': 'true'}),
    ({'style': 'color:blue;'}),
    ({'tabindex': '4'}),
    ({'title': 'html'}),
    ({'translate': 'yes'})
])
def test_construct_global_attributes(data):
    """Test for validating whether global attributes are constructed correctly
    or not.
    """
    attributes = GlobalAttributes(**data)
    assert attributes.construct() == global_attributes.render(data)


@parametrize('attributes,exception,error_msg', [
    ({'contenteditable': True}, AttributeValueError, 'should be a string'),
    ({'contenteditable': 'temp'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'class': '1class'},
     AttributeValueError,
     'must begin with a letter'),
    ({'dir': 'temp'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'draggable': True}, AttributeValueError, 'should be a string'),
    ({'draggable': 'temp'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'dropzone': 'temp'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'hidden': 'temp'},
     AttributeError,
     'should be a boolean'),
    ({'id': 'temp id'},
     AttributeValueError,
     'id attribute value should not have any spaces'),
    ({'id': '1234'},
     AttributeValueError,
     'id attribute value must contain at least one character'),
    ({'spellcheck': True}, AttributeValueError, 'should be a string'),
    ({'spellcheck': 'temp'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'tabindex': 'temp'},
     AttributeError,
     'should be an integer'),
    ({'translate': 'temp'},
     TagAttributeError,
     'should be one of these')
])
def test_construct_global_attributes_error(attributes, exception, error_msg):
    """Test for validating global attributes."""
    with pytest.raises(exception) as exc:
        GlobalAttributes(**attributes)

    assert error_msg in str(exc)
