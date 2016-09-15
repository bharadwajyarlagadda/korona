# -*- coding: utf-8 -*-
"""Module for constructing Html Tags."""


from __future__ import absolute_import

from ..lib.utils import (
    validate_tag_attribute_value,
    validate_attribute_values,
    validate_url
)
from .root.attributes import TAG_ATTRIBUTES
from ..templates.html import (
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

RECTANGLE_SHAPE_COORDINATES = 4
CIRCLE_SHAPE_COORDINATES = 3


class Article(object):
    """Class for constructing article tag.

    Args:
        text (str): Article tag text. (Ex. <article>text</article>)

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text=None):
        self.tag = 'article'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed article tag <article></article>."""
        return article_tag.render(self.values)


class B(object):
    """Class for constructing bold tag.

    Args:
        text (str): Bold tag text. (Ex. <b>text</b>)

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text=None):
        self.tag = 'b'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed bold tag <b></b>."""
        return bold_tag.render(self.values)


class Base(object):
    """Class for constructing base tag.

    Args:
        href (str): Specifies the base URL for all relative URLs in the page.
        target (str): Specifies the default target for all hyperlinks and
            forms in the page.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.

    .. versionchanged:: 0.3.1
        Added URL validation for href attribute.
    """
    def __init__(self, href=None, target=None):
        # TODO: Add in the main api method where it can check that there
        # should be only one base tag in the whole html document.
        self.tag = 'base'
        validate_url(attribute_name='href', url=href)
        self.validate_values(href=href, target=target)
        self.values = {'href': href, 'target': target}

    def construct(self):
        """Returns the constructed base tag <base>."""
        return base_tag.render(self.values)

    def validate_values(self, href, target):
        """Validates the following:
            - Either of href or target attribute value is given.
            - Check whether both href and target attribute values are strings
            or not.
        """
        if not href and not target:
            raise AttributeError('<base>: base tag must have either a href '
                                 'attribute or a target attribute, or both.')

        if target and not isinstance(target, str):
            raise ValueError('<base>: target attribute value should be '
                             'string')


class Button(object):
    """Class for constructing button tag.

    Args:
        autofocus (bool): Specifies that a button should automatically get
            focus when the page loads.
        disabled (bool): Specifies that a button should be disabled.
        form (str): Specifies one or more forms the button belongs to.
        formaction (str): Specifies where to send the form-data when a form is
            submitted. Only for type="submit".
        formenctype (str): Specifies how form-data should be encoded before
            sending it to a server. Only for type="submit".
        formmethod (str): Specifies how to send the form-data (which HTTP
            method to use). Only for type="submit".
        formnovalidate (bool): Specifies that the form-data should not be
            validated on submission. Only for type="submit".
        formtarget (str): Specifies where to display the response after
            submitting the form. Only for type="submit".
        name (str): Specifies a name for the button.
        type (str): Specifies the type of button.
        value (str): Specifies an initial value for the button.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self,
                 autofocus=False,
                 disabled=False,
                 form=None,
                 formaction=None,
                 formenctype=None,
                 formmethod=None,
                 formnovalidate=False,
                 formtarget=None,
                 name=None,
                 type=None,
                 value=None,
                 text=None):
        self.tag = 'button'
        self.validate_type(value=type)
        self.pre_validate(type=type,
                          attribute_name='formaction',
                          value=formaction)
        self.pre_validate(type=type,
                          attribute_name='formenctype',
                          value=formenctype)
        self.validate_values(attribute_name='formenctype', value=formenctype)
        self.pre_validate(type=type,
                          attribute_name='formmethod',
                          value=formmethod)
        self.validate_values(attribute_name='formmethod', value=formmethod)
        self.pre_validate(type=type,
                          attribute_name='formnovalidate',
                          value=formnovalidate)
        self.pre_validate(type=type,
                          attribute_name='formtarget',
                          value=formtarget)
        self.validate_values(attribute_name='type', value=type)

        self.values = {'autofocus': autofocus,
                       'disabled': disabled,
                       'form': form,
                       'formaction': formaction,
                       'formenctype': formenctype,
                       'formmethod': formmethod,
                       'formnovalidate': formnovalidate,
                       'formtarget': formtarget,
                       'name': name,
                       'type': type,
                       'value': value,
                       'text': text}

    def construct(self):
        """Returns the constructed base tag <button>."""
        return button_tag.render(self.values)

    def validate_type(self, value):
        """Validate the type attribute for a <button> element. Different
        browsers use different default types for the <button> element.
        """
        if not value:
            raise AttributeError('<button>: Button type should be specified')

    def pre_validate(self, type, attribute_name, value):
        """Validates whether an attribute is dependant on another attribute or
        not. Some of the attributes requires type attribute to be set to
        'submit'.
        """
        if not value:
            return

        if value and type != 'submit':
            raise AttributeError('<button>: The {attribute_name} attribute is '
                                 'only used for buttons with type "submit"'
                                 .format(attribute_name=attribute_name))

    def validate_values(self, attribute_name, value):
        """Validates whether the given attribute value is a valid value or not.
        Some of the attributes have confined values. Even if we give some
        other value, the html output would not be correct.
        """
        if not value:
            return

        attribute_values = TAG_ATTRIBUTES[self.tag][attribute_name]['values']

        if value not in attribute_values:
            raise AttributeError('<button>: {attribute_name} attribute '
                                 'values should be one of these: {values}'
                                 .format(attribute_name=attribute_name,
                                         values=','.join(attribute_values)))


class Canvas(object):
    """Class for constructing canvas tag.

    Args:
        height (str): Specifies the height of the canvas.
        width (str): Specifies the width of the canvas.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, height=None, width=None):
        # TODO: Possible add the canvas text attribute.
        self.tag = 'canvas'
        validate_tag_attribute_value(tag=self.tag, value=height)
        validate_tag_attribute_value(tag=self.tag, value=width)
        self.values = {'height': height, 'width': width}

    def construct(self):
        """Returns the constructed canvas tag <canvas>."""
        return canvas_tag.render(self.values)


