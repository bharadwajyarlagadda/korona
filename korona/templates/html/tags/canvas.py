# -*- coding: utf-8 -*-
"""<canvas> template"""

from ..environment import env

canvas = env.from_string("""\
<canvas {% if height -%} height="{{ height }}" {% endif -%}
        {% if width -%} width="{{ width }}" {% endif -%}></canvas>
""")
