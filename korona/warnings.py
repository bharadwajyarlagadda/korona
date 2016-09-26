# -*- coding: utf-8 -*-
"""Module for warnings to be used in Korona."""

import warnings

STACK_LEVEL = 3


def warn(warning):
    """Displays warning messages to the user."""
    warnings.simplefilter('always', UserWarning)
    warnings.warn(warning, stacklevel=STACK_LEVEL)
