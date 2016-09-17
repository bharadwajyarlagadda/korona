# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Abbr
from korona.templates.html.tags import abbr


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None})
])
def test_construct_abbr_tag(attributes):
    """Test for validating whether the abbr tag is constructed correctly or
    not.
    """
    abbreviate = Abbr(**attributes)
    assert abbreviate.construct() == abbr.render(attributes)
