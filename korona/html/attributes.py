# -*- coding: utf-8 -*-

GLOBAL_ATTRIBUTES = {
    # TODO: Add data-* global attribute.
    # TODO: Come back and check whether there are any validations on the
    # global attributes.
    'accesskey': {
        'description': 'Specifies a shortcut key to activate/focus an element'
    },
    'class': {
        'description': 'Specifies one or more classnames for an element '
                       '(refers to a class in a style sheet)'
    },
    'contenteditable': {
        'description': 'Specifies whether the content of an element is '
                       'editable or not'
    },
    'contextmenu': {
        'description': 'Specifies a context menu for an element. The context '
                       'menu appears when a user right-clicks on the element'
    },
    'dir': {
        'description': 'Specifies the text direction for the content in an '
                       'element'
    },
    'draggable': {
        'description': 'Specifies whether an element is draggable or not'
    },
    'dropzone': {
        'description': 'Specifies whether the dragged data is copied, moved, '
                       'or linked, when dropped'
    },
    'hidden': {
        'description': 'Specifies that an element is not yet, or is no longer,'
                       ' relevant'
    },
    'id': {
        'description': 'Specifies a unique id for an element'
    },
    'lang': {
        'description': 'Specifies the language of the element content'
    },
    'spellcheck': {
        'description': 'Specifies whether the element is to have its spelling '
                       'and grammar checked or not'
    },
    'style': {
        'description': 'Specifies an inline CSS style for an element'
    },
    'tabindex': {
        'description': 'Specifies the tabbing order of an element'
    },
    'title': {
        'description': 'Specifies extra information about an element'
    },
    'translate': {
        'description': 'Specifies whether the content of an element should be '
                       'translated or not'
    }
}


