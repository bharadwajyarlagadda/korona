# -*- coding: utf-8 -*-
"""Template for constructing global attributes."""

from .environment import env

global_attributes = env.from_string("""\
{% if accesskey -%} accesskey="{{ accesskey }}" {% endif -%}
{% if class -%} class="{{ class }}" {% endif -%}
{% if contenteditable -%} contenteditable="{{ contenteditable }}" {% endif -%}
{% if contextmenu -%} contextmenu="{{ contextmenu }}" {% endif -%}
{% if dir -%} dir="{{ dir }}" {% endif -%}
{% if draggable -%} draggable="{{ draggable }}" {% endif -%}
{% if dropzone -%} dropzone="{{ dropzone }}" {% endif -%}
{% if hidden -%} hidden {% endif -%}
{% if id -%} id="{{ id }}" {% endif -%}
{% if lang -%} lang="{{ lang }}" {% endif -%}
{% if spellcheck -%} spellcheck="{{ spellcheck }}" {% endif -%}
{% if style -%} style="{{ style }}" {% endif -%}
{% if tabindex -%} tabindex="{{ tabindex }}" {% endif -%}
{% if title -%} title="{{ title }}" {% endif -%}
{% if translate -%} translate="{{ translate }}" {% endif -%}
""")
