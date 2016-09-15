# -*- coding: utf-8 -*-
"""Module for constructing Html Tags."""


from __future__ import absolute_import

from ..lib.utils import (
    validate_attribute_values,
    validate_url
)

from ..templates.html import (
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
