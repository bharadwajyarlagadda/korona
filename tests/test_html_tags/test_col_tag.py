# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Col
from korona.templates.html.tags import col_tag


@parametrize('attributes', [
    ({'align': 'char'}),
    ({'align': 'char', 'char': '.'}),
    ({'align': 'char', 'char': '.', 'charoff': '2'}),
    ({'align': 'left', 'span': '2'}),
    ({'align': 'right', 'valign': 'top'}),
    ({'width': '130'})
])
def test_construct_col_tag(attributes):
    """Test for validating whether the col tag is constructed correctly or
    not.
    """
    col = Col(**attributes)
    assert col.construct() == col_tag.render(attributes)


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
def test_construct_col_tag_error(attributes, exception, error_msg):
    """Test for validating col tag's attributes."""
    with pytest.raises(exception) as exc:
        Col(**attributes)

    assert error_msg in str(exc)
