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
- ``text`` (text as in <a>{text}</a>)

Korona can build an anchor tag.

.. code-block:: python

    from korona.html.construct import A

    attributes = {'charset': 'UTF-8', 'href': 'www.google.com', 'hreflang': 'en', 'text': 'google'}

    # You can pass in the attributes in the form of a dictionary.
    anchor1 = A(**attributes)
    # You can also pass in the attributes as args.
    anchor2 = A(charset='UTF-8', href='www.google.com', hreflang='en', text='google')
    anchor_tag1 = anchor1.construct()
    anchor_tag2 = anchor2.construct()

    assert anchor_tag1 == '<a charset="UTF-8" href="www.google.com" hreflang="en" >google</a>'
    assert anchor_tag1 == anchor_tag2


<abbr>
------

Korona can build an <abbr> tag.

.. code-block:: python

    from korona.html.construct import Abbr

    attributes = {'text': 'WHO'}

    # You can pass in the attributes in the form of a dictionary.
    abbreviate1 = Abbr(**attributes)
    # You can also pass in the attributes as args.
    abbreviate2 = Abbr(text='WHO')
    abbreviate_tag1 = abbreviate1.construct()
    abbreviate_tag2 = abbreviate2.construct()

    assert abbreviate_tag1 == '<abbr>WHO </abbr>'
    assert abbreviate_tag1 == abbreviate_tag2


.. note:: korona only supports ``text`` attribute for ``<abbr>`` tag for now.

<acronym>
---------

Korona can build an <acronym> tag.

.. code-block:: python

    from korona.html.construct import Acronym

    attributes = {'text': 'ASAP'}

    # You can pass in the attributes in the form of a dictionary.
    acronym1 = Acronym(**attributes)
    # You can also pass in the attributes as args.
    acronym2 = Acronym(text='ASAP')
    acronym_tag1 = acronym1.construct()
    acronym_tag2 = acronym2.construct()

    assert acronym_tag1 == '<acronym>ASAP </acronym>'
    assert acronym_tag1 == acronym_tag2


.. note:: korona only supports ``text`` attribute for ``<acronym>`` tag for now.

<address>
---------

Korona can build an <address> tag.

.. code-block:: python

    from korona.html.construct import Address

    attributes = {'text': 'abcd@yahoo.com'}

    # You can pass in the attributes in the form of a dictionary.
    address1 = Address(**attributes)
    # You can also pass in the attributes as args.
    address2 = Address(text='abcd@yahoo.com')
    address_tag1 = address1.construct()
    address_tag2 = address2.construct()

    assert address_tag1 == '<address>abcd@yahoo.com </address>'
    assert address_tag1 == address_tag2

<area>
------

Korona supports some of the area tag attributes like:

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

    area_tag1 = area1.construct()
    area_tag2 = area2.construct()

    assert area_tag1 == '<area href="www.example.com" hreflang="en" alt="example" >
    assert area_tag1 == area_tag2

<article>
---------

Korona can build an <article> tag.

.. code-block:: python

    from korona.html.construct import Article

    attributes = {'text': '<p>Hi there</p>'}

    # You can pass in the attributes in the form of a dictionary.
    article1 = Article(**attributes)
    # You can also pass in the attributes as args.
    article2 = Article(text='<p>Hi there</p>')
    article_tag1 = article1.construct()
    article_tag2 = article2.construct()

    assert article_tag1 == '<article><p>Hi there</p> </article>'
    assert article_tag1 == article_tag2


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

    bold_tag1 = bold1.construct()
    bold_tag2 = bold2.construct()

    assert bold_tag1 == '<b>example </b>'
    assert bold_tag1 == bold_tag2


<base>
------

Korona can build <base> tag.

.. code-block:: python

    from korona.html.construct import Base

    attributes = {'href': 'www.google.com', 'target': 'example'}

    # You can pass in the attributes in the form of a dictionary.
    base1 = Base(**attributes)
    # You can also pass in the attributes as args.
    base2 = Base(href='www.google.com', target='example')

    base_tag1 = base1.construct()
    base_tag2 = base2.construct()

    assert base_tag1 == '<base href="www.google.com" target="example" >'
    assert base_tag1 == base_tag2

<button>
--------

Korona supports some of the button tag attributes like:

