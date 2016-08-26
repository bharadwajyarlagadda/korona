# -*- coding: utf-8 -*-

GLOBAL_ATTRIBUTES = []


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
    'caption':
        {
            'align': {
                'description': 'Defines the alignment of the caption',
                'values': ['left', 'right', 'top', 'bottom']
            }
        }
}
