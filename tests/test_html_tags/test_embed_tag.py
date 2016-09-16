# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Embed
from korona.templates.html.tags import embed_tag


@parametrize('attributes', [
    ({'height': '200'}),
    ({'height': '200', 'width': '100'}),
    ({'src': 'helloworld.swf', 'height': '200', 'width': '100'}),
    ({'src': 'helloworld.swf',
      'height': '200',
      'width': '100',
      'type': 'application'})
])
def test_construct_embed_tag(attributes):
    """Test for validating whether the embed tag is constructed correctly or
    not.
    """
    embed = Embed(**attributes)
    assert embed.construct() == embed_tag.render(attributes)
