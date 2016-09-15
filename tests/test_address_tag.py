
from .fixtures import parametrize

from korona.html.tags import Address
from korona.templates.html import address_tag


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None}),
    ({'text': '<p>Hi there</p>'})
])
def test_construct_address_tag(attributes):
    """Test for validating whether the address tag is constructed correctly or
    not.
    """
    address = Address(**attributes)
    assert address.construct() == address_tag.render(attributes)
