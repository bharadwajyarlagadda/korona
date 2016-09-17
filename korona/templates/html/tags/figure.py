# -*- coding: utf-8 -*-
"""<figure> template"""

from ..environment import env

figure = env.from_string("""\
<figure>{%- if text -%} {{ text }} {%- endif -%}</figure>
""")
