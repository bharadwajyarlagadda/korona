# -*- coding: utf-8 -*-
"""<img> template"""

from ..environment import env

img = env.from_string("""\
<img {% if align -%} align="{{ align }}" {% endif -%}
     {% if alt -%} alt="{{ alt }}" {% endif -%}
     {% if border -%} border="{{ border }}" {% endif -%}
     {% if crossorigin -%} crossorigin="{{ crossorigin }}" {% endif -%}
     {% if height -%} height="{{ height }}" {% endif -%}
     {% if hspace -%} hspace="{{ hspace }}" {% endif -%}
     {% if ismap -%} ismap {% endif -%}
     {% if longdesc -%} longdesc="{{ longdesc }}" {% endif -%}
     {% if src -%} src="{{ src }}" {% endif -%}
     {% if usemap -%} usemap="{{ usemap }}" {% endif -%}
     {% if vspace -%} vspace="{{ vspace }}" {% endif -%}
     {% if width -%} width="{{ width }}" {% endif -%}>
""")
