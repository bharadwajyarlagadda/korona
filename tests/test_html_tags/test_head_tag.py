# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Head
from korona.templates.html.tags import head_tag


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_head_tag(attributes):
    """Test for validating whether the head tag is constructed correctly or
    not.
    """
    head = Head(**attributes)
    assert head.construct() == head_tag.render(attributes)
