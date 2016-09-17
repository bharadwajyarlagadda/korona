# -*- coding: utf-8 -*-
"""<head> template"""

from ..environment import env

head = env.from_string("""\
<head>{%- if text -%} {{ text }} {%- endif -%}</head>
""")
