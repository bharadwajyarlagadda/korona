# -*- coding: utf-8 -*-

from .environment import env

anchor_tag = env.from_string("""
<a {% if name -%} name="{{ name }}" {% endif -%}
   {% if rel -%} rel="{{ rel }}" {% endif -%}
   {% if rev -%} rev="{{ rev }}" {% endif -%}
   {% if charset -%} charset="{{ charset }}" {% endif -%}
   {% if href -%} href="{{ href }}" {% endif -%}
   {% if type -%} type="{{ type }}" {% endif -%}
   {% if hreflang -%} hreflang="{{ hreflang }}" {% endif -%}
   {% if target -%} target="{{ target }}" {% endif -%}
   {% if shape -%} shape="{{ shape }}" {% endif -%}
   {% if coords -%} coords="{{ coords }}" {% endif -%}
   {% if download -%} download="{{ download }}" {% endif -%}>
   {% if text -%} {{ text }} {% endif -%}
</a>
""")

abbr_tag = env.from_string("""
<abbr>{% if text -%} {{ text }}{% endif -%}</abbr>
""")

acronym_tag = env.from_string("""
<acronym>{% if text -%} {{ text }}{% endif -%}</acronym>
""")

bold_tag = env.from_string("""
<b>{% if text -%} {{ text }}{% endif -%}</b>
""")
