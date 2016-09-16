# -*- coding: utf-8 -*-

import pytest

from korona.html.construct import (
    Footer,
    Form,
    Frame,
    FrameSet,
    Head,
    Header,
    HR,
    Html,
    I,
    IFrame,
    Img
)
from korona.templates.html import (
    footer_tag,
    form_tag,
    frame_tag,
    frameset_tag,
    head_tag,
    header_tag,
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
    ({'text': 'abcd'})
])
def test_construct_footer_tag(attributes):
    """Test for validating whether the footer tag is constructed correctly or
    not.
    """
    footer = Footer(**attributes)
    assert footer.construct() == footer_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abcd'}),
    ({'action': 'demo.asp',
      'method': 'get',
      'name': 'name1',
      'target': '_top'}),
    ({'novalidate': True}),
    ({'method': 'post', 'enctype': 'text/plain'})
])
def test_construct_form_tag(attributes):
    """Test for validating whether the form tag is constructed correctly or
    not.
    """
    form = Form(**attributes)
    assert form.construct() == form_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'enctype': 'text/plain', 'method': 'get'},
     AttributeError,
     'enctype attribute can be used/set only if method'),
    ({'method': 'post', 'enctype': 'plain'},
     AttributeError,
     'attribute values should be one of these'),
    ({'autocomplete': 'false'},
     AttributeError,
     'attribute values should be one of these'),
    ({'method': 'PUT'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_form_tag_error(attributes, exception, error_msg):
    """Test for validating form tag's attributes."""
    with pytest.raises(exception) as exc:
        Form(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'noresize': 'noresize'}),
    ({'src': 'frame_a.htm', 'scrolling': 'yes'}),
    ({'frameborder': '0'}),
    ({'src': 'frame_a.htm',
      'scrolling': 'auto',
      'marginheight': '250',
      'marginwidth': '100',
      'name': 'name1',
      'longdesc': 'a.txt'})
])
def test_construct_frame_tag(attributes):
    """Test for validating whether the frame tag is constructed correctly or
    not.
    """
    frame = Frame(**attributes)
    assert frame.construct() == frame_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'scrolling': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'noresize': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'frameborder': '2'},
     AttributeError,
     'attribute values should be one of these'),
    ({'src': 123},
     ValueError,
     'is not a valid url')
])
def test_construct_frame_tag_error(attributes, exception, error_msg):
    """Test for validating frame tag's attributes."""
    with pytest.raises(exception) as exc:
        Frame(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'cols': '25%'}),
    ({'rows': '50%'})
])
def test_construct_frameset_tag(attributes):
    """Test for validating whether the frameset tag is constructed correctly or
    not.
    """
    frameset = FrameSet(**attributes)
    assert frameset.construct() == frameset_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_head_tag(attributes):
    """Test for validating whether the head tag is constructed correctly or
    not.
    """
    head = Head(**attributes)
    assert head.construct() == head_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_header_tag(attributes):
    """Test for validating whether the header tag is constructed correctly or
    not.
    """
    header = Header(**attributes)
    assert header.construct() == header_tag.render(attributes)


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
