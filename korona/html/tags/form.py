# -*- coding: utf-8 -*-
"""Module for constructing <form> tag."""

from ...lib.utils import validate_attribute_values
from ...templates.html.tags import form_tag


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
