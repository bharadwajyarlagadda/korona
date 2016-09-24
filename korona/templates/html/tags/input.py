# -*- coding: utf-8 -*-
"""<input> template"""

from ..environment import env

input = env.from_string("""\
<input {% if type -%} type="{{ type }}" {% endif -%}
       {% if name -%} name="{{ name }}" {% endif -%}
       {% if value -%} value="{{ value }}" {% endif -%}
       {% if min -%} min="{{ min }}" {% endif -%}
       {% if max -%} max="{{ max }}" {% endif -%}
       {% if maxlength -%} maxlength="{{ maxlength }}" {% endif -%}
       {% if dirname -%} dirname="{{ dirname }}" {% endif -%}
       {% if accept -%} accept="{{ accept }}" {% endif -%}
       {% if src -%} src="{{ src }}" {% endif -%}
       {% if alt -%} alt="{{ alt }}" {% endif -%}
       {% if align -%} align="{{ align }}" {% endif -%}
       {% if width -%} width="{{ width }}" {% endif -%}
       {% if height -%} height="{{ height }}" {% endif -%}
       {% if size -%} size="{{ size }}" {% endif -%}
       {% if step -%} step="{{ step }}" {% endif -%}
       {% if pattern -%} pattern="{{ pattern }}" {% endif -%}
       {% if placeholder -%} placeholder="{{ placeholder }}" {% endif -%}
       {% if form -%} form="{{ form }}" {% endif -%}
       {% if formaction -%} formaction="{{ formaction }}" {% endif -%}
       {% if formenctype -%} formenctype="{{ formenctype }}" {% endif -%}
       {% if formmethod -%} formmethod="{{ formmethod }}" {% endif -%}
       {% if formtarget -%} formtarget="{{ formtarget }}" {% endif -%}
       {% if list -%} list="{{ list }}" {% endif -%}
       {% if autocomplete -%} autocomplete="{{ autocomplete }}" {% endif -%}
       {% if multiple -%} multiple {% endif -%}
       {% if readonly -%} readonly {% endif -%}
       {% if required -%} required {% endif -%}
       {% if formnovalidate -%} formnovalidate {% endif -%}
       {% if disabled -%} disabled {% endif -%}
       {% if checked -%} checked {% endif -%}
       {% if autofocus -%} autofocus {% endif -%}>
""")
