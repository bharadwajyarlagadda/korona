# -*- coding: utf-8 -*-
"""<del> template"""

from ..environment import env

delete = env.from_string("""\
<del {% if cite -%} cite="{{ cite }}" {% endif -%}
     {% if datetime -%} datetime="{{ datetime }}" {% endif -%}>
     {%- if text -%} {{ text }} {%- endif -%}</del>
""")
