# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Details
from korona.templates.html.tags import details


@parametrize('attributes', [
    ({'open': True}),
    ({'text': 'abcd'}),
    ({'open': True, 'text': 'abcd'})
])
def test_construct_details_tag(attributes):
    """Test for validating whether the details tag is constructed correctly or
    not.
    """
    details_ = Details(**attributes)
    assert details_.construct() == details.render(attributes)