class Caption(object):
    """Class for constructing caption tag.

    Args:
        align (str): Defines the alignment of the caption.
        text (str): Specifies the caption text.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, align=None, text=None):
        self.tag = 'caption'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed caption tag <caption>."""
        return caption_tag.render(self.values)


class Cite(object):
    """Class for constructing cite tag.

    Args:
        text (str): Specifies the citation text.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text):
        self.tag = 'cite'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed cite tag <cite>."""
        return cite_tag.render(self.values)


class Col(object):
    """Class for constructing col tag.

    Args:
        align (str): Specifies the alignment of the content related to a <col>
            element.
        char (str): Specifies the alignment of the content related to a <col>
            element to a character.
        charoff (int): Specifies the number of characters the content will be
            aligned from the character specified by the char attribute.
        span (int): Specifies the number of columns a <col> element should
            span.
        valign (str): Specifies the vertical alignment of the content related
            to a <col> element.
        width (str): Specifies the width of a <col> element.

    .. versionadded:: 0.2.0
    """
    def __init__(self,
                 align=None,
                 char=None,
                 charoff=None,
                 span=None,
                 valign=None,
                 width=None):
        self.tag = 'col'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.validate_char_attribute(align=align, value=char)
        self.validate_charoff_attribute(align=align, char=char, value=charoff)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='valign',
                                  value=valign)
        self.values = {'align': align,
                       'char': char,
                       'charoff': charoff,
                       'span': span,
                       'valign': valign,
                       'width': width}

    def construct(self):
        """Returns the constructed col tag <col>."""
        return col_tag.render(self.values)

    def validate_char_attribute(self, align, value):
        """Validates char attribute. The char attribute can only be used if
        the align attribute is set to "char".
        """
        if not value:
            return

        if value and align != 'char':
            raise AttributeError('<col>: The char attribute can only be used '
                                 'if the align attribute is set to "char".')

    def validate_charoff_attribute(self, align, char, value):
        """Validates charoff attribute. The charoff attribute can only be
        used if the char attribute is specified and the align attribute is
        set to "char".
        """
        if not value:
            return

        if value and (not char or align != 'char'):
            raise AttributeError('<col>: The charoff attribute can only be '
                                 'used if the char attribute is specified and '
                                 'the align attribute is set to "char".')


