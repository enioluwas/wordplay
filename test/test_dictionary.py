from collections import Counter as Ct
from wordplay.criteria import Criteria
from wordplay.dictionary import Dictionary
from wordplay.utils import Utils

global_dict = Dictionary()


def setup_function(function):
    Utils.set_disallowed_chars(set())


def test_get_words():
    exp_result = ['correlates', 'corrosives', 'corrugates']
    words = Criteria()
    words.begins_with('c').ends_with('s').contains('or')
    words.contains_at(('o', 2), ('r', 4)).size_is(10)
    test_result = global_dict.get_words(words)

    assert Ct(test_result) == Ct(exp_result)


def test_get_words_with_any_letters():
    exp_result = ['diotic', 'dition', 'indico', 'indict', 'nidiot', 'odinic']
    test_result = global_dict.get_words_with_any_letters('diction', 6)

    assert Ct(test_result) == Ct(exp_result)

    exp_result = ['o', 'op', 'ox', 'p', 'po', 'pox', 'x']
    test_result = global_dict.get_words_with_any_letters('pox')

    assert Ct(test_result) == Ct(exp_result)


def test_get_words_within():
    exp_result = ['e', 'h', 'ho', 'hol', 'hole', 'l', 'le', 'o', 'ol', 'ole']
    test_result = global_dict.get_words_within('hole')

    assert Ct(test_result) == Ct(exp_result)

    exp_result = ['hol', 'ole']
    test_result = global_dict.get_words_within('hole', 3)

    assert Ct(test_result) == Ct(exp_result)


def test_get_anagrams():
    exp_result = ['post', 'pots', 'spot', 'stop', 'tops']
    test_result = global_dict.get_anagrams('opts')

    assert Ct(test_result) == Ct(exp_result)

    exp_result = ['keats', 'skate', 'skeat', 'stake', 'steak', 'takes', 'teaks']
    test_result = global_dict.get_anagrams('aekst')

    assert Ct(test_result) == Ct(exp_result)
