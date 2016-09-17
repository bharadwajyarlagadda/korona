# -*- coding: utf-8 -*-
"""Templates for heading tags <h1>, <h2>, <h3>, <h4>, <h5>, <h6>"""

from ..environment import env

h1 = env.from_string("""\
<h1 {% if align -%} align="{{ align }}" {% endif -%}>
    {%- if text -%} {{ text }} {%- endif -%}</h1>
""")

h2 = env.from_string("""\
<h2 {% if align -%} align="{{ align }}" {% endif -%}>
    {%- if text -%} {{ text }} {%- endif -%}</h2>
""")

h3 = env.from_string("""\
<h3 {% if align -%} align="{{ align }}" {% endif -%}>
    {%- if text -%} {{ text }} {%- endif -%}</h3>
""")

h4 = env.from_string("""\
<h4 {% if align -%} align="{{ align }}" {% endif -%}>
    {%- if text -%} {{ text }} {%- endif -%}</h4>
""")

h5 = env.from_string("""\
<h5 {% if align -%} align="{{ align }}" {% endif -%}>
    {%- if text -%} {{ text }} {%- endif -%}</h5>
""")

h6 = env.from_string("""\
<h6 {% if align -%} align="{{ align }}" {% endif -%}>
    {%- if text -%} {{ text }} {%- endif -%}</h6>
""")
