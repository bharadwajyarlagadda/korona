# -*- coding: utf-8 -*-
"""Module for constructing <fieldset> tag."""

from __future__ import absolute_import

from ...templates.html.tags import fieldset


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
        return fieldset.render(self.values)
