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
        },
    'h1':
        {
            'align': {
                'description': 'Specifies the alignment of a heading',
                'values': ['left', 'center', 'right', 'justify']
            }
        },
    'h2':
        {
            'align': {
                'description': 'Specifies the alignment of a heading',
                'values': ['left', 'center', 'right', 'justify']
            }
        },
    'h3':
        {
            'align': {
                'description': 'Specifies the alignment of a heading',
                'values': ['left', 'center', 'right', 'justify']
            }
        },
    'h4':
        {
            'align': {
                'description': 'Specifies the alignment of a heading',
                'values': ['left', 'center', 'right', 'justify']
            }
        },
    'h5':
        {
            'align': {
                'description': 'Specifies the alignment of a heading',
                'values': ['left', 'center', 'right', 'justify']
            }
        },
    'h6':
        {
            'align': {
                'description': 'Specifies the alignment of a heading',
                'values': ['left', 'center', 'right', 'justify']
            }
        },
    'hr':
        {
            'align': {
                'description': 'Specifies the alignment of a <hr> element',
                'values': ['left', 'center', 'right']
            },
            'noshade': {
                'description': 'Specifies that a <hr> element should render in'
                               ' one solid color (noshaded), instead of a '
                               'shaded color',
                'values': None
            },
            'size': {
                'description': 'Specifies the height of a <hr> element',
                'values': None
            },
            'width': {
                'description': 'Specifies the width of a <hr> element',
                'values': None
            }
        },
    'iframe':
        {
            'align': {
                'description': 'Specifies the alignment of an <iframe> '
                               'according to surrounding elements',
                'values': ['left', 'right', 'middle', 'top', 'bottom']
            },
            'frameborder': {
                'description': 'Specifies whether or not to display a border '
                               'around an <iframe>',
                'values': ['1', '0']
            },
            'height': {
                'description': 'Specifies the height of an <iframe>',
                'values': None
            },
            'longdesc': {
                'description': 'Specifies a page that contains a long '
                               'description of the content of an <iframe>',
                'values': None
            },
            'marginheight': {
                'description': 'Specifies the top and bottom margins of the '
                               'content of an <iframe>',
                'values': None
            },
            'marginwidth': {
                'description': 'Specifies the left and right margins of the '
                               'content of an <iframe>',
                'values': None
            },
            'name': {
                'description': 'Specifies the name of an <iframe>',
                'values': None
            },
            'sandbox': {
                'description': 'Enables an extra set of restrictions for the '
                               'content in an <iframe>',
                'values': ['',
                           'allow-forms',
                           'allow-pointer-lock',
                           'allow-popups',
                           'allow-same-origin',
                           'allow-scripts',
                           'allow-top-navigation']
            },
            'scrolling': {
                'description': 'Specifies whether or not to display scrollbars'
                               ' in an <iframe>',
                'values': ['yes', 'no', 'auto']
            },
            'src': {
                'description': 'Specifies the address of the document to embed'
                               ' in the <iframe>',
                'src': None
            },
            'srcdoc': {
                'description': 'Specifies the HTML content of the page to show'
                               ' in the <iframe>',
                'values': None
            },
            'width': {
                'description': 'Specifies the width of an <iframe>',
                'values': None
            }
        },
    'img':
        {
            'align': {
                'description': 'Specifies the alignment of an image according '
                               'to surrounding elements',
                'values': ['left', 'right', 'middle', 'top', 'bottom']
            },
            'alt': {
                'description': 'Specifies an alternate text for an image',
                'values': None
            },
            'border': {
                'description': 'Specifies the width of the border around an '
                               'image',
                'values': None
            },
            'crossorigin': {
                'description': 'Allow images from third-party sites that allow'
                               ' cross-origin access to be used with canvas',
                'values': None
            },
            'height': {
                'description': 'Specifies the height of an image',
                'values': None
            },
            'hspace': {
                'description': 'Specifies the whitespace on left and right '
                               'side of an image',
                'values': None
            },
            'ismap': {
                'description': 'Specifies an image as a server-side image-map',
                'values': None
            },
            'longdesc': {
                'description': 'Specifies a URL to a detailed description of '
                               'an image',
                'values': None
            },
            'src': {
                'description': 'Specifies the URL of an image',
                'values': None
            },
            'usemap': {
                'description': 'Specifies an image as a client-side image-map',
                'values': None
            },
            'vspace': {
                'description': 'Specifies the whitespace on top and bottom of '
                               'an image',
                'values': None
            },
            'width': {
                'description': 'Specifies the width of an image',
                'values': None
            }
        },
    'input':
        {
            'accept': {
                'description': 'Specifies the types of files that the server '
                               'accepts (only for type="file")',
                'values': None
            },
            'align': {
                'description': 'Specifies the alignment of an image input '
                               '(only for type="image")',
                'values': ['left', 'right', 'top', 'middle', 'bottom']
            },
            'alt': {
                'description': 'Specifies an alternate text for images (only '
                               'for type="image")',
                'values': None
            },
            'autocomplete': {
                'description': 'Specifies whether an <input> element should '
                               'have autocomplete enabled',
                'values': ['on', 'off']
            },
            'autofocus': {
                'description': 'Specifies that an <input> element should '
                               'automatically get focus when the page loads',
                'values': None
            },
            'checked': {
                'description': 'Specifies that an <input> element should be '
                               'pre-selected when the page loads (for '
                               'type="checkbox" or type="radio")',
                'values': None
            },
            'dirname': {
                'description': 'Specifies that the text direction will be '
                               'submitted',
                'values': None
            },
            'disabled': {
                'description': 'Specifies that an <input> element should be '
                               'disabled',
                'values': None
            },
            'form': {
                'description': 'Specifies one or more forms the <input> '
                               'element belongs to',
                'values': None
            },
            'formaction': {
                'description': 'Specifies the URL of the file that will '
                               'process the input control when the form is '
                               'submitted (for type="submit" and '
                               'type="image")',
                'values': None
            },
            'formenctype': {
                'description': 'Specifies how the form-data should be encoded '
                               'when submitting it to the server (for type='
                               '"submit" and type="image")',
                'values': ['application/x-www-form-urlencoded',
                           'multipart/form-data',
                           'text/plain']
            },
            'formmethod': {
                'description': 'Defines the HTTP method for sending data to '
                               'the action URL (for type="submit" and type='
                               '"image")',
                'values': ['get', 'post']
            },
            'formnovalidate': {
                'description': 'Defines that form elements should not be '
                               'validated when submitted',
                'values': None
            },
            'formtarget': {
                'description': 'Specifies where to display the response that '
                               'is received after submitting the form (for '
                               'type="submit" and type="image")',
                'values': None
            },
            'height': {
                'description': 'Specifies the height of an <input> element '
                               '(only for type="image")',
                'values': None
            },
            'list': {
                'description': 'Refers to a <datalist> element that contains '
                               'pre-defined options for an <input> element',
                'values': None
            },
            'max': {
                'description': 'Specifies the maximum value for an <input> '
                               'element',
                'values': None
            },
            'maxlength': {
                'description': 'Specifies the maximum number of characters '
                               'allowed in an <input> element',
                'values': None
            },
            'min': {
                'description': 'Specifies a minimum value for an <input> '
                               'element',
                'values': None
            },
            'multiple': {
                'description': 'Specifies that a user can enter more than one '
                               'value in an <input> element',
                'values': None
            },
            'name': {
                'description': 'Specifies the name of an <input> element',
                'values': None
            },
            'pattern': {
                'description': "Specifies a regular expression that an <input>"
                               " element's value is checked against",
                'values': None
            },
            'placeholder': {
                'description': 'Specifies a short hint that describes the '
                               'expected value of an <input> element',
                'values': None
            },
            'readonly': {
                'description': 'Specifies that an input field is read-only',
                'values': None
            },
            'required': {
                'description': 'Specifies that an input field must be filled '
                               'out before submitting the form',
                'values': None
            },
            'size': {
                'description': 'Specifies the width, in characters, of an '
                               '<input> element',
                'values': None
            },
            'src': {
                'description': 'Specifies the URL of the image to use as a '
                               'submit button (only for type="image")',
                'values': None
            },
            'step': {
                'description': 'Specifies the legal number intervals for an '
                               'input field',
                'values': None
            },
            'type': {
                'description': 'Specifies the type <input> element to display',
                'values': ['button',
                           'checkbox',
                           'color',
                           'date',
                           'datetime',
                           'datetime-local',
                           'email',
                           'file',
                           'hidden',
                           'image',
                           'month',
                           'number',
                           'password',
                           'radio',
                           'range',
                           'reset',
                           'search',
                           'submit',
                           'tel',
                           'text',
                           'time',
                           'url',
                           'week']
            },
            'value': {
                'description': 'Specifies the value of an <input> element',
                'values': None
            },
            'width': {
                'description': 'Specifies the width of an <input> element '
                               '(only for type="image")',
                'values': None
            }
        }
}
