# -*- coding: utf-8 -*-
"""<frame> template"""

from ..environment import env

frame = env.from_string("""\
<frame {% if src -%} src="{{ src }}" {% endif -%}
       {% if frameborder -%} frameborder="{{ frameborder }}" {% endif -%}
       {% if longdesc -%} longdesc="{{ longdesc }}" {% endif -%}
       {% if marginheight -%} marginheight="{{ marginheight }}" {% endif -%}
       {% if marginwidth -%} marginwidth="{{ marginwidth }}" {% endif -%}
       {% if name -%} name="{{ name }}" {% endif -%}
       {% if noresize -%} noresize="{{ noresize }}" {% endif -%}
       {% if scrolling -%} scrolling="{{ scrolling }}" {% endif -%}>
""")
