# -*- coding: utf-8 -*-

import pytest

from .fixtures import parametrize

from korona.lib.utils import validate_tag


@parametrize('tag,error,error_msg', [
    ('htmle', ValueError, 'tag is not supported'),
    (None, AttributeError, 'Tag cannot be empty')
])
def test_validate_invalid_tags(tag, error, error_msg):
    """Test for validating the error for given invalid tags."""
    with pytest.raises(error) as exc:
        validate_tag(tag)

    assert error_msg in str(exc)
