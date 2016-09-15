# -*- coding: utf-8 -*-

import pytest

from korona.html.construct import (
    Article,
    B,
    Base,
    Button,
    Canvas,
    Caption,
    Cite,
    Col,
    ColGroup,
    DD,
    Del,
    Details,
    Dialog,
    Div,
    DL,
    DT,
    Embed,
    FieldSet,
    Figure,
    Footer,
    Form,
    Frame,
    FrameSet,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Head,
    Header,
    HR,
    Html,
    I,
    IFrame,
    Img
)
from korona.templates.html import (
    article_tag,
    bold_tag,
    base_tag,
    button_tag,
    canvas_tag,
    caption_tag,
    cite_tag,
    col_tag,
    colgroup_tag,
    dd_tag,
    del_tag,
    details_tag,
    dialog_tag,
    div_tag,
    dl_tag,
    dt_tag,
    embed_tag,
    fieldset_tag,
    figure_tag,
    footer_tag,
    form_tag,
    frame_tag,
    frameset_tag,
    h1_tag,
    h2_tag,
    h3_tag,
    h4_tag,
    h5_tag,
    h6_tag,
    head_tag,
    header_tag,
    hr_tag,
    html_tag,
    italics_tag,
    iframe_tag,
    img_tag
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
    ({'text': 'abc'}),
    ({'text': None}),
    ({'text': '<p>Hi there</p>'})
])
def test_construct_article_tag(attributes):
    """Test for validating whether the article tag is constructed correctly or
    not.
    """
    article = Article(**attributes)
    assert article.construct() == article_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None})
])
def test_construct_bold_tag(attributes):
    """Test for validating whether the bold tag is constructed correctly or
    not.
    """
    bold = B(**attributes)
    assert bold.construct() == bold_tag.render(attributes)


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
    assert base.construct() == base_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'href': 123}, ValueError, 'is not a valid url'),
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
    assert button.construct() == button_tag.render(attributes)


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
    assert canvas.construct() == canvas_tag.render(attributes)


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
    assert caption.construct() == caption_tag.render(attributes)


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
    assert cite.construct() == cite_tag.render(attributes)


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


@parametrize('attributes', [
    ({'text': 'abc'})
])
def test_construct_dd_tag(attributes):
    """Test for validating whether the dd tag is constructed correctly or not.
    """
    dd = DD(**attributes)
    assert dd.construct() == dd_tag.render(attributes)


@parametrize('attributes', [
    ({'cite': 'www.abcd.com'}),
    ({'datetime': '2014-11-15T22:55:03Z'}),
    ({'datetime': '2015-11-15T22:55:03Z', 'text': 'abcd'})
])
def test_construct_del_tag(attributes):
    """Test for validating whether the del tag is constructed correctly or not.
    """
    del_ = Del(**attributes)
    assert del_.construct() == del_tag.render(attributes)


@parametrize('attributes', [
    ({'open': True}),
    ({'text': 'abcd'}),
    ({'open': True, 'text': 'abcd'})
])
def test_construct_details_tag(attributes):
    """Test for validating whether the details tag is constructed correctly or
    not.
    """
    details = Details(**attributes)
    assert details.construct() == details_tag.render(attributes)


@parametrize('attributes', [
    ({'open': True}),
    ({'text': 'abcd'}),
    ({'open': True, 'text': 'abcd'})
])
def test_construct_dialog_tag(attributes):
    """Test for validating whether the dialog tag is constructed correctly or
    not.
    """
    dialog = Dialog(**attributes)
    assert dialog.construct() == dialog_tag.render(attributes)


@parametrize('attributes', [
    ({'align': 'left'}),
    ({'text': 'abcd'}),
    ({'align': 'right', 'text': 'abcd'})
])
def test_construct_div_tag(attributes):
    """Test for validating whether the div tag is constructed correctly or not.
    """
    div = Div(**attributes)
    assert div.construct() == div_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_div_tag_error(attributes, exception, error_msg):
    """Test for validating div tag's attributes."""
    with pytest.raises(exception) as exc:
        Div(**attributes)

    assert error_msg in str(exc)


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


