# -*- coding: utf-8 -*-
"""<form> template"""

from ..environment import env

form = env.from_string("""\
<form {% if action -%} action="{{ action }}" {% endif -%}
      {% if accept -%} accept="{{ accept }}" {% endif -%}
      {% if method -%} method="{{ method }}" {% endif -%}
      {% if name -%} name="{{ name }}" {% endif -%}
      {% if autocomplete -%} autocomplete="{{ autocomplete }}" {% endif -%}
      {% if target -%} target="{{ target }}" {% endif -%}
      {% if enctype -%} enctype="{{ enctype }}" {% endif -%}
      {% if novalidate -%} novalidate {% endif -%}>
      {%- if text -%} {{ text }} {%- endif -%}</form>
""")
