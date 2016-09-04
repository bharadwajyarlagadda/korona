# -*- coding: utf-8 -*-
"""Templates for all the html tags."""

from .environment import env

anchor_tag = env.from_string("""\
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
   {%- if text -%} {{ text }} {%- endif -%}
</a>
""")

abbr_tag = env.from_string("""\
<abbr>{%- if text -%} {{ text }} {%- endif -%}</abbr>
""")

acronym_tag = env.from_string("""\
<acronym>{%- if text -%} {{ text }} {%- endif -%}</acronym>
""")

address_tag = env.from_string("""\
<address>{%- if text -%} {{ text }} {%- endif -%}</address>
""")

area_tag = env.from_string("""\
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

article_tag = env.from_string("""\
<article>{%- if text -%} {{ text }} {%- endif -%}</article>
""")

bold_tag = env.from_string("""\
<b>{%- if text -%} {{ text }} {%- endif -%}</b>
""")

base_tag = env.from_string("""\
<base {% if href -%} href="{{ href }}" {% endif -%}
      {% if target -%} target="{{ target }}" {% endif -%}>
""")

button_tag = env.from_string("""\
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

canvas_tag = env.from_string("""\
<canvas {% if height -%} height="{{ height }}" {% endif -%}
        {% if width -%} width="{{ width }}" {% endif -%}></canvas>
""")

caption_tag = env.from_string("""\
<caption {% if align -%} align="{{ align }}" {% endif -%}>
         {%- if text -%} {{ text }} {%- endif -%}</caption>
""")

cite_tag = env.from_string("""\
<cite>{%- if text -%} {{ text }} {%- endif -%}</cite>
""")

col_tag = env.from_string("""\
<col {% if align -%} align="{{ align }}" {% endif -%}
     {% if char -%} char="{{ char }}" {% endif -%}
     {% if charoff -%} charoff="{{ charoff }}" {% endif -%}
     {% if span -%} span="{{ span }}" {% endif -%}
     {% if valign -%} valign="{{ valign }}" {% endif -%}
     {% if width -%} width="{{ width }}" {% endif -%}>
""")

colgroup_tag = env.from_string("""\
<colgroup {% if span -%} span="{{ span }}" {% endif -%}
          {% if align -%} align="{{ align }}" {% endif -%}
          {% if char -%} char="{{ char }}" {% endif -%}
          {% if charoff -%} charoff="{{ charoff }}" {% endif -%}
          {% if valign -%} valign="{{ valign }}" {% endif -%}
          {% if width -%} width="{{ width }}" {% endif -%}></colgroup>
""")

dd_tag = env.from_string("""\
<dd>{%- if text -%} {{ text }} {%- endif -%}</dd>
""")

del_tag = env.from_string("""\
<del {% if cite -%} cite="{{ cite }}" {% endif -%}
     {% if datetime -%} datetime="{{ datetime }}" {% endif -%}>
     {%- if text -%} {{ text }} {%- endif -%}</del>
""")

details_tag = env.from_string("""\
<details {% if open -%} open {% endif -%}>
         {%- if text -%} {{ text}} {%- endif -%}</details>
""")

dialog_tag = env.from_string("""\
<dialog {% if open -%} open {% endif -%}>
        {%- if text -%} {{ text }} {%- endif -%}</dialog>
""")

div_tag = env.from_string("""\
<div {% if align -%} align="{{ align }}" {% endif -%}>
     {%- if text -%} {{ text }} {%- endif -%}</div>
""")

dl_tag = env.from_string("""\
<dl>{%- if text -%} {{ text }} {%- endif -%}</dl>
""")

dt_tag = env.from_string("""\
<dt>{%- if text -%} {{ text }} {%- endif -%}</dt>
""")

embed_tag = env.from_string("""\
<embed {% if src -%} src="{{ src }}" {% endif -%}
       {% if type -%} type="{{ type }}" {% endif -%}
       {% if width -%} width="{{ width }}" {% endif -%}
       {% if height -%} height="{{ height }}" {% endif -%}>
""")

fieldset_tag = env.from_string("""\
<fieldset {% if form -%} form="{{ form }}" {% endif -%}
          {% if name -%} name="{{ name }}" {% endif -%}
          {% if disabled -%} disabled {% endif -%}></fieldset>
""")

figure_tag = env.from_string("""\
<figure>{%- if text -%} {{ text }} {%- endif -%}</figure>
""")

footer_tag = env.from_string("""\
<footer>{%- if text -%} {{ text }} {%- endif -%}</footer>
""")

form_tag = env.from_string("""\
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

frame_tag = env.from_string("""\
<frame {% if src -%} src="{{ src }}" {% endif -%}
       {% if frameborder -%} frameborder="{{ frameborder }}" {% endif -%}
       {% if longdesc -%} longdesc="{{ longdesc }}" {% endif -%}
       {% if marginheight -%} marginheight="{{ marginheight }}" {% endif -%}
       {% if marginwidth -%} marginwidth="{{ marginwidth }}" {% endif -%}
       {% if name -%} name="{{ name }}" {% endif -%}
       {% if noresize -%} noresize="{{ noresize }}" {% endif -%}
       {% if scrolling -%} scrolling="{{ scrolling }}" {% endif -%}>
""")

frameset_tag = env.from_string("""\
<frameset {% if cols -%} cols="{{ cols }}" {% endif -%}
          {% if rows -%} rows="{{ rows }}" {% endif -%}></frameset>
""")