TAG_ATTRIBUTES = {
    # Some of the attributes have confined values. We will mention all the
    # confined values in a list for that particular attribute. In other words,
    # the attribute values should be one of them.

    # TODO: Add default values for the respective tag attributes if any.
    'a':
        {
            'charset': {
                'description': 'Specifies the character-set of a linked '
                               'document.',
                'values': None
            },
            'coords': {
                'description': 'Specifies the coordinates of a link.',
                'values': None
            },
            'download': {
                'description': 'Specifies that the target will be downloaded '
                               'when a user clicks on the hyper link.',
                'values': None
            },
            'href': {
                'descirption': 'Specifies the URL of the page the link goes '
                               'to.',
                'values': None
            },
            'hreflang': {
                'description': 'Specifies the language of the linked '
                               'document.',
                'values': None
            },
            # TODO: Add media attribute.
            'name': {
                'description': 'Specifies the name of an anchor.',
                'values': None
            },
            'rel': {
                'description': 'Specifies the relationship between the current'
                               ' document and the linked document.',
                'values': ['alternate',
                           'author',
                           'bookmark',
                           'help',
                           'license',
                           'next',
                           'nofollow',
                           'noreferrer',
                           'prefetch',
                           'prev',
                           'search',
                           'tag']
            },
            'rev': {
                'description': 'Specifies the relationship between the linked '
                               'document and the current document.',
                'values': ['alternate',
                           'stylesheet',
                           'start',
                           'next',
                           'prev',
                           'contents',
                           'index',
                           'glossary',
                           'copyright',
                           'chapter',
                           'section',
                           'subsection',
                           'appendix',
                           'help',
                           'bookmark',
                           'nofollow']
            },
            'shape': {
                'description': 'Specifies the shape of a link.',
                'values': ['default', 'rect', 'circle', 'poly']
            },
            'target': {
                'description': 'Specifies where to open the linked document.',
                'values': None
            },
            'type': {
                'description': 'Specifies the media type of the linked '
                               'document.',
                'values': None
            }
        },
    'area':
        {
            'alt': {
                'description': 'Specifies an alternate text for the area. '
                               'Required if the href attribute is present',
                'values': None
            },
            'coords': {
                'description': 'Specifies the coordinates of the area',
                'values': None
            },
            'download': {
                'description': 'Specifies that the target will be downloaded '
                               'when a user clicks on the hyperlink',
                'values': None
            },
            'href': {
                'description': 'Specifies the hyperlink target for the area',
                'values': None
            },
            'hreflang': {
                'description': 'Specifies the language of the target URL',
                'values': None
            },
            'media': {
                'description': 'Specifies what media/device the target URL is '
                               'optimized for',
                'values': None
            },
            'nohref': {
                'description': 'Specifies that an area has no associated link',
                'values': None
            },
            'rel': {
                'description': 'Specifies the relationship between the current'
                               ' document and the target URL',
                'values': ['alternate',
                           'author',
                           'bookmark',
                           'help',
                           'license',
                           'next',
                           'nofollow',
                           'noreferrer',
                           'prefetch',
                           'prev',
                           'search',
                           'tag']
            },
            'shape': {
                'description': 'Specifies the shape of the area',
                'values': ['default', 'rect', 'circle', 'poly']
            },
            'target': {
                'description': 'Specifies where to open the target URL',
                'values': None
            },
            'type': {
                'description': 'Specifies the media type of the target URL',
                'values': None
            }
        },
    'base':
        {
            'href': {
                'description': 'Specifies the base URL for all relative URLs '
                               'in the page',
                'values': None
            },
            'target': {
                'description': 'Specifies the default target for all '
                               'hyperlinks and forms in the page',
                'values': None
            }
        },
    'button':
        {
            'autofocus': {
                'description': 'Specifies that a button should automatically '
                               'get focus when the page loads',
                'values': None
            },
            'disabled': {
                'description': 'Specifies that a button should be disabled',
                'values': None
            },
            'form': {
                'description': 'Specifies one or more forms the button '
                               'belongs to',
                'values': None
            },
            'formaction': {
                'description': 'Specifies where to send the form-data when a '
                               'form is submitted. Only for type "submit"',
                'values': None
            },
            'formenctype': {
                'description': 'Specifies how form-data should be encoded '
                               'before sending it to a server. Only for '
                               'type "submit"',
                'values': ['application/x-www-form-urlencoded',
                           'multipart/form-data',
                           'text/plain']
            },
            'formmethod': {
                'description': 'Specifies how to send the form-data (which '
                               'HTTP method to use). Only for type "submit"',
                'values': ['get', 'post']
            },
            'formnovalidate': {
                'description': 'Specifies that the form-data should not be '
                               'validated on submission. Only for type '
                               '"submit"',
                'values': None
            },
            'formtarget': {
                'description': 'Specifies where to display the response after '
                               'submitting the form. Only for type "submit"',
                'values': None
            },
            'name': {
                'description': 'Specifies a name for the button',
                'values': None
            },
            'type': {
                'description': 'Specifies the type of button',
                'values': ['button', 'reset', 'submit']
            },
            'value': {
                'descirption': 'Specifies an initial value for the button',
                'values': None
            }
        },
    'caption':
        {
            'align': {
                'description': 'Defines the alignment of the caption',
                'values': ['left', 'right', 'top', 'bottom']
            }
        },
    'col':
        {
            'align': {
                'description': 'Specifies the alignment of the content related'
                               ' to a <col> element',
                'values': ['left', 'right', 'center', 'justify', 'char']
            },
            'char': {
                'description': 'Specifies the alignment of the content related'
                               ' to a <col> element to a character',
                'values': None
            },
            'charoff': {
                'description': 'Specifies the number of characters the content'
                               ' will be aligned from the character specified '
                               'by the char attribute',
                'values': None
            },
            'span': {
                'description': 'Specifies the number of columns a <col> '
                               'element should span',
                'values': None
            },
            'valign': {
                'description': 'Specifies the vertical alignment of the '
                               'content related to a <col> element',
                'values': ['top', 'middle', 'bottom', 'baseline']
            },
            'width': {
                'description': 'Specifies the width of a <col> element',
                'values': None
            }
        },
    'colgroup':
        {
            'align': {
                'description': 'Aligns the content in a column group',
                'values': ['left', 'right', 'center', 'justify', 'char']
            },
            'char': {
                'description': 'Aligns the content in a column group to a '
                               'character',
                'values': None
            },
            'charoff': {
                'description': 'Sets the number of characters the content '
                               'will be aligned from the character specified '
                               'by the char attribute',
                'values': None
            },
            'span': {
                'description': 'Specifies the number of columns a column '
                               'group should span',
                'values': None
            },
            'valign': {
                'description': 'Vertical aligns the content in a column group',
                'values': ['top', 'middle', 'bottom', 'baseline']
            },
            'width': {
                'description': 'Specifies the width of a column group',
                'values': None
            }
        },
    'div':
        {
            'align': {
                'description': 'Specifies the alignment of the content inside '
                               'a <div> element',
                'values': ['left', 'right', 'center', 'justify']
            }
        },
    'form':
        {
            'autocomplete': {
                'description': 'Specifies whether a form should have '
                               'autocomplete on or off',
                'values': ['on', 'off']
            },
            'enctype': {
                'description': 'Specifies how the form-data should be encoded '
                               'when submitting it to the server (only for '
                               'method="post")',
                'values': ['application/x-www-form-urlencoded',
                           'multipart/form-data',
                           'text/plain']
            },
            'method': {
                'description': 'Specifies the HTTP method to use when sending '
                               'form-data',
                'values': ['get', 'post']
            }
        },
    'frame':
        {
            'frameborder': {
                'description': 'Specifies whether or not to display a border '
                               'around a frame',
                'values': ['0', '1']
            },
            'longdesc': {
                'description': 'Specifies a page that contains a long '
                               'description of the content of a frame',
                'values': None
            },
            'marginheight': {
                'description': 'Specifies the top and bottom margins of a '
                               'frame',
                'values': None
            },
            'marginwidth': {
                'description': 'Specifies the left and right margins of a '
                               'frame',
                'values': None
            },
            'name': {
                'description': 'Specifies the name of a frame',
                'values': None
            },
            'noresize': {
                'description': 'Specifies that a frame is not resizable',
                'values': ['noresize']
            },
            'scrolling': {
                'description': 'Specifies whether or not to display scrollbars'
                               ' in a frame',
                'values': ['yes', 'no', 'auto']
            },
            'src': {
                'description': 'Specifies the URL of the document to show in a'
                               ' frame',
                'values': None
            }
        }
}
