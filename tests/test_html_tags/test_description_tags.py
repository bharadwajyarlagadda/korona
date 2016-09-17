# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import DD, DL, DT
from korona.templates.html.tags import dd, dl, dt


@parametrize('attributes', [
    ({'text': 'abc'})
])
def test_construct_dd_tag(attributes):
    """Test for validating whether the dd tag is constructed correctly or not.
    """
    dd_ = DD(**attributes)
    assert dd_.construct() == dd.render(attributes)


@parametrize('attributes', [
    ({'text': 'abc'})
])
def test_construct_dl_tag(attributes):
    """Test for validating whether the dl tag is constructed correctly or not.
    """
    dl_ = DL(**attributes)
    assert dl_.construct() == dl.render(attributes)


@parametrize('attributes', [
    ({'text': 'abc'})
])
def test_construct_dt_tag(attributes):
    """Test for validating whether the dt tag is constructed correctly or not.
    """
    dt_ = DT(**attributes)
    assert dt_.construct() == dt.render(attributes)
