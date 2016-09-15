# -*- coding: utf-8 -*-

import pytest

from .fixtures import parametrize

from korona.html.tags import Base
from korona.templates.html.tags import base_tag


@parametrize('attributes', [
    ({'href': 'www.google.com'}),
    ({'target': 'abc'}),
    ({'href': 'www.google.com', 'target': 'abc'})
])
def test_construct_base_tag(attributes):
    """Test for validating whether the base tag is constructed correctly or
    not.
    """
    base = Base(**attributes)
    assert base.construct() == base_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'href': 123}, ValueError, 'is not a valid url'),
    ({'target': 123}, ValueError, 'value should be string'),
    ({'href': None, 'target': None},
     AttributeError,
     'either a href attribute or a target attribute, or both')
])
def test_construct_base_tag_error(attributes, exception, error_msg):
    """Test for validating base tag's attributes."""
    with pytest.raises(exception) as exc:
        Base(**attributes)

    assert error_msg in str(exc)
