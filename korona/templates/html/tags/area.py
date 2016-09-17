# -*- coding: utf-8 -*-
"""<area> template"""

from ..environment import env

area = env.from_string("""\
<area {% if shape -%} shape="{{ shape }}" {% endif -%}
      {% if coords -%} coords="{{ coords }}" {% endif -%}
      {% if href -%} href="{{ href }}" {% endif -%}
      {% if type -%} type="{{ type }}" {% endif -%}
      {% if hreflang -%} hreflang="{{ hreflang }}" {% endif -%}
      {% if alt -%} alt="{{ alt }}" {% endif -%}
      {% if media -%} media="{{ media }}" {% endif -%}
      {% if rel -%} rel="{{ rel }}" {% endif -%}
      {% if nohref -%} nohref {% endif -%}
      {% if download -%} download="{{ download }}" {% endif -%}
      {% if target -%} target="{{ target }}" {% endif -%}>
""")
