# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Frame
from korona.templates.html.tags import frame


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
    frame_ = Frame(**attributes)
    assert frame_.construct() == frame.render(attributes)


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
