# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Dialog
from korona.templates.html.tags import dialog


@parametrize('attributes', [
    ({'open': True}),
    ({'text': 'abcd'}),
    ({'open': True, 'text': 'abcd'})
])
def test_construct_dialog_tag(attributes):
    """Test for validating whether the dialog tag is constructed correctly or
    not.
    """
    dialog_ = Dialog(**attributes)
    assert dialog_.construct() == dialog.render(attributes)
