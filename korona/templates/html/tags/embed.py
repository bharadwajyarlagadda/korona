# -*- coding: utf-8 -*-
"""<embed> template"""

from ..environment import env

embed = env.from_string("""\
<embed {% if src -%} src="{{ src }}" {% endif -%}
       {% if type -%} type="{{ type }}" {% endif -%}
       {% if width -%} width="{{ width }}" {% endif -%}
       {% if height -%} height="{{ height }}" {% endif -%}>
""")
