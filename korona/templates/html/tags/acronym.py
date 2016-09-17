# -*- coding: utf-8 -*-
"""<acronym> template"""

from ..environment import env

acronym = env.from_string("""\
<acronym>{%- if text -%} {{ text }} {%- endif -%}</acronym>
""")
