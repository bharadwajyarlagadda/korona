# -*- coding: utf-8 -*-
"""<i> template"""

from ..environment import env

italics = env.from_string("""\
<i>{%- if text -%} {{ text }} {%- endif -%}</i>
""")
