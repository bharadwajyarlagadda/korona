# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import DD, DL, DT
from korona.templates.html.tags import dd_tag, dl_tag, dt_tag


@parametrize('attributes', [
    ({'text': 'abc'})
])
def test_construct_dd_tag(attributes):
    """Test for validating whether the dd tag is constructed correctly or not.
    """
    dd = DD(**attributes)
    assert dd.construct() == dd_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abc'})
])
def test_construct_dl_tag(attributes):
    """Test for validating whether the dl tag is constructed correctly or not.
    """
    dl = DL(**attributes)
    assert dl.construct() == dl_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abc'})
])
def test_construct_dt_tag(attributes):
    """Test for validating whether the dt tag is constructed correctly or not.
    """
    dt = DT(**attributes)
    assert dt.construct() == dt_tag.render(attributes)
