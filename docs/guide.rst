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


.. note:: korona only supports ``text`` attribute for ``<abbr>`` tag.

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
