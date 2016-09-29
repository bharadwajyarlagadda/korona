# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Canvas
from korona.templates.html.tags import canvas
from korona.exceptions import AttributeValueError


@parametrize('attributes', [
    ({'height': '100'}),
    ({'width': '200'}),
    ({'height': '100', 'width': '200'})
])
def test_construct_canvas_tag(attributes):
    """Test for validating whether the canvas tag is constructed correctly or
    not.
    """
    canvas_ = Canvas(**attributes)
    assert canvas_.construct() == canvas.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'height': 123}, AttributeValueError, 'should be a string'),
    ({'width': 123}, AttributeValueError, 'should be a string'),
    ({'height': None, 'width': 123},
     AttributeValueError,
     'should be a string')
])
def test_construct_canvas_tag_error(attributes, exception, error_msg):
    """Test for validating canvas tag's attributes."""
    with pytest.raises(exception) as exc:
        Canvas(**attributes)

    assert error_msg in str(exc)
