# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import FieldSet
from korona.templates.html.tags import fieldset


@parametrize('attributes', [
    ({'disabled': True}),
    ({'form': 'form1'}),
    ({'name': 'name1'}),
    ({'disabled': True, 'form': 'form1', 'name': 'name1'})
])
def test_construct_fieldset_tag(attributes):
    """Test for validating whether the fieldset tag is constructed correctly
    or not.
    """
    fset = FieldSet(**attributes)
    assert fset.construct() == fieldset.render(attributes)