class ColGroup(object):
    """Class for constructing colgroup tag.

    Args:
        align (str): Aligns the content in a column group.
        char (str): Aligns the content in a column group to a character.
        charoff (int): Sets the number of characters the content will be
            aligned from the character specified by the char attribute.
        span (int): Specifies the number of columns a column group should span.
        valign (str): Vertical aligns the content in a column group.
        width (str): Specifies the width of a column group.

    .. versionadded:: 0.2.0
    """
    def __init__(self,
                 align=None,
                 char=None,
                 charoff=None,
                 span=None,
                 valign=None,
                 width=None):
        self.tag = 'colgroup'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.validate_char_attribute(align=align, value=char)
        self.validate_charoff_attribute(align=align, char=char, value=charoff)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='valign',
                                  value=valign)
        self.values = {'align': align,
                       'char': char,
                       'charoff': charoff,
                       'span': span,
                       'valign': valign,
                       'width': width}

    def construct(self):
        """Returns the constructed colgroup tag <colgroup>."""
        return colgroup_tag.render(self.values)

    def validate_char_attribute(self, align, value):
        """Validates char attribute. The char attribute can only be used if
        the align attribute is set to "char".
        """
        if not value:
            return

        if value and align != 'char':
            raise AttributeError('<colgroup>: The char attribute can only be '
                                 'used if the align attribute is set to '
                                 '"char".')

    def validate_charoff_attribute(self, align, char, value):
        """Validates charoff attribute. The charoff attribute can only be
        used if the char attribute is specified and the align attribute is
        set to "char".
        """
        if not value:
            return

        if value and (not char or align != 'char'):
            raise AttributeError('<colgroup>: The charoff attribute can only '
                                 'be used if the char attribute is specified '
                                 'and the align attribute is set to "char".')


class DD(object):
    """Class for constructing dd tag.

    Args:
        text (str): Specifies the dd text. (As in <dd>{text}</dd>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        self.tag = 'dd'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed dd tag <dd></dd>."""
        return dd_tag.render(self.values)


class Del(object):
    """Class for constructing del tag.

    Args:
        cite (str): Specifies a URL to a document that explains the reason
            why the text was deleted.
        datetime (datetime): Specifies the date and time of when the text was
            deleted.

    .. versionadded:: 0.2.0
    """
    def __init__(self, cite=None, datetime=None, text=None):
        self.tag = 'del'
        # TODO: If possible, add validation for attribute cite
        self.values = {'cite': cite, 'datetime': datetime, 'text': text}

    def construct(self):
        """Returns the constructed del tag <del>."""
        return del_tag.render(self.values)


class Details(object):
    """Class for constructing details tag.

    Args:
        open (bool): Specifies that the details should be visible (open) to
            the user.
        text (str): Specifies the details text. (As in
            <details>{text}</details>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, open=False, text=None):
        self.tag = 'details'
        self.values = {'open': open, 'text': text}

    def construct(self):
        """Returns the constructed details tag <details></details>."""
        return details_tag.render(self.values)


class Dialog(object):
    """Class for constructing dialog tag.

    Args:
        open (bool): Specifies that the dialog element is active and that the
            user can interact with it.
        text (str): Specifies the dialog text. (As in
            <dialog>{text}</dialog>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, open=False, text=None):
        self.tag = 'dialog'
        self.values = {'open': open, 'text': text}

    def construct(self):
        """Returns the constructed dialog tag <dialog></dialog>."""
        return dialog_tag.render(self.values)


class Div(object):
    """Class for constructing div tag.

    Args:
        align (str): Specifies the alignment of the content inside a <div>
            element.
        text (str): Specifies the div text. (As in <div>{text}</div>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'div'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed div tag <div></div>."""
        return div_tag.render(self.values)


class DL(object):
    """Class for constructing dl tag.

    Args:
        text (str): Specifies the dl text. (As in <dl>{text}</dl>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        self.tag = 'dl'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed dl tag <dl></dl>."""
        return dl_tag.render(self.values)


class DT(object):
    """Class for constructing dt tag.

    Args:
        text (str): Specifies the dt text. (As in <dt>{text}</dt>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        self.tag = 'dt'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed dt tag <dt></dt>."""
        return dt_tag.render(self.values)


class Embed(object):
    """Class for constructing embed tag.

    Args:
        height (str): Specifies the height of the embedded content (in pixels).
        width (str): Specifies the width of the embedded content (in pixels).
        src (str): Specifies the address of the external file to embed.
        type (str): Specifies the media type of the embedded content.

    .. versionadded:: 0.2.0
    """
    def __init__(self, height=None, width=None, src=None, type=None):
        self.tag = 'embed'
        self.values = {'height': height,
                       'width': width,
                       'src': src,
                       'type': type}

    def construct(self):
        """Returns the constructed embed tag <embed>."""
        return embed_tag.render(self.values)


