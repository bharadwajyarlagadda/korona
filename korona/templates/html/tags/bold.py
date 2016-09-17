# -*- coding: utf-8 -*-
"""<b> template"""

from ..environment import env

bold = env.from_string("""\
<b>{%- if text -%} {{ text }} {%- endif -%}</b>
""")
