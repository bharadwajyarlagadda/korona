# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Article
from korona.templates.html.tags import article_tag


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None}),
    ({'text': '<p>Hi there</p>'})
])
def test_construct_article_tag(attributes):
    """Test for validating whether the article tag is constructed correctly or
    not.
    """
    article = Article(**attributes)
    assert article.construct() == article_tag.render(attributes)
