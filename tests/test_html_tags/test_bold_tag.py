# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import B
from korona.templates.html.tags import bold_tag


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None})
])
def test_construct_bold_tag(attributes):
    """Test for validating whether the bold tag is constructed correctly or
    not.
    """
    bold = B(**attributes)
    assert bold.construct() == bold_tag.render(attributes)
