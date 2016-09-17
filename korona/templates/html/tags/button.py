# -*- coding: utf-8 -*-
"""<button> template"""

from ..environment import env

button = env.from_string("""\
<button {% if name -%} name="{{ name }}" {% endif -%}
        {% if type -%} type="{{ type }}" {% endif -%}
        {% if value -%} value="{{ value }}" {% endif -%}
        {% if form -%} form="{{ form }}" {% endif -%}
        {% if formaction -%} formaction="{{ formaction }}" {% endif -%}
        {% if formenctype -%} formenctype="{{ formenctype }}" {% endif -%}
        {% if formmethod -%} formmethod="{{ formmethod }}" {% endif -%}
        {% if formtarget -%} formtarget="{{ formtarget }}" {% endif -%}
        {% if formnovalidate -%} formnovalidate {% endif -%}
        {% if disabled -%} disabled {% endif -%}
        {% if autofocus -%} autofocus {% endif -%}>
        {%- if text -%} {{ text }} {%- endif -%}</button>
""")
