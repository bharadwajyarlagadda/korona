# -*- coding: utf-8 -*-
"""<address> template"""

from ..environment import env

address = env.from_string("""\
<address>{%- if text -%} {{ text }} {%- endif -%}</address>
""")
