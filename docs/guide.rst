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

Korona can build an ``<anchor>`` tag.

.. code-block:: python

    from korona.html.tags import A

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

Korona can build an ``<abbr>`` tag.

.. code-block:: python

    from korona.html.tags import Abbr

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

Korona can build an ``<acronym>`` tag.

.. code-block:: python

    from korona.html.tags import Acronym

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

Korona can build an ``<address>`` tag.

.. code-block:: python

    from korona.html.tags import Address

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

Korona can build an ``<area>`` tag.

.. code-block:: python

    from korona.html.tags import Area

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

Korona can build an ``<article>`` tag.

.. code-block:: python

    from korona.html.tags import Article

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

Korona can build ``<b>`` tag.

.. code-block:: python

    from korona.html.tags import B

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

Korona can build ``<base>`` tag.

.. code-block:: python

    from korona.html.tags import Base

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

Korona can build ``<button>`` tag.

.. code-block:: python

    from korona.html.tags import Button

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

Korona can build ``<canvas>`` tag.

.. code-block:: python

    from korona.html.tags import Canvas

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

Korona can build ``<caption>`` tag.

.. code-block:: python

    from korona.html.tags import Caption

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

Korona can build ``<cite>`` tag.

.. code-block:: python

    from korona.html.tags import Cite

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

Korona can build ``<col>`` tag.

.. code-block:: python

    from korona.html.tags import Col

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

Korona can build ``<colgroup>`` tag.

.. code-block:: python

    from korona.html.tags import ColGroup

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

Korona can build ``<dd>`` tag.

.. code-block:: python

    from korona.html.tags import DD

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

Korona can build ``<del>`` tag.

.. code-block:: python

    from korona.html.tags import Del

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

    from korona.html.tags import Details

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

    from korona.html.tags import Dialog

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

    from korona.html.tags import Div

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

Korona can build ``<dl>`` tag.

.. code-block:: python

    from korona.html.tags import DL

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

Korona can build ``<dt>`` tag.

.. code-block:: python

    from korona.html.tags import DT

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

Korona can build ``<embed>`` tag.

.. code-block:: python

    from korona.html.tags import Embed

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

Korona can build ``<fieldset>`` tag.

.. code-block:: python

    from korona.html.tags import FieldSet

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

Korona can build ``<figure>`` tag.

.. code-block:: python

    from korona.html.tags import Figure

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

Korona can build ``<footer>`` tag.

.. code-block:: python

    from korona.html.tags import Footer

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

Korona can build ``<form>`` tag.

.. code-block:: python

    from korona.html.tags import Form

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

Koron can build ``<frame>`` tag.

.. code-block:: python

    from korona.html.tags import Frame

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

Korona can build ``<frameset>`` tag.

.. code-block:: python

    from korona.html.tags import FrameSet

    attributes = {'cols': '25%'}

    # You can pass in the attributes in the form of a dictionary.
    frameset1 = FrameSet(**attributes)
    # You can also pass in the attributes as args.
    frameset2 = FrameSet(cols='25%')

    frameset_tag1 = frameset1.construct()
    frameset_tag2 = frameset2.construct()

    assert frameset_tag1 == '<frameset cols="25%" ></frameset>'
    assert frameset_tag1 == frameset2_tag

<h1>
----

Korona supports ``align`` attribute for ``<h1>`` tag. Korona can help you build ``<h1>`` tag.

