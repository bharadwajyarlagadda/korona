# -*- coding: utf-8 -*-

import pytest

from korona.html.construct import (
    HR,
    Html,
    I,
    IFrame,
    Img
)
from korona.templates.html import (
    hr_tag,
    html_tag,
    italics_tag,
    iframe_tag,
    img_tag
)
from korona.lib.utils import validate_tag

from .fixtures import parametrize


@parametrize('tag,error,error_msg', [
    ('htmle', ValueError, 'tag is not supported'),
    (None, AttributeError, 'Tag cannot be empty')
])
def test_validate_invalid_tags(tag, error, error_msg):
    """Test for validating the error for given invalid tags."""
    with pytest.raises(error) as exc:
        validate_tag(tag)

    assert error_msg in str(exc)


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


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'xmlns': 'www.w3.org', 'text': 'abcd'}),
    ({'manifest': 'demo.appcache', 'text': 'abcd'})
])
def test_construct_html_tag(attributes):
    """Test for validating whether the html tag is constructed correctly or
    not.
    """
    html = Html(**attributes)
    assert html.construct() == html_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'manifest': 12},
     ValueError,
     'is not a valid url.')
])
def test_construct_html_tag_error(attributes, exception, error_msg):
    """Test for validating html tag's attributes."""
    with pytest.raises(exception) as exc:
        Html(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_italics_tag(attributes):
    """Test for validating whether the italics tag is constructed correctly or
    not.
    """
    italics = I(**attributes)
    assert italics.construct() == italics_tag.render(attributes)


@parametrize('attributes', [
    ({'align': 'left', 'frameborder': '1'}),
    ({'src': '/demo.asp', 'height': '100', 'width': '200'}),
    ({'longdesc': 'demo.txt'}),
    ({'marginheight': '50', 'marginwidth': '50', 'name': 'example'}),
    ({'sandbox': 'allow-forms allow-scripts', 'scrolling': 'yes'}),
    ({'srcdoc': '<p>hello</p>'})
])
def test_construct_iframe_tag(attributes):
    """Test for validating whether the iframe tag is constructed correctly or
    not.
    """
    iframe = IFrame(**attributes)
    assert iframe.construct() == iframe_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'frameborder': '4'},
     AttributeError,
     'attribute values should be one of these'),
    ({'align': 'left-center'},
     AttributeError,
     'attribute values should be one of these'),
    ({'sandbox': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'sandbox': 'allow-forms abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'scrolling': 'mount'},
     AttributeError,
     'attribute values should be one of these'),
    ({'sandbox': 'allow-forms allow-pointer-lock abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'longdesc': 123}, ValueError, 'is not a valid url'),
    ({'src': 123}, ValueError, 'is not a valid url')
])
def test_construct_iframe_tag_error(attributes, exception, error_msg):
    """Test for validating iframe tag's attributes."""
    with pytest.raises(exception) as exc:
        IFrame(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'align': 'left', 'alt': 'Smiley text', 'border': '4'}),
    ({'crossorigin': 'anonymous'}),
    ({'height': '30', 'width': '30', 'hspace': '20', 'vspace': '20'}),
    ({'ismap': True}),
    ({'longdesc': 'explained', 'src': '/demo.asp', 'usemap': 'planets'})
])
def test_construct_img_tag(attributes):
    """Test for validating whether the img tag is constructed correctly or not.
    """
    img = Img(**attributes)
    assert img.construct() == img_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'left-top'},
     AttributeError,
     'attribute values should be one of these'),
    ({'longdesc': 123}, ValueError, 'is not a valid url'),
    ({'src': 123}, ValueError, 'is not a valid url')
])
def test_construct_img_tag_error(attributes, exception, error_msg):
    """Test for validating img tag's attributes."""
    with pytest.raises(exception) as exc:
        Img(**attributes)

    assert error_msg in str(exc)
