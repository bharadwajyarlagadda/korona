# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import H1, H2, H3, H4, H5, H6
from korona.templates.html.tags import h1, h2, h3, h4, h5, h6


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h1_tag(attributes):
    """Test for validating whether the h1 tag is constructed correctly or not.
    """
    h1_ = H1(**attributes)
    assert h1_.construct() == h1.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h1_tag_error(attributes, exception, error_msg):
    """Test for validating h1 tag's attributes."""
    with pytest.raises(exception) as exc:
        H1(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h2_tag(attributes):
    """Test for validating whether the h2 tag is constructed correctly or not.
    """
    h2_ = H2(**attributes)
    assert h2_.construct() == h2.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h2_tag_error(attributes, exception, error_msg):
    """Test for validating h2 tag's attributes."""
    with pytest.raises(exception) as exc:
        H2(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h3_tag(attributes):
    """Test for validating whether the h3 tag is constructed correctly or not.
    """
    h3_ = H3(**attributes)
    assert h3_.construct() == h3.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h3_tag_error(attributes, exception, error_msg):
    """Test for validating h3 tag's attributes."""
    with pytest.raises(exception) as exc:
        H3(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h4_tag(attributes):
    """Test for validating whether the h4 tag is constructed correctly or not.
    """
    h4_ = H4(**attributes)
    assert h4_.construct() == h4.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h4_tag_error(attributes, exception, error_msg):
    """Test for validating h4 tag's attributes."""
    with pytest.raises(exception) as exc:
        H4(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h5_tag(attributes):
    """Test for validating whether the h5 tag is constructed correctly or not.
    """
    h5_ = H5(**attributes)
    assert h5_.construct() == h5.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h5_tag_error(attributes, exception, error_msg):
    """Test for validating h5 tag's attributes."""
    with pytest.raises(exception) as exc:
        H5(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h6_tag(attributes):
    """Test for validating whether the h6 tag is constructed correctly or not.
    """
    h6_ = H6(**attributes)
    assert h6_.construct() == h6.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h6_tag_error(attributes, exception, error_msg):
    """Test for validating h6 tag's attributes."""
    with pytest.raises(exception) as exc:
        H6(**attributes)

    assert error_msg in str(exc)
