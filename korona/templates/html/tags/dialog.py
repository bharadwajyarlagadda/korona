# -*- coding: utf-8 -*-
"""<dialog> template"""

from ..environment import env

dialog = env.from_string("""\
<dialog {% if open -%} open {% endif -%}>
        {%- if text -%} {{ text }} {%- endif -%}</dialog>
""")