class FieldSet(object):
    """Class for constructing fieldset tag.

    Args:
        disabled (bool): Specifies that a group of related form elements
            should be disabled.
        form (str): Specifies one or more forms the fieldset belongs to.
        name (str): Specifies a name for the fieldset.

    .. versionadded:: 0.2.0
    """
    def __init__(self, disabled=False, form=None, name=None):
        # TODO: Add support for inner tags.
        self.tag = 'fieldset'
        self.values = {'disabled': disabled, 'form': form, 'name': name}

    def construct(self):
        """Returns the constructed fieldset tag <fieldset></fieldset>."""
        return fieldset_tag.render(self.values)


class Figure(object):
    """Class for constructing figure tag.

    Args:
        text (str): Specifies the figure text. (As in <figure>{text}</figure>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        # TODO: Add support for inner tags.
        self.tag = 'figure'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed figure tag <figure></figure>."""
        return figure_tag.render(self.values)


class Footer(object):
    """Class for constructing the footer tag.

    Args:
        text (str): Specifies the footer text. (As in <footer>{text}</footer>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        # TODO: Add support for inner tags.
        self.tag = 'footer'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed footer tag <footer></footer>."""
        return footer_tag.render(self.values)


class Form(object):
    """Class for constructing <form> tag.

    Args:
        accept (str): Specifies a comma-separated list of file types that the
            server accepts (that can be submitted through the file upload).
        action (str): Specifies where to send the form-data when a form is
            submitted.
        autocomplete (str): Specifies whether a form should have autocomplete
            on or off.
        enctype (str): Specifies how the form-data should be encoded when
            submitting it to the server (only for method="post").
        method (str): Specifies the HTTP method to use when sending form-data.
        name (str): Specifies the name of a form.
        novalidate (bool): Specifies that the form should not be validated
            when submitted.
        target (str): Specifies where to display the response that is received
            after submitting the form.
        text (str): Specifies the form text. (As in <form>{text}</form>)

    .. versionadded:: 0.2.0
    """
    def __init__(self,
                 accept=None,
                 action=None,
                 autocomplete=None,
                 enctype=None,
                 method=None,
                 name=None,
                 novalidate=False,
                 target=None,
                 text=None):
        self.tag = 'form'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='autocomplete',
                                  value=autocomplete)
        self.validate_enctype_attribute(method=method, enctype=enctype)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='enctype',
                                  value=enctype)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='method',
                                  value=method)
        self.values = {'accept': accept,
                       'action': action,
                       'autocomplete': autocomplete,
                       'enctype': enctype,
                       'method': method,
                       'name': name,
                       'novalidate': novalidate,
                       'target': target,
                       'text': text}

    def construct(self):
        """Returns the constructed form tag <form></form>."""
        return form_tag.render(self.values)

    def validate_enctype_attribute(self, method, enctype):
        """Validates enctype attribute. The enctype attribute can be used only
        if method is post.
        """
        if not enctype:
            return

        if enctype and method != 'post':
            raise AttributeError('<form>: The enctype attribute can be '
                                 'used/set only if method="post".')


class Frame(object):
    """Class for constructing <frame> tag.

    Args:
        frameborder (str): Specifies whether or not to display a border around
            a frame.
        longdesc (str): Specifies a page that contains a long description of
            the content of a frame.
        marginheight (str): Specifies the top and bottom margins of a frame.
        marginwidth (str): Specifies the left and right margins of a frame.
        name (str): Specifies the name of a frame.
        noresize (str): Specifies that a frame is not resizable.
        scrolling (str): Specifies whether or not to display scrollbars in a
            frame.
        src (str): Specifies the URL of the document to show in a frame.

    .. versionadded:: 0.2.0

    .. versionchanged:: 0.3.1
        Added URL validation for src attribute.
    """
    def __init__(self,
                 frameborder=None,
                 longdesc=None,
                 marginheight=None,
                 marginwidth=None,
                 name=None,
                 noresize=None,
                 scrolling=None,
                 src=None):
        self.tag = 'frame'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='frameborder',
                                  value=frameborder)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='noresize',
                                  value=noresize)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='scrolling',
                                  value=scrolling)
        validate_url(attribute_name='src', url=src)
        self.values = {'frameborder': frameborder,
                       'longdesc': longdesc,
                       'marginheight': marginheight,
                       'marginwidth': marginwidth,
                       'name': name,
                       'noresize': noresize,
                       'scrolling': scrolling,
                       'src': src}

    def construct(self):
        """Returns the constructed tag <frame>."""
        return frame_tag.render(self.values)


