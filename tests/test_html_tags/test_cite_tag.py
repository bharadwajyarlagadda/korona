# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Cite
from korona.templates.html.tags import cite


@parametrize('attributes', [
    ({'text': 'abcd'}),
])
def test_construct_cite_tag(attributes):
    """Test for validating whether the citation tag is constructed correctly or
    not.
    """
    cite_ = Cite(**attributes)
    assert cite_.construct() == cite.render(attributes)
