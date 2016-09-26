# -*- coding: utf-8 -*-

import warnings

import pytest

from ..fixtures import parametrize

from korona.exceptions import TagAttributeError, AttributeValueError
from korona.html.tags import A
from korona.templates.html.tags import anchor


@parametrize('attributes', [
    ({'href': 'www.google.com'}),
    ({'href': 'www.google.com', 'rel': 'nofollow'}),
    ({'charset': 'utf-8',
      'download': '/abc/images.jpeg',
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
    anchor_ = A(**attributes)
    assert anchor_.construct() == anchor.render(attributes)


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
    anchor_ = A(**attributes)

    if not isinstance(attributes['coords'], str):
        attributes['coords'] = (','.join(str(coord)
                                         for coord in attributes['coords']))

    assert anchor_.construct() == anchor.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'rel': 1}, TagAttributeError, 'only used when href attribute is set.'),
    ({'type': 1}, TagAttributeError, 'only used when href attribute is set.'),
    ({'charset': 1}, AttributeValueError, 'should be a string'),
    ({'rel': 1, 'href': 'www.google.com'},
     AttributeValueError,
     'should be a string'),
    ({'shape': 'circle', 'coords': [1, 2, 3, 4]},
     TagAttributeError,
     'coordinates should be given for circle shape'),
    ({'shape': 'rect', 'coords': [1, 2, 3, 4, 5]},
     TagAttributeError,
     'coordinates should be given for rectangle shape'),
    ({'shape': 'circle', 'coords': [1, 2]},
     TagAttributeError,
     'coordinates should be given for circle shape'),
    ({'shape': 'rect', 'coords': [1, 2, 3]},
     TagAttributeError,
     'coordinates should be given for rectangle shape'),
    ({'shape': 'rect', 'coords': {'x': 1, 'y': 2}},
     AttributeValueError,
     'should be either list/tuple/str not a dictionary'),
    ({'coords': [1, 2, 3]},
     TagAttributeError,
     'shape attribute should be present when coords are specified'),
    ({'download': 'abc'},
     TagAttributeError,
     'only used when href attribute is set.'),
    ({'href': 'www.google.com', 'rel': 'abc'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'rev': 'abc'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'shape': 'abc'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'href': 532},
     ValueError,
     'is not a valid url')
])
def test_construct_anchor_tag_error(attributes, exception, error_msg):
    """Test for validating anchor tag's attributes."""
    with pytest.raises(exception) as exc:
        A(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes,warning', [
    ({'charset': 'temp'}, 'Common character sets used are')
])
def test_charsets_attribute_warning(attributes, warning):
    """Validates the warning message displayed for charset attribute in
    anchor tag.
    """
    with warnings.catch_warnings(record=True) as expected_warning:
        A(**attributes)

    assert len(expected_warning) == 1
    assert issubclass(expected_warning[-1].category, UserWarning)
    assert warning in str(expected_warning[-1].message)
