# -*- coding: utf-8 -*-
"""<hr> template"""

from ..environment import env

hr = env.from_string("""\
<hr {% if align -%} align="{{ align }}" {% endif -%}
    {% if noshade -%} noshade {% endif -%}
    {% if width -%} width="{{ width }}" {% endif -%}
    {% if size -%} size="{{ size }}" {% endif -%}>
""")