- ``autofocus``
- ``disabled``
- ``form``
- ``formaction``
- ``formenctype``
- ``formmethod``
- ``formnovalidate``
- ``formtarget``
- ``name``
- ``type``
- ``value``
- ``text`` (text as in <button>{text}</button>)

Korona can build <button> tag.

.. code-block:: python

    from korona.html.construct import Button

    attributes = {'name': 'HTML1',
                  'type': 'submit',
                  'value': 'HTML1',
                  'text': 'HTML1'}

    # You can pass in the attributes in the form of a dictionary.
    button1 = Button(**attributes)
    # You can also pass in the attributes as args.
    button2 = Button(name='HTML1', type='submit', value='HTML1', text='HTML1')

    button_tag1 = button1.construct()
    button_tag2 = button2.construct()

    assert button_tag1 == '<button name="HTML1" type="submit" value="HTML1" >HTML1</button>'
    assert button_tag1 == button_tag2


<canvas>
--------

Korona can build <canvas> tag.

.. code-block:: python

    from korona.html.construct import Canvas

    attributes = {'height': '100', 'width': '200'}

    # You can pass in the attributes in the form of a dictionary.
    canvas1 = Canvas(**attributes)
    # You can also pass in the attributes as args.
    canvas2 = Canvas(height='100', width='200')

    canvas_tag1 = canvas1.construct()
    canvas_tag2 = canvas2.construct()

    assert canvas_tag1 == '<canvas height="100" width="200" ></canvas>'
    assert canvas_tag1 == canvas_tag2

.. note:: korona doesn't support canvas ``text`` for now.

<caption>
---------

Korona can build <caption> tag.