@parametrize('attributes', [
    ({'height': '200'}),
    ({'height': '200', 'width': '100'}),
    ({'src': 'helloworld.swf', 'height': '200', 'width': '100'}),
    ({'src': 'helloworld.swf',
      'height': '200',
      'width': '100',
      'type': 'application'})
])
def test_construct_embed_tag(attributes):
    """Test for validating whether the embed tag is constructed correctly or
    not.
    """
    embed = Embed(**attributes)
    assert embed.construct() == embed_tag.render(attributes)


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
    fieldset = FieldSet(**attributes)
    assert fieldset.construct() == fieldset_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_figure_tag(attributes):
    """Test for validating whether the figure tag is constructed correctly or
    not.
    """
    figure = Figure(**attributes)
    assert figure.construct() == figure_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_footer_tag(attributes):
    """Test for validating whether the footer tag is constructed correctly or
    not.
    """
    footer = Footer(**attributes)
    assert footer.construct() == footer_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abcd'}),
    ({'action': 'demo.asp',
      'method': 'get',
      'name': 'name1',
      'target': '_top'}),
    ({'novalidate': True}),
    ({'method': 'post', 'enctype': 'text/plain'})
])
def test_construct_form_tag(attributes):
    """Test for validating whether the form tag is constructed correctly or
    not.
    """
    form = Form(**attributes)
    assert form.construct() == form_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'enctype': 'text/plain', 'method': 'get'},
     AttributeError,
     'enctype attribute can be used/set only if method'),
    ({'method': 'post', 'enctype': 'plain'},
     AttributeError,
     'attribute values should be one of these'),
    ({'autocomplete': 'false'},
     AttributeError,
     'attribute values should be one of these'),
    ({'method': 'PUT'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_form_tag_error(attributes, exception, error_msg):
    """Test for validating form tag's attributes."""
    with pytest.raises(exception) as exc:
        Form(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'noresize': 'noresize'}),
    ({'src': 'frame_a.htm', 'scrolling': 'yes'}),
    ({'frameborder': '0'}),
    ({'src': 'frame_a.htm',
      'scrolling': 'auto',
      'marginheight': '250',
      'marginwidth': '100',
      'name': 'name1',
      'longdesc': 'a.txt'})
])
def test_construct_frame_tag(attributes):
    """Test for validating whether the frame tag is constructed correctly or
    not.
    """
    frame = Frame(**attributes)
    assert frame.construct() == frame_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'scrolling': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'noresize': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'frameborder': '2'},
     AttributeError,
     'attribute values should be one of these'),
    ({'src': 123},
     ValueError,
     'is not a valid url')
])
def test_construct_frame_tag_error(attributes, exception, error_msg):
    """Test for validating frame tag's attributes."""
    with pytest.raises(exception) as exc:
        Frame(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'cols': '25%'}),
    ({'rows': '50%'})
])
def test_construct_frameset_tag(attributes):
    """Test for validating whether the frameset tag is constructed correctly or
    not.
    """
    frameset = FrameSet(**attributes)
    assert frameset.construct() == frameset_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h1_tag(attributes):
    """Test for validating whether the h1 tag is constructed correctly or not.
    """
    h1 = H1(**attributes)
    assert h1.construct() == h1_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h1_tag_error(attributes, exception, error_msg):
    """Test for validating h1 tag's attributes."""
    with pytest.raises(exception) as exc:
        H1(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h2_tag(attributes):
    """Test for validating whether the h2 tag is constructed correctly or not.
    """
    h2 = H2(**attributes)
    assert h2.construct() == h2_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h2_tag_error(attributes, exception, error_msg):
    """Test for validating h2 tag's attributes."""
    with pytest.raises(exception) as exc:
        H2(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h3_tag(attributes):
    """Test for validating whether the h3 tag is constructed correctly or not.
    """
    h3 = H3(**attributes)
    assert h3.construct() == h3_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h3_tag_error(attributes, exception, error_msg):
    """Test for validating h3 tag's attributes."""
    with pytest.raises(exception) as exc:
        H3(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h4_tag(attributes):
    """Test for validating whether the h4 tag is constructed correctly or not.
    """
    h4 = H4(**attributes)
    assert h4.construct() == h4_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h4_tag_error(attributes, exception, error_msg):
    """Test for validating h4 tag's attributes."""
    with pytest.raises(exception) as exc:
        H4(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h5_tag(attributes):
    """Test for validating whether the h5 tag is constructed correctly or not.
    """
    h5 = H5(**attributes)
    assert h5.construct() == h5_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h5_tag_error(attributes, exception, error_msg):
    """Test for validating h5 tag's attributes."""
    with pytest.raises(exception) as exc:
        H5(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd', 'align': 'left'})
])
def test_construct_h6_tag(attributes):
    """Test for validating whether the h6 tag is constructed correctly or not.
    """
    h6 = H6(**attributes)
    assert h6.construct() == h6_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'abcd'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_h6_tag_error(attributes, exception, error_msg):
    """Test for validating h6 tag's attributes."""
    with pytest.raises(exception) as exc:
        H6(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_head_tag(attributes):
    """Test for validating whether the head tag is constructed correctly or
    not.
    """
    head = Head(**attributes)
    assert head.construct() == head_tag.render(attributes)


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_header_tag(attributes):
    """Test for validating whether the header tag is constructed correctly or
    not.
    """
    header = Header(**attributes)
    assert header.construct() == header_tag.render(attributes)


@parametrize('attributes', [
    ({'align': 'left', 'width': '50%'}),
    ({'align': 'center', 'size': '100'}),
    ({'noshade': True})
])
def test_construct_hr_tag(attributes):
    """Test for validating whether the hr tag is constructed correctly or not.
    """
    hr = HR(**attributes)
    assert hr.construct() == hr_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'top-right'},
     AttributeError,
     'attribute values should be one of these')
])
def test_construct_hr_tag_error(attributes, exception, error_msg):
    """Test for validating hr tag's attributes."""
    with pytest.raises(exception) as exc:
        HR(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'xmlns': 'www.w3.org', 'text': 'abcd'}),
    ({'manifest': 'demo.appcache', 'text': 'abcd'})
])
def test_construct_html_tag(attributes):
    """Test for validating whether the html tag is constructed correctly or
    not.
    """
    html = Html(**attributes)
    assert html.construct() == html_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'manifest': 12},
     ValueError,
     'is not a valid url.')
])
def test_construct_html_tag_error(attributes, exception, error_msg):
    """Test for validating html tag's attributes."""
    with pytest.raises(exception) as exc:
        Html(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'text': 'abcd'})
])
def test_construct_italics_tag(attributes):
    """Test for validating whether the italics tag is constructed correctly or
    not.
    """
    italics = I(**attributes)
    assert italics.construct() == italics_tag.render(attributes)


