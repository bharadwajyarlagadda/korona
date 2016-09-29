# -*- coding: utf-8 -*-

from ...exceptions import AttributeValueError, TagAttributeError
from ...lib.utils import (
    validate_string_attribute,
    validate_boolean_attribute,
    validate_number_attribute,
    validate_attribute_values
)
from ...templates.html.global_attributes import global_attributes

GLOBAL_ATTRIBUTES = {
    # TODO: Add data-* global attribute.
    'accesskey': {
        'description': 'Specifies a shortcut key to activate/focus an element',
        'values': None
    },
    'class': {
        'description': 'Specifies one or more classnames for an element '
                       '(refers to a class in a style sheet)',
        'values': None
    },
    'contenteditable': {
        'description': 'Specifies whether the content of an element is '
                       'editable or not',
        'values': ['true', 'false']
    },
    'contextmenu': {
        'description': 'Specifies a context menu for an element. The context '
                       'menu appears when a user right-clicks on the element',
        'values': None
    },
    'data-*': {
        'description': 'Used to store custom data private to the page or '
                       'application',
        'values': None
    },
    'dir': {
        'description': 'Specifies the text direction for the content in an '
                       'element',
        'values': ['ltr', 'rtl', 'auto']
    },
    'draggable': {
        'description': 'Specifies whether an element is draggable or not',
        'values': ['true', 'false', 'auto']
    },
    'dropzone': {
        'description': 'Specifies whether the dragged data is copied, moved, '
                       'or linked, when dropped',
        'values': ['copy', 'move', 'link']
    },
    'hidden': {
        'description': 'Specifies that an element is not yet, or is no longer,'
                       ' relevant',
        'values': None
    },
    'id': {
        'description': 'Specifies a unique id for an element',
        'values': None
    },
    'lang': {
        'description': 'Specifies the language of the element content',
        'values': None
    },
    'spellcheck': {
        'description': 'Specifies whether the element is to have its spelling '
                       'and grammar checked or not',
        'values': ['true', 'false']
    },
    'style': {
        'description': 'Specifies an inline CSS style for an element',
        'values': None
    },
    'tabindex': {
        'description': 'Specifies the tabbing order of an element',
        'values': None
    },
    'title': {
        'description': 'Specifies extra information about an element',
        'values': None
    },
    'translate': {
        'description': 'Specifies whether the content of an element should be '
                       'translated or not',
        'values': ['yes', 'no']
    }
}


class GlobalAttributes(object):
    """Class for constructing global attributes for HTML tags.

    Some of the global attributes are:

      - accesskey (str): Specifies a shortcut key to activate/focus an element.
      - class (str): Specifies one or more classnames for an element (refers
        to a class in a style sheet).
      - contenteditable (str): Specifies whether the content of an element is
        editable or not.
      - contextmenu (str): Specifies a context menu for an element. The
        context menu appears when a user right-clicks on the element.
      - dir (str): Specifies the text direction for the content in an element.
      - draggable (str): Specifies whether an element is draggable or not.
      - dropzone (str): Specifies whether the dragged data is copied, moved,
        or linked, when dropped.
      - hidden (bool): Specifies that an element is not yet, or is no longer,
        relevant.
      - id (str): Specifies a unique id for an element.
      - lang (str): Specifies the language of the element's content.
      - spellcheck (str): Specifies whether the element is to have its
        spelling and grammar checked or not.
      - style (str): Specifies an inline CSS style for an element.
      - tabindex (int): Specifies the tabbing order of an element.
      - title (str): Specifies extra information about an element.
      - translate (str): Specifies whether the content of an element should
        be translated or not.

    Args:
        kwargs (dict): A dictionary of all the global attributes used in HTML.

    .. versionadded:: 0.4.3-dev
    """
    def __init__(self, **kwargs):
        accesskey = kwargs.get('accesskey', None)
        class_ = kwargs.get('class', None)
        contenteditable = kwargs.get('contenteditable', None)
        contextmenu = kwargs.get('contextmenu', None)
        # TODO: Add support for data-* attribute
        dir = kwargs.get('dir', None)
        draggable = kwargs.get('draggable', None)
        dropzone = kwargs.get('dropzone', None)
        hidden = kwargs.get('hidden', None)
        id = kwargs.get('id', None)
        lang = kwargs.get('lang', None)
        spellcheck = kwargs.get('spellcheck', None)
        style = kwargs.get('style', None)
        tabindex = kwargs.get('tabindex', None)
        title = kwargs.get('title', None)
        translate = kwargs.get('translate', None)

        self.tag = kwargs.get('tag', None)

        self.validate_class_attribute(class_)
        validate_string_attribute(tag=self.tag,
                                  attribute_name='contenteditable',
                                  attribute_value=contenteditable)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='contenteditable',
            attribute_value=contenteditable,
            default_values=GLOBAL_ATTRIBUTES['contenteditable']['values'])
        validate_attribute_values(
            tag=self.tag,
            attribute_name='dir',
            attribute_value=dir,
            default_values=GLOBAL_ATTRIBUTES['dir']['values'])
        validate_string_attribute(tag=self.tag,
                                  attribute_name='draggable',
                                  attribute_value=draggable)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='draggable',
            attribute_value=draggable,
            default_values=GLOBAL_ATTRIBUTES['draggable']['values'])
        validate_attribute_values(
            tag=self.tag,
            attribute_name='dropzone',
            attribute_value=dropzone,
            default_values=GLOBAL_ATTRIBUTES['dropzone']['values'])
        validate_boolean_attribute(tag=self.tag,
                                   attribute_name='hidden',
                                   attribute_value=hidden)
        self.validate_id_attribute(id=id)
        validate_string_attribute(tag=self.tag,
                                  attribute_name='spellcheck',
                                  attribute_value=spellcheck)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='spellcheck',
            attribute_value=spellcheck,
            default_values=GLOBAL_ATTRIBUTES['spellcheck']['values'])
        validate_number_attribute(tag=self.tag,
                                  attribute_name='tabindex',
                                  attribute_value=tabindex)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='translate',
            attribute_value=translate,
            default_values=GLOBAL_ATTRIBUTES['translate']['values'])

        self.values = {'accesskey': accesskey,
                       'class': class_,
                       'contenteditable': contenteditable,
                       'contextmenu': contextmenu,
                       'dir': dir,
                       'draggable': draggable,
                       'dropzone': dropzone,
                       'hidden': hidden,
                       'id': id,
                       'lang': lang,
                       'spellcheck': spellcheck,
                       'style': style,
                       'tabindex': tabindex,
                       'title': title,
                       'translate': translate}

    def construct(self):
        """Returns the constructed string of global attributes."""
        return global_attributes.render(self.values)

    def validate_class_attribute(self, classname):
        """Validates whether the class attribute value starts with a letter or
        not.
        """
        if not classname:
            return

        if not classname[0].isalpha():
            raise AttributeValueError('class attribute value must begin with a'
                                      ' letter A-Z or a-z')

    def validate_id_attribute(self, id):
        """Validates that the id attribute value does not has a space character
         and at least one of the character should be an alphabet.
        """
        if not id:
            return

        if any(i == ' ' for i in id):
            raise AttributeValueError('id attribute value should not have any '
                                      'spaces.')
        if not any(i.isalpha() for i in id):
            raise AttributeValueError('id attribute value must contain at '
                                      'least one character')
