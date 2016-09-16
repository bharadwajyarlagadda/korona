
from ..fixtures import parametrize

from korona.html.tags import Del
from korona.templates.html.tags import del_tag


@parametrize('attributes', [
    ({'cite': 'www.abcd.com'}),
    ({'datetime': '2014-11-15T22:55:03Z'}),
    ({'datetime': '2015-11-15T22:55:03Z', 'text': 'abcd'})
])
def test_construct_del_tag(attributes):
    """Test for validating whether the del tag is constructed correctly or not.
    """
    del_ = Del(**attributes)
    assert del_.construct() == del_tag.render(attributes)
