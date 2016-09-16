# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Header
from korona.templates.html.tags import header_tag


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_header_tag(attributes):
    """Test for validating whether the header tag is constructed correctly or
    not.
    """
    header = Header(**attributes)
    assert header.construct() == header_tag.render(attributes)
