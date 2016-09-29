# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Div
from korona.templates.html.tags import div
from korona.exceptions import TagAttributeError


@parametrize('attributes', [
    ({'align': 'left'}),
    ({'text': 'abcd'}),
    ({'align': 'right', 'text': 'abcd'})
])
def test_construct_div_tag(attributes):
    """Test for validating whether the div tag is constructed correctly or not.
    """
    division = Div(**attributes)
    assert division.construct() == div.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     TagAttributeError,
     'attribute values should be one of these')
])
def test_construct_div_tag_error(attributes, exception, error_msg):
    """Test for validating div tag's attributes."""
    with pytest.raises(exception) as exc:
        Div(**attributes)

    assert error_msg in str(exc)
