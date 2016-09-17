# -*- coding: utf-8 -*-
"""<article> template"""

from ..environment import env

article = env.from_string("""\
<article>{%- if text -%} {{ text }} {%- endif -%}</article>
""")
