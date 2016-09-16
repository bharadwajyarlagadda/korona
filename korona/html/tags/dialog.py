# -*- coding: utf-8 -*-
"""Module for constructing <dialog> tag."""

from ...templates.html.tags import dialog_tag


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
