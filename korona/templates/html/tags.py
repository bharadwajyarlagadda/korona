# -*- coding: utf-8 -*-

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
