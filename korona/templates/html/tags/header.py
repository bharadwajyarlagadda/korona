# -*- coding: utf-8 -*-
"""<header> template"""

from ..environment import env

header = env.from_string("""\
<header>{%- if text -%} {{ text }} {%- endif -%}</header>
""")