class FrameSet(object):
    """Class for constructing <frameset> tag.

    Args:
        cols (str): Specifies the number and size of columns in a frameset.
        rows (str): Specifies the number and size of rows in a frameset.

    .. versionadded:: 0.2.0
    """
    def __init__(self, cols=None, rows=None):
        self.tag = 'frameset'
        self.values = {'cols': cols, 'rows': rows}

    def construct(self):
        """Returns the constructed tag <frameset>."""
        return frameset_tag.render(self.values)


class H1(object):
    """Class for constructing <h1> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h1> text. (As in <h1>{text}</h1>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h1'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h1>."""
        return h1_tag.render(self.values)


class H2(object):
    """Class for constructing <h2> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h2> text. (As in <h2>{text}</h2>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h2'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h2>."""
        return h2_tag.render(self.values)


class H3(object):
    """Class for constructing <h3> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h3> text. (As in <h3>{text}</h3>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h3'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h3>."""
        return h3_tag.render(self.values)


class H4(object):
    """Class for constructing <h4> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h4> text. (As in <h4>{text}</h4>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h4'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h4>."""
        return h4_tag.render(self.values)


class H5(object):
    """Class for constructing <h5> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h5> text. (As in <h5>{text}</h5>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h5'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h5>."""
        return h5_tag.render(self.values)


class H6(object):
    """Class for constructing <h6> tag.

    Args:
        align (str): Specifies the alignment of a heading.
        text (str): Specifies the <h6> text. (As in <h6>{text}</h6>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, text=None):
        self.tag = 'h6'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed tag <h6>."""
        return h6_tag.render(self.values)


class Head(object):
    """Class for constructing <head> tag.

    Args:
        text (str): Specifies the head text. (As in <head>{text}</head>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, text=None):
        # TODO: Add the ability to validate which inner tags can go into the
        # <head> tag.
        self.tag = 'head'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed tag <head>."""
        return head_tag.render(self.values)


class Header(object):
    """Class for constructing the header tag.

    Args:
        text (str): Specifies the header text. (As in <header>{text}</header>)

    .. versionadded:: 0.3.0
    """
    def __init__(self, text=None):
        # TODO: Add support for inner tags.
        self.tag = 'header'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed header tag <header></header>."""
        return header_tag.render(self.values)


class HR(object):
    """Class for constructing hr tag.

    Args:
        align (str): Specifies the alignment of a <hr> element.
        noshade (bool): Specifies that a <hr> element should render in one
            solid color (noshaded), instead of a shaded color.
        size (str): Specifies the height of a <hr> element.
        width (str): Specifies the width of a <hr> element

    .. versionadded:: 0.3.0
    """
    def __init__(self, align=None, noshade=False, size=None, width=None):
        self.tag = 'hr'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        self.values = {'align': align,
                       'noshade': noshade,
                       'size': size,
                       'width': width}

    def construct(self):
        """Returns the constructed hr tag <hr>."""
        return hr_tag.render(self.values)


class Html(object):
    """Class for constructing html tag.

    Args:
        manifest (str): Specifies the address of the document's cache manifest
            (for offline browsing)
        xmlns (str): Specifies the XML namespace attribute (If you need your
            content to conform to XHTML)
        text (str): Specifies the html text. (As in <html>{text}</html>)

    .. versionadded:: 0.4.0-dev
    """
    def __init__(self, manifest=None, xmlns=None, text=None):
        # TODO: Add support for inner tags.
        self.tag = 'html'
        validate_url(attribute_name='manifest', url=manifest)
        self.values = {'manifest': manifest,
                       'xmlns': xmlns,
                       'text': text}

    def construct(self):
        """Returns the constructed html tag <html>."""
        return html_tag.render(self.values)


class I(object):
    """Class for constructing <i> tag.

    Args:
        text (str): Specifies the italics text. (As in <i>{text}</i>)

    .. versionadded:: 0.4.0-dev
    """
    def __init__(self, text=None):
        self.tag = 'i'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed italics tag <i>."""
        return italics_tag.render(self.values)


