# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import HR
from korona.templates.html.tags import hr_tag


@parametrize('attributes', [
    ({'align': 'left', 'width': '50%'}),
    ({'align': 'center', 'size': '100'}),
    ({'noshade': True})
])
def test_construct_hr_tag(attributes):
    """Test for validating whether the hr tag is constructed correctly or not.
    """
    hr = HR(**attributes)
    assert hr.construct() == hr_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'top-right'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_hr_tag_error(attributes, exception, error_msg):
    """Test for validating hr tag's attributes."""
    with pytest.raises(exception) as exc:
        HR(**attributes)

    assert error_msg in str(exc)
