# -*- coding: utf-8 -*-
"""<colgroup> template"""

from ..environment import env

colgroup = env.from_string("""\
<colgroup {% if span -%} span="{{ span }}" {% endif -%}
          {% if align -%} align="{{ align }}" {% endif -%}
          {% if char -%} char="{{ char }}" {% endif -%}
          {% if charoff -%} charoff="{{ charoff }}" {% endif -%}
          {% if valign -%} valign="{{ valign }}" {% endif -%}
          {% if width -%} width="{{ width }}" {% endif -%}></colgroup>
""")
