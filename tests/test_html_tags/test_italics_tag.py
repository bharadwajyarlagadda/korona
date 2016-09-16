# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import I
from korona.templates.html.tags import italics_tag


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_italics_tag(attributes):
    """Test for validating whether the italics tag is constructed correctly or
    not.
    """
    italics = I(**attributes)
    assert italics.construct() == italics_tag.render(attributes)
