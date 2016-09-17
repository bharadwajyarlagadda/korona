# -*- coding: utf-8 -*-
"""<col> template"""

from ..environment import env

col = env.from_string("""\
<col {% if align -%} align="{{ align }}" {% endif -%}
     {% if char -%} char="{{ char }}" {% endif -%}
     {% if charoff -%} charoff="{{ charoff }}" {% endif -%}
     {% if span -%} span="{{ span }}" {% endif -%}
     {% if valign -%} valign="{{ valign }}" {% endif -%}
     {% if width -%} width="{{ width }}" {% endif -%}>
""")
