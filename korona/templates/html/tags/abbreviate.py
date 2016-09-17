# -*- coding: utf-8 -*-
"""<abbr> template"""

from ..environment import env

abbr = env.from_string("""\
<abbr>{%- if text -%} {{ text }} {%- endif -%}</abbr>
""")
