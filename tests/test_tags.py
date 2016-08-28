# -*- coding: utf-8 -*-

import pytest

from korona.html.construct import (
    A,
    Abbr,
    Acronym,
    Address,
    Area,
    Article,
    B,
    Base,
    Button,
    Canvas,
    Caption,
    Cite
)
from korona.templates.html import (
    anchor_tag,
    abbr_tag,
    acronym_tag,
    address_tag,
    area_tag,
    article_tag,
    bold_tag,
    base_tag,
    button_tag,
    canvas_tag,
    caption_tag,
    cite_tag
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
    ({'type': 1}, AttributeError, 'only used when href attribute is set.'),
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
    ({'text': None}),
    ({'text': '<p>Hi there</p>'})
])
def test_construct_address_tag(attributes):
    """Test for validating whether the address tag is constructed correctly or
    not.
    """
    address = Address(**attributes)
    assert address.construct_tag() == address_tag.render(attributes)


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
    assert area.construct_tag() == area_tag.render(attributes)


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

    assert area.construct_tag() == area_tag.render(attributes)


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
])
def test_construct_area_tag_error(attributes, exception, error_msg):
    """Test for validating area tag's attributes."""
    with pytest.raises(exception) as exc:
        Area(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None}),
    ({'text': '<p>Hi there</p>'})
])
def test_construct_article_tag(attributes):
    """Test for validating whether the article tag is constructed correctly or
    not.
    """
    article = Article(**attributes)
    assert article.construct_tag() == article_tag.render(attributes)


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


@parametrize('attributes', [
    ({'type': 'submit', 'autofocus': True}),
    ({'type': 'submit', 'disabled': True}),
    ({'type': 'submit', 'formnovalidate': True}),
    ({'type': 'submit', 'text': 'HTML'}),
    ({'type': 'submit', 'name': 'HTML', 'value': 'HTML', 'text': 'HTML'}),
    ({'type': 'submit',
      'text': 'HTML',
      'form': 'form1',
      'formaction': 'demo.asp',
      'formmethod': 'post',
      'formtarget': '_blank',
      'formenctype': 'multipart/form-data'})
])
def test_construct_button_tag(attributes):
    """Test for validating whether the button tag is constructed correctly or
    not.
    """
    button = Button(**attributes)
    assert button.construct_tag() == button_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({}, AttributeError, 'Button type should be specified'),
    ({'type': 'reset', 'formaction': 'demo.asp'},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'reset', 'formmethod': 'post'},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'reset', 'formtarget': '_blank'},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'reset', 'formenctype': 'multipart/form-data'},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'reset', 'formnovalidate': True},
     AttributeError,
     'attribute is only used for buttons with type "submit"'),
    ({'type': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'type': 'submit', 'formenctype': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'type': 'submit', 'formmethod': 'abc'},
     AttributeError,
     'attribute values should be one of these'),

])
def test_construct_button_tag_error(attributes, exception, error_msg):
    """Test for validating button tag's attributes."""
    with pytest.raises(exception) as exc:
        Button(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'height': '100'}),
    ({'width': '200'}),
    ({'height': '100', 'width': '200'})
])
def test_construct_canvas_tag(attributes):
    """Test for validating whether the canvas tag is constructed correctly or
    not.
    """
    canvas = Canvas(**attributes)
    assert canvas.construct_tag() == canvas_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'height': 123}, ValueError, 'should be a string'),
    ({'width': 123}, ValueError, 'should be a string'),
    ({'height': None, 'width': 123},
     ValueError,
     'should be a string')
])
def test_construct_canvas_tag_error(attributes, exception, error_msg):
    """Test for validating canvas tag's attributes."""
    with pytest.raises(exception) as exc:
        Canvas(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'align': 'top'}),
    ({'text': 'abcd'}),
    ({'align': 'bottom', 'text': 'abcd'})
])
def test_construct_caption_tag(attributes):
    """Test for validating whether the caption tag is constructed correctly or
    not.
    """
    caption = Caption(**attributes)
    assert caption.construct_tag() == caption_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 123}, ValueError, 'should be a string'),
    ({'align': 'abcd', 'text': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_caption_tag_error(attributes, exception, error_msg):
    """Test for validating caption tag's attributes."""
    with pytest.raises(exception) as exc:
        Caption(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd'}),
])
def test_construct_cite_tag(attributes):
    """Test for validating whether the citation tag is constructed correctly or
    not.
    """
    cite = Cite(**attributes)
    assert cite.construct_tag() == cite_tag.render(attributes)
