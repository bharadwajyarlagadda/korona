# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import B
from korona.templates.html.tags import bold


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None})
])
def test_construct_bold_tag(attributes):
    """Test for validating whether the bold tag is constructed correctly or
    not.
    """
    bold_ = B(**attributes)
    assert bold_.construct() == bold.render(attributes)