.. code-block:: python

    from korona.html.tags import H1

    attributes = {'align': 'left', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    h1_one = H1(**attributes)
    # You can also pass in the attributes as args.
    h1_two = H1(align='left', text='abcd')

    h1_tag1 = h1_one.construct()
    h1_tag2 = h1_two.construct()

    assert h1_tag1 == '<h1 align="left" >abcd</h1>
    assert h1_tag1 == h1_tag2

<h2>
----

Korona supports ``align`` attribute for ``<h2>`` tag. Korona can help you build ``<h2>`` tag.

.. code-block:: python

    from korona.html.tags import H2

    attributes = {'align': 'left', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    h2_one = H2(**attributes)
    # You can also pass in the attributes as args.
    h2_two = H2(align='left', text='abcd')

    h2_tag1 = h2_one.construct()
    h2_tag2 = h2_two.construct()

    assert h2_tag1 == '<h2 align="left" >abcd</h2>
    assert h2_tag1 == h2_tag2

<h3>
----

Korona supports ``align`` attribute for ``<h3>`` tag. Korona can help you build ``<h3>`` tag.

.. code-block:: python

    from korona.html.tags import H3

    attributes = {'align': 'left', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    h3_one = H3(**attributes)
    # You can also pass in the attributes as args.
    h3_two = H3(align='left', text='abcd')

    h3_tag1 = h3_one.construct()
    h3_tag2 = h3_two.construct()

    assert h3_tag1 == '<h3 align="left" >abcd</h3>
    assert h3_tag1 == h3_tag2

<h4>
----

Korona supports ``align`` attribute for ``<h4>`` tag. Korona can help you build ``<h4>`` tag.

.. code-block:: python

    from korona.html.tags import H4

    attributes = {'align': 'left', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    h4_one = H4(**attributes)
    # You can also pass in the attributes as args.
    h4_two = H4(align='left', text='abcd')

    h4_tag1 = h4_one.construct()
    h4_tag2 = h4_two.construct()

    assert h4_tag1 == '<h4 align="left" >abcd</h4>
    assert h4_tag1 == h4_tag2

<h5>
----

Korona supports ``align`` attribute for ``<h5>`` tag. Korona can help you build ``<h5>`` tag.

.. code-block:: python

    from korona.html.tags import H5

    attributes = {'align': 'left', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    h5_one = H5(**attributes)
    # You can also pass in the attributes as args.
    h5_two = H5(align='left', text='abcd')

    h5_tag1 = h5_one.construct()
    h5_tag2 = h5_two.construct()

    assert h5_tag1 == '<h5 align="left" >abcd</h5>
    assert h5_tag1 == h5_tag2

<h6>
----

Korona supports ``align`` attribute for ``<h6>`` tag. Korona can help you build ``<h6>`` tag.

.. code-block:: python

    from korona.html.tags import H6

    attributes = {'align': 'left', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    h6_one = H6(**attributes)
    # You can also pass in the attributes as args.
    h6_two = H6(align='left', text='abcd')

    h6_tag1 = h6_one.construct()
    h6_tag2 = h6_two.construct()

    assert h6_tag1 == '<h6 align="left" >abcd</h6>
    assert h6_tag1 == h6_tag2

<head>
------

Korona can help you build ``<head>`` tag.

.. code-block:: python

    from korona.html.tags import Head

    attributes = {'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    head1 = Head(**attributes)
    # You can also pass in the attributes as args.
    head2 = Head(text='abcd')

    head_tag1 = head1.construct()
    head_tag2 = head2.construct()

    assert head_tag1 == '<head>abcd</head>'
    assert head_tag1 == head_tag2

.. note:: <head> tag for now only supports ``text``. It doesn't has the capability for creating inner tags such as ``<title>``, ``<style>``, etc.

<header>
--------

Korona can help you build ``<header>`` tag.

.. code-block:: python

    from korona.html.tags import Header

    attributes = {'text': 'abc'}

    # You can pass in the attributes in the form of a dictionary.
    header1 = Header(**attributes)
    # You can also pass in the attributes as args.
    header2 = Header(text='abc')

    header_tag1 = header1.construct()
    header_tag2 = header2.construct()

    assert header_tag1 == '<header>abc</header>'
    assert header_tag1 == header_tag2

.. note:: Korona for now does not support any inner tags in <header> tag.

<hr>
----

Korona can help you build ``<hr>`` tag.

.. code-block:: python

    from korona.html.tags import HR

    attributes = {'align': 'center', 'size': '100'}

    # You can pass in the attributes in the form of a dictionary.
    hr1 = HR(**attributes)
    # You can also pass in the attributes as args.
    hr2 = HR(align='center', size='100')

    hr_tag1 = hr1.construct()
    hr_tag2 = hr2.construct()

    assert hr_tag1 == '<hr align="center" size="100" >'
    assert hr_tag1 == hr_tag2

<html>
------

Korona supports some of the html tag attributes like:

- ``manifest``
- ``xmlns``

Korona can help you build ``<html>`` tag.

.. code-block:: python

    from korona.html.tags import Html

    attributes = {'manifest': 'demo.appcache', 'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    html1 = Html(**attributes)
    # You can also pass in the attributes as args.
    html2 = Html(manifest='demo.appcache', text='abcd')

    html_tag1 = html1.construct()
    html_tag2 = html2.construct()

    assert html_tag1 == '<html manifest="demo.appcache" >abcd</html>'
    assert html_tag1 == html_tag2

<i>
---

Korona can help you build ``<i>`` tag.

.. code-block:: python

    from korona.html.tags import I

    attributes = {'text': 'abcd'}

    # You can pass in the attributes in the form of a dictionary.
    italics1 = I(**attributes)
    # You can also pass in the attributes as args.
    italics2 = I(text='abcd')

    italics_tag1 = italics1.construct()
    italics_tag2 = italics2.construct()

    assert italics_tag1 == '<i>abcd</i>
    assert italics_tag1 == italics_tag2

<iframe>
--------

Korona supports ``iframe`` tag attributes like:

- ``align``
- ``frameborder``
- ``height``
- ``longdesc``
- ``marginheight``
- ``marginwidth``
- ``name``
- ``sandbox``
- ``scrolling``
- ``src``
- ``srcdoc``
- ``width``

Korona can help you build ``<iframe>`` tag.

.. code-block:: python

    from korona.html.tags import IFrame

    attributes = {'src': '/demo.asp', 'height': '100', 'width': '200'}

    # You can pass in the attributes in the form of a dictionary.
    iframe1 = IFrame(**attributes)
    # You can also pass in the attributes as args.
    iframe2 = IFrame(src='/demo.asp', height='100', width='200')

    iframe_tag1 = iframe1.construct()
    iframe_tag2 = iframe2.construct()

    assert iframe_tag1 == '<iframe src="/demo.asp" width="200" height="100" ></iframe>'
    assert iframe_tag1 == iframe_tag2

<img>
-----

Korona supports ``img`` tag attributes like:

- ``align``
- ``alt``
- ``border``
- ``crossorigin``
- ``height``
- ``hspace``
- ``ismap``
- ``longdesc``
- ``src``
- ``usemap``
- ``vspace``
- ``width``

Korona can help you build ``<img>`` tag.

.. code-block:: python

    from korona.html.tags import Img

    attributes = {'height': '30', 'width': '30', 'hspace': '20', 'vspace': '20'}

    # You can pass in the attributes in the form of a dictionary.
    img1 = Img(**attributes)
    # You can also pass in the attributes as args.
    img2 = Img(height='30', width='30', hspace='20', vspace='20')

    img_tag1 = img1.construct()
    img_tag2 = img2.construct()

    assert img_tag1 == '<img height="30" hspace="20" vspace="20" width="30" >'
    assert img_tag1 == img_tag2

<input>
-------

Korona supports input tag attributes like:

- accept(str): Specifies the types of files that the server accepts. The
    accept attribute can only be used with <input type="file">.

- align (str): Specifies the alignment of an image input. The align attribute
    is only used with <input type="image">.

- alt (str): Specifies an alternate text for images. The alt attribute can only
    be used with <input type="image">.

- autocomplete (str): Specifies whether an <input> element should have
    autocomplete enabled. The autocomplete attribute works with the following
    <input> types: text, search, url, tel, email, password, datepickers, range,
    and color.

- autofocus (bool): Specifies that an <input> element should automatically get
    focus when the page loads.

- checked (bool): Specifies that an <input> element should be pre-selected
    when the page loads. The checked attribute can be used with <input
    type="checkbox"> and <input type="radio">.

- dirname (str): Specifies that the text direction will be submitted. The
    dirname attribute's value is always the name of the input field, followed by
    ".dir".

- disabled (bool): Specifies that an <input> element should be disabled.

- form (str): Specifies one or more forms the <input> element belongs to.

- formaction (str): Specifies the URL of the file that will process the input
    control when the form is submitted. The formaction attribute is used with
    type="submit" and type="image".

- formenctype (str): Specifies how the form-data should be encoded when
    submitting it to the server. The formenctype attribute is used with
    type="submit" and type="image".

- formmethod (str): Defines the HTTP method for sending data to the action URL.
    The formmethod attribute can be used with type="submit" and type="image".

- formnovalidate (bool): Defines that form elements should not be validated
    when submitted. The formnovalidate attribute can be used with type="submit".

- formtarget (str): Specifies where to display the response that is received
    after submitting the form. The formtarget attribute can be used with
    type="submit" and type="image".

- height (int/float): Specifies the height of an <input> element. The height
    attribute is used only with <input type="image">.

- list (str): Refers to a <datalist> element that contains pre-defined options
    for an <input> element.

- max (int/date/time): Specifies the maximum value for an <input> element. The
    max attribute works with the following input types: number, range, date,
    datetime, datetime-local, month, time and week.

- maxlength (int): Specifies the maximum number of characters allowed in an
    <input> element.

- min (int/date/time): Specifies a minimum value for an <input> element. The
    min attribute works with the following input types: number, range, date,
    datetime, datetime-local, month, time and week.

- multiple (bool): Specifies that a user can enter more than one value in an
    <input> element. The multiple attribute works with the following input types:
    email, and file.

- name (str): Specifies the name of an <input> element.

- pattern (str): Specifies a regular expression that an <input> element's
    value is checked against. The pattern attribute works with the following input
    types: text, date, search, url, tel, email, and password.

- placeholder (str): Specifies a short hint that describes the expected value
    of an <input> element. The placeholder attribute works with the following
    input types: text, search, url, tel, email, and password.

- readonly (bool): Specifies that an input field is read-only.

- required (bool): Specifies that an input field must be filled out before
    submitting the form. The required attribute works with the following input
    types: text, search, url, tel, email, password, date pickers, number,
    checkbox, radio, and file.

- size (int): Specifies the width, in characters, of an <input> element. The
    size attribute works with the following input types: text, search, tel, url,
    email, and password.

- src (str): Specifies the URL of the image to use as a submit button. The src
    attribute is required for <input type="image">, and can only be used with
    <input type="image">.

- step (int): Specifies the legal number intervals for an input field. The step
    attribute works with the following input types: number, range, date, datetime,
    datetime-local, month, time and week.

- type (str): Specifies the type <input> element to display.

- value (str): Specifies the value of an <input> element. The value attribute
    cannot be used with <input type="file">.

- width (int/float): Specifies the width of an <input> element. The width
    attribute is used only with <input type="image">.


Korona can help you build ``<input>`` tag.

.. code-block:: python

    from korona.html.tags import Input

    attributes = {'height': '30', 'width': '30', 'type': 'image', 'src': 'img_submit.jpeg'}

    # You can pass in the attributes in the form of a dictionary.
    input1 = Input(**attributes)
    # You can also pass in the attributes as args.
    input2 = Input(height='30', width='30', type='image', src='img_submit.jpeg')

    input_tag1 = input1.construct()
    input_tag2 = input2.construct()

    assert input_tag1 == '<input type="image" src="img_submit.jpeg" width="30" height="30" >'
    assert input_tag1 == input_tag2