class IFrame(object):
    """Class for constructing <iframe> tag.

    Args:
        align (str): Specifies the alignment of an <iframe> according to
            surrounding elements.
        frameborder (str): Specifies whether or not to display a border around
            an <iframe>.
        height (str): Specifies the height of an <iframe>.
        longdesc (str): Specifies a page that contains a long description of
            the content of an <iframe>.
        marginheight (str): Specifies the top and bottom margins of the
            content of an <iframe>.
        marginwidth (str): Specifies the left and right margins of the content
            of an <iframe>.
        name (str): Specifies the name of an <iframe>.
        sandbox (str): Enables an extra set of restrictions for the content in
            an <iframe>.
        scrolling (str): Specifies whether or not to display scrollbars in an
            <iframe>.
        src (str): Specifies the address of the document to embed in the
            <iframe>.
        srcdoc (str): Specifies the HTML content of the page to show in the
            <iframe>.
        width (str): Specifies the width of an <iframe>.

    .. versionadded:: 0.4.0-dev
    """
    def __init__(self,
                 align=None,
                 frameborder=None,
                 height=None,
                 longdesc=None,
                 marginheight=None,
                 marginwidth=None,
                 name=None,
                 sandbox=None,
                 scrolling=None,
                 src=None,
                 srcdoc=None,
                 width=None):
        self.tag = 'iframe'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='frameborder',
                                  value=frameborder)
        validate_url(attribute_name='longdesc', url=longdesc)
        self.validate_sandbox(sandbox=sandbox)
        validate_attribute_values(tag=self.tag,
                                  attribute_name='scrolling',
                                  value=scrolling)
        validate_url(attribute_name='src', url=src)
        self.values = {'align': align,
                       'frameborder': frameborder,
                       'height': height,
                       'longdesc': longdesc,
                       'marginheight': marginheight,
                       'marginwidth': marginwidth,
                       'name': name,
                       'sandbox': sandbox,
                       'scrolling': scrolling,
                       'src': src,
                       'srcdoc': srcdoc,
                       'width': width}

    def construct(self):
        """Returns the constructed iframe tag <iframe>."""
        return iframe_tag.render(self.values)

    def validate_sandbox(self, sandbox):
        """Validates sandbox attribute. The value of the sandbox attribute
        can either be just sandbox (then all restrictions are applied), or a
        space-separated list of pre-defined values that will REMOVE the
        particular restrictions.
        """
        if not sandbox:
            return

        parts = sandbox.split(' ')

        for part in parts:
            validate_attribute_values(tag=self.tag,
                                      attribute_name='sandbox',
                                      value=part)


class Img(object):
    """Class for constructing <img> tag.

    Args:
        align (str): Specifies the alignment of an image according to
            surrounding elements.
        alt (str): Specifies an alternate text for an image.
        border (str): Specifies the width of the border around an image.
        crossorigin (str): Allow images from third-party sites that allow
            cross-origin access to be used with canvas.
        height (str): Specifies the height of an image.
        hspace (str): Specifies the whitespace on left and right side of an
            image.
        ismap (bool): Specifies an image as a server-side image-map.
        longdesc (str): Specifies a URL to a detailed description of an image.
        src (str): Specifies the URL of an image.
        usemap (str): Specifies an image as a client-side image-map.
        vspace (str): Specifies the whitespace on top and bottom of an image.
        width (str): Specifies the width of an image.

    .. versionadded:: 0.4.0-dev
    """
    def __init__(self,
                 align=None,
                 alt=None,
                 border=None,
                 crossorigin=None,
                 height=None,
                 hspace=None,
                 ismap=False,
                 longdesc=None,
                 src=None,
                 usemap=None,
                 vspace=None,
                 width=None):
        self.tag = 'img'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  value=align)
        # TODO: Add validation for ismap attribute.
        validate_url(attribute_name='longdesc', url=longdesc)
        validate_url(attribute_name='src', url=src)
        # TODO: Add validation for usemap attribute.
        self.values = {'align': align,
                       'alt': alt,
                       'border': border,
                       'crossorigin': crossorigin,
                       'height': height,
                       'hspace': hspace,
                       'ismap': ismap,
                       'longdesc': longdesc,
                       'src': src,
                       'usemap': usemap,
                       'vspace': vspace,
                       'width': width}

    def construct(self):
        """Returns the constructed image tag <img>."""
        return img_tag.render(self.values)