@parametrize('attributes', [
    ({'align': 'left', 'frameborder': '1'}),
    ({'src': '/demo.asp', 'height': '100', 'width': '200'}),
    ({'longdesc': 'demo.txt'}),
    ({'marginheight': '50', 'marginwidth': '50', 'name': 'example'}),
    ({'sandbox': 'allow-forms allow-scripts', 'scrolling': 'yes'}),
    ({'srcdoc': '<p>hello</p>'})
])
def test_construct_iframe_tag(attributes):
    """Test for validating whether the iframe tag is constructed correctly or
    not.
    """
    iframe = IFrame(**attributes)
    assert iframe.construct() == iframe_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'frameborder': '4'},
     AttributeError,
     'attribute values should be one of these'),
    ({'align': 'left-center'},
     AttributeError,
     'attribute values should be one of these'),
    ({'sandbox': 'abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'sandbox': 'allow-forms abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'scrolling': 'mount'},
     AttributeError,
     'attribute values should be one of these'),
    ({'sandbox': 'allow-forms allow-pointer-lock abc'},
     AttributeError,
     'attribute values should be one of these'),
    ({'longdesc': 123}, ValueError, 'is not a valid url'),
    ({'src': 123}, ValueError, 'is not a valid url')
])
def test_construct_iframe_tag_error(attributes, exception, error_msg):
    """Test for validating iframe tag's attributes."""
    with pytest.raises(exception) as exc:
        IFrame(**attributes)

    assert error_msg in str(exc)


@parametrize('attributes', [
    ({'align': 'left', 'alt': 'Smiley text', 'border': '4'}),
    ({'crossorigin': 'anonymous'}),
    ({'height': '30', 'width': '30', 'hspace': '20', 'vspace': '20'}),
    ({'ismap': True}),
    ({'longdesc': 'explained', 'src': '/demo.asp', 'usemap': 'planets'})
])
def test_construct_img_tag(attributes):
    """Test for validating whether the img tag is constructed correctly or not.
    """
    img = Img(**attributes)
    assert img.construct() == img_tag.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'align': 'left-top'},
     AttributeError,
     'attribute values should be one of these'),
    ({'longdesc': 123}, ValueError, 'is not a valid url'),
    ({'src': 123}, ValueError, 'is not a valid url')
])
def test_construct_img_tag_error(attributes, exception, error_msg):
    """Test for validating img tag's attributes."""
    with pytest.raises(exception) as exc:
        Img(**attributes)

    assert error_msg in str(exc)
