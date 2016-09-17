# -*- coding: utf-8 -*-
"""<fieldset> template"""

from ..environment import env

fieldset = env.from_string("""\
<fieldset {% if form -%} form="{{ form }}" {% endif -%}
          {% if name -%} name="{{ name }}" {% endif -%}
          {% if disabled -%} disabled {% endif -%}></fieldset>
""")
