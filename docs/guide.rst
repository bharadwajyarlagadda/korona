User's Guide
============

Korona helps you to build html pages.

Korona also helps you to build individual html tags.

<a>
---

Korona supports some of the anchor tag attributes like:

- ``charset``
- ``coords``
- ``download``
- ``href``
- ``hreflang``
- ``name``
- ``rel``
- ``rev``
- ``shape``
- ``target``
- ``type``
- ``text`` (The text as in <a>{text}</a>)

Korona can build an anchor tag.

.. code-block:: python

    from korona.html.construct import A

    attributes = {'charset': 'UTF-8', 'href': 'www.google.com', 'hreflang': 'en', 'text': 'google'}

    # You can pass in the attributes in the form of a dictionary.
    anchor1 = A(**attributes)
    # You can also pass in the attributes as args.
    anchor2 = A(charset='UTF-8', href='www.google.com', hreflang='en', text='google')
    anchor_tag1 = anchor1.construct_tag()
    anchor_tag2 = anchor2.construct_tag()

    assert anchor_tag1 == '<a charset="UTF-8" href="www.google.com" hreflang="en" >google</a>'
    assert anchor_tag1 == anchor_tag2


<abbr>
------

Korona builds an <abbr> tag.

.. code-block:: python

    from korona.html.construct import Abbr

    attributes = {'text': 'WHO'}

    # You can pass in the attributes in the form of a dictionary.
    abbreviate1 = Abbr(**attributes)
    # You can also pass in the attributes as args.
    abbreviate2 = Abbr(text='WHO')
    abbreviate_tag1 = abbreviate1.construct_tag()
    abbreviate_tag2 = abbreviate2.construct_tag()

    assert abbreviate_tag1 == '<abbr>WHO</abbr>'
    assert abbreviate_tag1 == abbreviate_tag2


.. note:: korona only supports ``text`` attribute for ``<abbr>`` tag for now.

<acronym>
---------

Korona builds an <acronym> tag.

.. code-block:: python

    from korona.html.construct import Acronym

    attributes = {'text': 'ASAP'}

    # You can pass in the attributes in the form of a dictionary.
    acronym1 = Acronym(**attributes)
    # You can also pass in the attributes as args.
    acronym2 = Acronym(text='ASAP')
    acronym_tag1 = acronym1.construct_tag()
    acronym_tag2 = acronym2.construct_tag()

    assert acronym_tag1 == '<acronym>ASAP</acronym>'
    assert acronym_tag1 == acronym_tag2


.. note:: korona only supports ``text`` attribute for ``<acronym>`` tag for now.

<area>
------

Korona supports some of the anchor tag attributes like:

- ``alt``
- ``coords``
- ``download``
- ``href``
- ``hreflang``
- ``media``
- ``nohref``
- ``rel``
- ``shape``
- ``target``
- ``type``

Korona can build an <area> tag.

.. code-block:: python

    from korona.html.construct import Area

    attributes = {'href': 'www.example.com', 'hreflang': 'en', 'alt': 'example'}

    # You can pass in the attributes in the form of a dictionary.
    area1 = Area(**attributes)
    # You can also pass in the attributes as args.
    area2 = Area(href='www.example.com', hreflang='en', alt='example')

    area_tag1 = area1.construct_tag()
    area_tag2 = area2.construct_tag()

    assert area_tag1 == '<area href="www.example.com" hreflang="en" alt="example" >
    assert area_tag1 == area_tag2

<b>
---

Korona can build <b> tag.

.. code-block:: python

    from korona.html.construct import B

    attributes = {'text': 'example'}

    # You can pass in the attributes in the form of a dictionary.
    bold1 = B(**attributes)
    # You can also pass in the attributes as args.
    bold2 = B(text='example')

    bold_tag1 = bold1.construct_tag()
    bold_tag2 = bold2.construct_tag()

    assert bold_tag1 == '<b>example</b>'
    assert bold_tag1 == bold_tag2


<base>
------

Korona can build <base> tag.

.. code-block:: python

    from koron.html.construct import Base

    attributes = {'href': 'www.google.com', 'target': 'example'}

    # You can pass in the attributes in the form of a dictionary.
    base1 = Base(**attributes)
    # You can also pass in the attributes as args.
    base2 = Base(href='www.google.com', target='example')

    base_tag1 = base1.construct_tag()
    base_tag2 = base2.construct_tag()

    assert base_tag1 == '<base href="www.google.com" target="example" >'
    assert base_tag1 == base_tag2

<canvas>
--------

Korona can build <canvas> tag.

.. code-block:: python

    from koron.html.construct import Canvas

    attributes = {'height': '100', 'width': '200'}

    # You can pass in the attributes in the form of a dictionary.
    canvas1 = Canvas(**attributes)
    # You can also pass in the attributes as args.
    canvas2 = Canvas(height='100', width='200')

    canvas_tag1 = canvas1.construct_tag()
    canvas_tag2 = canvas2.construct_tag()

    assert canvas_tag1 == '<canvas height="100" width="200" ></canvas>'
    assert canvas_tag1 == canvas_tag2

.. note:: korona doesn't support canvas ``text`` for now.

<caption>
---------

Korona can build <caption> tag.

.. code-block:: python

    from koron.html.construct import Caption

    attributes = {'align': 'top', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    caption1 = Caption(**attributes)
    # You can also pass in the attributes as args.
    caption2 = Caption(align='top', text='abcd')

    caption_tag1 = caption1.construct_tag()
    caption_tag2 = caption2.construct_tag()

    assert caption_tag1 == '<caption align="top" >abcd</caption>'
    assert caption_tag1 == caption_tag2

<cite>
------

Korona can build <cite> tag.

.. code-block:: python

    from koron.html.construct import Cite

    attributes = {'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    cite1 = Cite(**attributes)
    # You can also pass in the attributes as args.
    cite2 = Cite(text='abcd')

    cite_tag1 = cite1.construct_tag()
    cite_tag2 = cite2.construct_tag()

    assert cite_tag1 == '<cite>abcd </cite>'
    assert cite_tag1 == cite_tag2
