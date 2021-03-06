# coding: utf8
from __future__ import unicode_literals

import pytest


@pytest.mark.xfail
@pytest.mark.models
@pytest.mark.parametrize('text', ["He is the man.", "They are the men."])
def test_issue686(EN, text):
    """Test that pronoun lemmas are assigned correctly."""
    tokens = EN(text)
    assert tokens[0].lemma_ == "-PRON-"
