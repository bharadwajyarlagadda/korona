# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Caption
from korona.templates.html.tags import caption


@parametrize('attributes', [
    ({'align': 'top'}),
    ({'text': 'abcd'}),
    ({'align': 'bottom', 'text': 'abcd'})
])
def test_construct_caption_tag(attributes):
    """Test for validating whether the caption tag is constructed correctly or
    not.
    """
    caption_ = Caption(**attributes)
    assert caption_.construct() == caption.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 123}, ValueError, 'should be a string'),
    ({'align': 'abcd', 'text': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_caption_tag_error(attributes, exception, error_msg):
    """Test for validating caption tag's attributes."""
    with pytest.raises(exception) as exc:
        Caption(**attributes)

    assert error_msg in str(exc)
