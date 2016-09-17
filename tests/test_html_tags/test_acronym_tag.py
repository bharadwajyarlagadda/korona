# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Acronym
from korona.templates.html.tags import acronym


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None})
])
def test_construct_acronym_tag(attributes):
    """Test for validating whether the acronym tag is constructed correctly or
    not.
    """
    acronym_ = Acronym(**attributes)
    assert acronym_.construct() == acronym.render(attributes)
