# -*- coding: utf-8 -*-

import pytest

from korona.html.construct import (
    A,
    Abbr,
    Acronym,
    B,
    Base
)
from korona.templates.html import (
    anchor_tag,
    abbr_tag,
    acronym_tag,
    bold_tag,
    base_tag
)
from korona.lib.utils import validate_tag

from .fixtures import parametrize


@parametrize('tag,error,error_msg', [
    ('htmle', ValueError, 'tag is not supported'),
    (None, AttributeError, 'Tag cannot be empty')
])
def test_validate_invalid_tags(tag, error, error_msg):
    """Test for validating the error for given invalid tags."""
    with pytest.raises(error) as exc:
        validate_tag(tag)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'href': 'www.google.com'}),
    ({'href': 'www.google.com', 'rel': 'nofollow'}),
    ({'charset': 'utf-8',
      'download': 'abc',
      'href': 'www.google.com',
      'hreflang': 'en',
      'name': 'C4',
      'rel': 'nofollow',
      'rev': 'nofollow',
      'target': '_blank',
      'type': 'text/html'}),
    ({'href': 'www.google.com', 'text': 'google'})
])
def test_construct_anchor_tag(attributes):
    """Test for validating whether the anchor tag is constructed correctly or
    not.
    """
    anchor = A(**attributes)
    assert anchor.construct_tag() == anchor_tag.render(attributes)


@parametrize('attributes', [
    ({'shape': 'rect', 'coords': [1, 2, 3, 4]}),
    ({'shape': 'circle', 'coords': [1, 2, 3]}),
    ({'shape': 'poly', 'coords': [1, 2, 3, 4, 5, 6]}),
    ({'shape': 'rect', 'coords': (1, 2, 3, 4)}),
    ({'shape': 'circle', 'coords': (1, 2, 3)}),
    ({'shape': 'poly', 'coords': (1, 2, 3, 4, 5, 6)}),
    ({'shape': 'rect', 'coords': '1,2,3,4'}),
    ({'shape': 'circle', 'coords': '1,2,3'}),
    ({'shape': 'poly', 'coords': '1,2,3,4,5,6'}),
])
def test_construct_anchor_tag_coords(attributes):
    """Test for validating the shape and coordinate attributes given."""
    anchor = A(**attributes)

    if not isinstance(attributes['coords'], str):
        attributes['coords'] = (','.join(str(coord)
                                         for coord in attributes['coords']))

    assert anchor.construct_tag() == anchor_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'rel': 1}, AttributeError, 'only used when href attribute is set.'),
    ({'charset': 1}, ValueError, 'should be a string'),
    ({'rel': 1, 'href': 'www.google.com'}, ValueError, 'should be a string'),
    ({'shape': 'circle', 'coords': [1, 2, 3, 4]},
     ValueError,
     'coordinates should be given for circle shape'),
    ({'shape': 'rect', 'coords': [1, 2, 3, 4, 5]},
     ValueError,
     'coordinates should be given for rectangle shape'),
    ({'shape': 'circle', 'coords': [1, 2]},
     ValueError,
     'coordinates should be given for circle shape'),
    ({'shape': 'rect', 'coords': [1, 2, 3]},
     ValueError,
     'coordinates should be given for rectangle shape'),
    ({'shape': 'rect', 'coords': {'x': 1, 'y': 2}},
     ValueError,
     'should be either list/tuple/str not a dictionary'),
    ({'coords': [1, 2, 3]},
     AttributeError,
     'shape attribute should be present when coords are specified'),
    ({'download': 'abc'},
     AttributeError,
     'only used when href attribute is set.'),
    ({'href': 'www.google.com', 'rel': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'rev': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'shape': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
])
def test_construct_anchor_tag_error(attributes, exception, error_msg):
    """Test for validating anchor tag's attributes."""
    with pytest.raises(exception) as exc:
        A(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None})
])
def test_construct_abbr_tag(attributes):
    """Test for validating whether the abbr tag is constructed correctly or
    not.
    """
    abbr = Abbr(**attributes)
    assert abbr.construct_tag() == abbr_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None})
])
def test_construct_acronym_tag(attributes):
    """Test for validating whether the acronym tag is constructed correctly or
    not.
    """
    acronym = Acronym(**attributes)
    assert acronym.construct_tag() == acronym_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None})
])
def test_construct_bold_tag(attributes):
    """Test for validating whether the bold tag is constructed correctly or
    not.
    """
    bold = B(**attributes)
    assert bold.construct_tag() == bold_tag.render(attributes)


@parametrize('attributes', [
    ({'href': 'www.google.com'}),
    ({'target': 'abc'}),
    ({'href': 'www.google.com', 'target': 'abc'})
])
def test_construct_base_tag(attributes):
    """Test for validating whether the base tag is constructed correctly or
    not.
    """
    base = Base(**attributes)
    assert base.construct_tag() == base_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'href': 123}, ValueError, 'value should be string'),
    ({'target': 123}, ValueError, 'value should be string'),
    ({'href': None, 'target': None},
     AttributeError,
     'either a href attribute or a target attribute, or both')
])
def test_construct_base_tag_error(attributes, exception, error_msg):
    """Test for validating base tag's attributes."""
    with pytest.raises(exception) as exc:
        Base(**attributes)

    assert error_msg in str(exc)
