# -*- coding: utf-8 -*-
"""<caption> template"""

from ..environment import env

caption = env.from_string("""\
<caption {% if align -%} align="{{ align }}" {% endif -%}>
         {%- if text -%} {{ text }} {%- endif -%}</caption>
""")
