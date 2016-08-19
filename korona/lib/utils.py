from ..html.tags import TAGS


def validate_tag(tag=None):
    """Validates whether the given tag is supported by korona or not."""
    if not tag:
        raise AttributeError('Tag cannot be empty')

    if tag not in TAGS:
        raise ValueError('{0} tag is not supported')
