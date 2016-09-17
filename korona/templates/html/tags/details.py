# -*- coding: utf-8 -*-
"""<details> template"""

from ..environment import env

details = env.from_string("""\
<details {% if open -%} open {% endif -%}>
         {%- if text -%} {{ text}} {%- endif -%}</details>
""")
