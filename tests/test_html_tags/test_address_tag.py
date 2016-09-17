# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Address
from korona.templates.html.tags import address


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None}),
    ({'text': '<p>Hi there</p>'})
])
def test_construct_address_tag(attributes):
    """Test for validating whether the address tag is constructed correctly or
    not.
    """
    addr = Address(**attributes)
    assert addr.construct() == address.render(attributes)
