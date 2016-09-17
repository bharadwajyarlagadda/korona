# -*- coding: utf-8 -*-
"""<footer> template"""

from ..environment import env

footer = env.from_string("""\
<footer>{%- if text -%} {{ text }} {%- endif -%}</footer>
""")
