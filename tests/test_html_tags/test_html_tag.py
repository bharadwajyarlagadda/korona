# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Html
from korona.templates.html.tags import html_tag


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
