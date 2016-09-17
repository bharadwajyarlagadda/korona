# -*- coding: utf-8 -*-
"""<div> template"""

from ..environment import env

div = env.from_string("""\
<div {% if align -%} align="{{ align }}" {% endif -%}>
     {%- if text -%} {{ text }} {%- endif -%}</div>
""")
