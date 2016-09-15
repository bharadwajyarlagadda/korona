# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import ColGroup
from korona.templates.html.tags import colgroup_tag


@parametrize('attributes', [
    ({'align': 'char'}),
    ({'align': 'char', 'char': '.'}),
    ({'align': 'char', 'char': '.', 'charoff': '2'}),
    ({'align': 'left', 'span': '2'}),
    ({'align': 'right', 'valign': 'top'}),
    ({'width': '130'})
])
def test_construct_colgroup_tag(attributes):
    """Test for validating whether the colgroup tag is constructed correctly or
    not.
    """
    colgroup = ColGroup(**attributes)
    assert colgroup.construct() == colgroup_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'char': '.'}, AttributeError, 'The char attribute can only be used'),
    ({'charoff': '2'}, AttributeError, 'The charoff attribute can only be'),
    ({'char': '.', 'charoff': '2'},
     AttributeError,
     'The char attribute can only be used'),
    ({'align': 'left', 'charoff': '2'},
     AttributeError,
     'The charoff attribute can only be')
])
def test_construct_colgroup_tag_error(attributes, exception, error_msg):
    """Test for validating colgroup tag's attributes."""
    with pytest.raises(exception) as exc:
        ColGroup(**attributes)

    assert error_msg in str(exc)
