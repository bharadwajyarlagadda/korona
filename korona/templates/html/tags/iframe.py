# -*- coding: utf-8 -*-
"""<iframe> template"""

from ..environment import env

iframe = env.from_string("""\
<iframe {% if src -%} src="{{ src }}" {% endif -%}
        {% if width -%} width="{{ width }}" {% endif -%}
        {% if height -%} height="{{ height }}" {% endif -%}
        {% if align -%} align="{{ align }}" {% endif -%}
        {% if frameborder -%} frameborder="{{ frameborder }}" {% endif -%}
        {% if longdesc -%} longdesc="{{ longdesc }}" {% endif -%}
        {% if marginheight -%} marginheight="{{ marginheight }}" {% endif -%}
        {% if marginwidth -%} marginwidth="{{ marginwidth }}" {% endif -%}
        {% if name -%} name="{{ name }}" {% endif -%}
        {% if sandbox -%} sandbox="{{ sandbox }}" {% endif -%}
        {% if scrolling -%} scrolling="{{ scrolling }}" {% endif -%}
        {% if srcdoc -%} srcdoc="{{ srcdoc }}" {% endif -%}></iframe>
""")
