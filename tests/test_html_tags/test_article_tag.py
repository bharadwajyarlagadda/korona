# -*- coding: utf-8 -*-

from ..fixtures import parametrize

from korona.html.tags import Article
from korona.templates.html.tags import article


@parametrize('attributes', [
    ({'text': 'abc'}),
    ({'text': None}),
    ({'text': '<p>Hi there</p>'})
])
def test_construct_article_tag(attributes):
    """Test for validating whether the article tag is constructed correctly or
    not.
    """
    artcle = Article(**attributes)
    assert artcle.construct() == article.render(attributes)
