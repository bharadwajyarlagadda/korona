# -*- coding: utf-8 -*-
"""<cite> template"""

from ..environment import env

cite = env.from_string("""\
<cite>{%- if text -%} {{ text }} {%- endif -%}</cite>
""")
