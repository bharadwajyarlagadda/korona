# -*- coding: utf-8 -*-
"""<html> template"""

from ..environment import env

html = env.from_string("""\
<html {% if manifest -%} manifest="{{ manifest }}" {% endif -%}
      {% if xmlns -%} xmlns="{{ xmlns }}" {% endif -%}>
      {%- if text -%} {{ text }} {%- endif -%}</html>
""")
