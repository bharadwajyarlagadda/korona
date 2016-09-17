# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Head
from korona.templates.html.tags import head


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_head_tag(attributes):
    """Test for validating whether the head tag is constructed correctly or
    not.
    """
    head_ = Head(**attributes)
    assert head_.construct() == head.render(attributes)
