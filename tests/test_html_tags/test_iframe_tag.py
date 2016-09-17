# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import IFrame
from korona.templates.html.tags import iframe


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
    iframe_ = IFrame(**attributes)
    assert iframe_.construct() == iframe.render(attributes)


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
