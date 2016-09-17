# -*- coding: utf-8 -*-
"""<base> template"""

from ..environment import env

base = env.from_string("""\
<base {% if href -%} href="{{ href }}" {% endif -%}
      {% if target -%} target="{{ target }}" {% endif -%}>
""")