.. code-block:: python

    from korona.html.construct import Caption

    attributes = {'align': 'top', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    caption1 = Caption(**attributes)
    # You can also pass in the attributes as args.
    caption2 = Caption(align='top', text='abcd')

    caption_tag1 = caption1.construct()
    caption_tag2 = caption2.construct()

    assert caption_tag1 == '<caption align="top" >abcd</caption>'
    assert caption_tag1 == caption_tag2

<cite>
------

Korona can build <cite> tag.

.. code-block:: python

    from korona.html.construct import Cite

    attributes = {'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    cite1 = Cite(**attributes)
    # You can also pass in the attributes as args.
    cite2 = Cite(text='abcd')

    cite_tag1 = cite1.construct()
    cite_tag2 = cite2.construct()

    assert cite_tag1 == '<cite>abcd </cite>'
    assert cite_tag1 == cite_tag2

<col>
-----

Korona supports some of the col tag attributes like:

- ``align``
- ``char``
- ``charoff``
- ``span``
- ``valign``
- ``width``

Korona can build <col> tag.

.. code-block:: python

    from korona.html.construct import Col

    attributes = {'align': 'char', 'char': '.', 'charoff': '2'}

    # You can pass in the attributes in the form of a dictionary.
    col1 = Col(**attributes)
    # You can also pass in the attributes as args.
    col2 = Col(align='char', char='.', charoff='2')

    col_tag1 = col1.construct()
    col_tag2 = col2.construct()

    assert col_tag1 == '<col align="char" char="." charoff="2" >'
    assert col_tag1 == col_tag2

<colgroup>
----------

Korona supports some of the colgroup tag attributes like:

- ``align``
- ``char``
- ``charoff``
- ``span``
- ``valign``
- ``width``

Korona can build <colgroup> tag.

.. code-block:: python

    from korona.html.construct import ColGroup

    attributes = {'align': 'char', 'char': '.', 'charoff': '2'}

    # You can pass in the attributes in the form of a dictionary.
    colgroup1 = ColGroup(**attributes)
    # You can also pass in the attributes as args.
    colgroup2 = ColGroup(align='char', char='.', charoff='2')

    colgroup_tag1 = colgroup1.construct()
    colgroup_tag2 = colgroup2.construct()

    assert colgroup_tag1 == '<colgroup align="char" char="." charoff="2" ></colgroup>'
    assert colgroup_tag1 == colgroup_tag2

<dd>
----

Korona can build <dd> tag.

.. code-block:: python

    from korona.html.construct import DD

    attributes = {'text': 'abc'}

    # You can pass in the attributes in the form of a dictionary.
    dd1 = DD(**attributes)
    # You can also pass in the attributes as args.
    dd2 = DD(text='abc')

    dd_tag1 = dd1.construct()
    dd_tag2 = dd2.construct()

    assert dd_tag1 == '<dd>abc </dd>'
    assert dd_tag1 == dd_tag2

<del>
-----

Korona supports some of the del tag attributes like:

- ``cite``
- ``datetime``

Korona can build <del> tag.

.. code-block:: python

    from korona.html.construct import Del

    attributes = {'cite': 'www.abcd.com', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    del1 = Del(**attributes)
    # You can also pass in the attributes as args.
    del2 = Del(cite='www.abcd.com', text='abcd')

    del_tag1 = del1.construct()
    del_tag2 = del2.construct()

    assert del_tag1 == '<del cite="www.abcd.com" >abcd</del>'
    assert del_tag1 == del_tag2

<details>
---------

Korona supports ``open`` attribute for ``<details>`` tag. Korona can help you build ``<details>`` tag.

.. code-block:: python

    from korona.html.construct import Details

    attributes = {'open': True, 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    details1 = Details(**attributes)
    # You can also pass in the attributes as args.
    details2 = Details(open=True, text='abcd')

    details_tag1 = details1.construct()
    details_tag2 = details2.construct()

    assert details_tag1 == '<details open >abcd</details>
    assert details_tag1 == details_tag2

<dialog>
--------

Korona supports ``open`` attribute for ``<dialog>`` tag. Korona can help you build ``<dialog>`` tag.

.. code-block:: python

    from korona.html.construct import Dialog

    attributes = {'open': True, 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    dialog1 = Dialog(**attributes)
    # You can also pass in the attributes as args.
    dialog2 = Dialog(open=True, text='abcd')

    dialog_tag1 = dialog1.construct()
    dialog_tag2 = dialog2.construct()

    assert dialog_tag1 == '<dialog open >abcd</dialog>
    assert dialog_tag1 == dialog_tag2

<div>
-----

Korona supports ``align`` attribute for ``<div>`` tag. Korona can help you build ``<div>`` tag.

.. code-block:: python

    from korona.html.construct import Div

    attributes = {'align': 'left', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    div1 = Div(**attributes)
    # You can also pass in the attributes as args.
    div2 = Div(align='left', text='abcd')

    div_tag1 = div1.construct()
    div_tag2 = div2.construct()

    assert div_tag1 == '<div align="left" >abcd</div>
    assert div_tag1 == dialog_tag2

<dl>
----

Korona can build <dl> tag.

.. code-block:: python

    from korona.html.construct import DL

    attributes = {'text': 'abc'}

    # You can pass in the attributes in the form of a dictionary.
    dl1 = DL(**attributes)
    # You can also pass in the attributes as args.
    dl2 = DL(text='abc')

    dl_tag1 = dl1.construct()
    dl_tag2 = dl2.construct()

    assert dl_tag1 == '<dl>abc</dl>'
    assert dl_tag1 == dl_tag2

<dt>
----

Korona can build <dt> tag.

.. code-block:: python

    from korona.html.construct import DT

    attributes = {'text': 'abc'}

    # You can pass in the attributes in the form of a dictionary.
    dt1 = DT(**attributes)
    # You can also pass in the attributes as args.
    dt2 = DT(text='abc')

    dt_tag1 = dt1.construct()
    dt_tag2 = dt2.construct()

    assert dt_tag1 == '<dt>abc</dt>'
    assert dt_tag1 == dt_tag2

<embed>
-------

Korona supports some of the embed tag attributes like:

- ``height``
- ``src``
- ``type``
- ``width``

Korona can build <embed> tag.

.. code-block:: python

    from korona.html.construct import Embed

    attributes = {'src': 'helloworld.swf', 'height': '200', 'width': '100'}

    # You can pass in the attributes in the form of a dictionary.
    embed1 = Embed(**attributes)
    # You can also pass in the attributes as args.
    embed2 = Embed(src='helloworld.swf', height='200', width='100')

    embed_tag1 = embed1.construct()
    embed_tag2 = embed2.construct()

    assert embed_tag1 == '<embed src="helloworld.swf" width="100" height="200" >'
    assert embed_tag1 == embed_tag2

<fieldset>
----------

Korona supports some of the fieldset tag attributes like:

- ``disabled``
- ``form``
- ``name``

Korona can build <fieldset> tag.

.. code-block:: python

    from korona.html.construct import FieldSet

    attributes = {'disabled': True, 'form': 'form1', 'name': 'name1'}

    # You can pass in the attributes in the form of a dictionary.
    fieldset1 = FieldSet(**attributes)
    # You can also pass in the attributes as args.
    fieldset2 = FieldSet(disabled=True, form='form1', name='name1')

    fieldset_tag1 = fieldset1.construct()
    fieldset_tag2 = fieldset2.construct()

    assert fieldset_tag1 == '<fieldset form="form1" name="name1" disabled ></fieldset>'
    assert fieldset_tag1 == fieldset_tag2

<figure>
--------

Korona can build <figure> tag.

.. code-block:: python

    from korona.html.construct import Figure

    attributes = {'text': 'abc'}

    # You can pass in the attributes in the form of a dictionary.
    figure1 = Figure(**attributes)
    # You can also pass in the attributes as args.
    figure2 = Figure(text='abc')

    figure_tag1 = figure1.construct()
    figure_tag2 = figure2.construct()

    assert figure_tag1 == '<figure>abc</figure>'
    assert figure_tag1 == figure_tag2

.. note:: Korona for now does not support any inner tags in <figure> tag.

<footer>
--------

Korona can build <footer> tag.

.. code-block:: python

    from korona.html.construct import Footer

    attributes = {'text': 'abc'}

    # You can pass in the attributes in the form of a dictionary.
    footer1 = Footer(**attributes)
    # You can also pass in the attributes as args.
    footer2 = Footer(text='abc')

    footer_tag1 = figure1.construct()
    footer_tag2 = figure2.construct()

    assert footer_tag1 == '<footer>abc</footer>'
    assert footer_tag1 == footer_tag2

.. note:: Korona for now does not support any inner tags in <footer> tag.

<form>
------

Korona supports some of the form tag attributes like:

- ``accept``
- ``action``
- ``autocomplete``
- ``enctype``
- ``method``
- ``name``
- ``novalidate``
- ``target``
- ``text`` (text as in <form>{text}</form>)

Korona can build <form> tag.

.. code-block:: python

    from korona.html.construct import Form

    attributes = {'action': 'demo.asp', 'method': 'get', 'name': 'name1', 'target': '_top'}

    # You can pass in the attributes in the form of a dictionary.
    form1 = Form(**attributes)
    # You can also pass in the attributes as args.
    form2 = Form(action='demo.asp', method='get', name='name1', target='_top')

    form_tag1 = form1.construct()
    form_tag2 = form2.construct()

    assert form_tag1 == '<form action="demo.asp" method="get" name="name1" target="_top" ></form>'
    assert form_tag1 == form_tag2

<frame>
-------

Korona supports some of the frame tag attributes like:

- ``frameborder``
- ``longdesc``
- ``marginheight``
- ``marginwidth``
- ``name``
- ``noresize``
- ``scrolling``
- ``src``

Koron can build <frame> tag.

.. code-block:: python

    from korona.html.construct import Frame

    attributes = {'src': 'frame_a.htm', 'scrolling': 'auto', 'marginheight': '250', 'marginwidth': '100', 'name': 'name1', 'longdesc': 'a.txt'}

    # You can pass in the attributes in the form of a dictionary.
    frame1 = Frame(**attributes)
    # You can also pass in the attributes as args.
    frame2 = Frame(src='frame_a.htm', scrolling='auto', marginheight='250', marginwidth='100', name='name1', longdesc='a.txt')

    frame_tag1 = frame1.construct()
    frame_tag2 = frame2.construct()

    assert frame_tag1 == '<frame src="frame_a.htm" longdesc="a.txt" marginheight="250" marginwidth="100" name="name1" scrolling="auto" >'
    assert frame_tag1 == frame_tag2

<frameset>
----------

Korona supports some of the frameset tag attributes like:

- ``cols``
- ``rows``

Korona can build <frameset> tag.

.. code-block:: python

    from korona.html.construct import FrameSet

    attributes = {'cols': '25%'}

    # You can pass in the attributes in the form of a dictionary.
    frameset1 = FrameSet(**attributes)
    # You can also pass in the attributes as args.
    frameset2 = FrameSet(cols='25%')

    frameset_tag1 = frameset1.construct()
    frameset_tag2 = frameset2.construct()

    assert frameset_tag1 == '<frameset cols="25%" ></frameset>'
    assert frameset_tag1 == frameset2_tag

