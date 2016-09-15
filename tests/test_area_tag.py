# -*- coding: utf-8 -*-

import pytest

from .fixtures import parametrize

from korona.html.tags import Area
from korona.templates.html import area_tag


@parametrize('attributes', [
    ({'href': 'www.google.com', 'alt': 'abc'}),
    ({'href': 'www.google.com', 'alt': 'abc', 'rel': 'nofollow'}),
    ({'download': 'abc',
      'href': 'www.google.com',
      'hreflang': 'en',
      'rel': 'nofollow',
      'target': '_blank',
      'type': 'text/html',
      'alt': 'abc'}),
    ({'href': 'www.google.com', 'alt': 'abc'})
])
def test_construct_area_tag(attributes):
    """Test for validating whether the area tag is constructed correctly or
    not.
    """
    area = Area(**attributes)
    assert area.construct() == area_tag.render(attributes)


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
def test_construct_area_tag_coords(attributes):
    """Test for validating the shape and coordinate attributes given."""
    area = Area(**attributes)

    if not isinstance(attributes['coords'], str):
        attributes['coords'] = (','.join(str(coord)
                                         for coord in attributes['coords']))

    assert area.construct() == area_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'rel': 1}, AttributeError, 'only used when href attribute is set.'),
    ({'rel': 1, 'href': 'www.google.com', 'alt': 'abc'},
     ValueError,
     'should be a string'),
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
    ({'href': 'abc', 'alt': 'abc', 'download': 123},
     ValueError,
     'should be a string'),
    ({'href': 'www.google.com', 'alt': 'abc', 'rel': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'shape': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'alt': 'abc'},
     AttributeError,
     'attribute is only used when href attribute is set.'),
    ({'href': 'abc'},
     AttributeError,
     'attribute is required if the href attribute is present'),
    ({'href': 532, 'alt': 'abc'},
     ValueError,
     'not a valid url')
])
def test_construct_area_tag_error(attributes, exception, error_msg):
    """Test for validating area tag's attributes."""
    with pytest.raises(exception) as exc:
        Area(**attributes)

    assert error_msg in str(exc)
