# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Footer
from korona.templates.html.tags import footer_tag


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_footer_tag(attributes):
    """Test for validating whether the footer tag is constructed correctly or
    not.
    """
    footer = Footer(**attributes)
    assert footer.construct() == footer_tag.render(attributes)
