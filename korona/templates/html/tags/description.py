# -*- coding: utf-8 -*-
"""Templates for description tags <dd>, <dl> and <dt>"""

from ..environment import env

dd = env.from_string("""\
<dd>{%- if text -%} {{ text }} {%- endif -%}</dd>
""")

dl = env.from_string("""\
<dl>{%- if text -%} {{ text }} {%- endif -%}</dl>
""")

dt = env.from_string("""\
<dt>{%- if text -%} {{ text }} {%- endif -%}</dt>
""")
