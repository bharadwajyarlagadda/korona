# -*- coding: utf-8 -*-
"""<frameset> template"""

from ..environment import env

frameset = env.from_string("""\
<frameset {% if cols -%} cols="{{ cols }}" {% endif -%}
          {% if rows -%} rows="{{ rows }}" {% endif -%}></frameset>
""")
