# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Img
from korona.templates.html.tags import img_tag


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
