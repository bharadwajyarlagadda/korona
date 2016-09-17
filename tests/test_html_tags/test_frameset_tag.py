# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import FrameSet
from korona.templates.html.tags import frameset


@parametrize('attributes', [
    ({'cols': '25%'}),
    ({'rows': '50%'})
])
def test_construct_frameset_tag(attributes):
    """Test for validating whether the frameset tag is constructed correctly or
    not.
    """
    frame_set = FrameSet(**attributes)
    assert frame_set.construct() == frameset.render(attributes)
