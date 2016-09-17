# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Figure
from korona.templates.html.tags import figure


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_figure_tag(attributes):
    """Test for validating whether the figure tag is constructed correctly or
    not.
    """
    fig = Figure(**attributes)
    assert fig.construct() == figure.render(attributes)
