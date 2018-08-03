from collections import Counter as Ct
from wordplay.criteria import Criteria
from wordplay.utils import ArgumentError, CriteriaError, Utils


def setup_function(function):
    Utils.set_disallowed_chars(set())


def test_copy_constructor():
    orig_words = Criteria()
    orig_words.begins_with('d').ends_with('n').contains('mna', 'tion')
    orig_words.contains_at(('t', 6), ('o', 8)).size_is(9)

    new_words = Criteria(orig_words)

    if orig_words.get_begins_with() != new_words.get_begins_with():
        assert False
    if orig_words.get_ends_with() != new_words.get_ends_with():
        assert False
    if Ct(orig_words.get_contains()) != Ct(new_words.get_contains()):
        assert False
    if Ct(orig_words.get_contains_at()) != Ct(new_words.get_contains_at()):
        assert False
    if orig_words.get_size() != new_words.get_size():
        assert False


def test_begins_with():
    words1 = Criteria().begins_with('NOIR')
    words2 = Criteria().begins_with(['n', 'o', 'i', 'r'])
    words3 = Criteria().begins_with(('n', 'o', 'i', 'r'))

    assert words1.get_begins_with() == 'noir'
    assert words1.get_begins_with() == words2.get_begins_with()
    assert words2.get_begins_with() == words3.get_begins_with()

    Utils.set_disallowed_chars({'1', '2', '3'})
    try:
        Criteria().begins_with('123')
        assert False
    except ArgumentError:
        assert True


def test_remove_begins_with():
    words1 = Criteria().begins_with('noir')
    words1.remove_begins_with('oi')
    assert words1.get_begins_with() == 'nr'

    words1.remove_begins_with()
    assert len(words1.get_begins_with()) == 0

    Utils.set_disallowed_chars({'1', '2', '3'})
    try:
        words1.remove_begins_with('123')
        assert False
    except ArgumentError:
        assert True


def test_ends_with():
    words1 = Criteria().ends_with('NOIR')
    words2 = Criteria().ends_with(['n', 'o', 'i', 'r'])
    words3 = Criteria().ends_with(('n', 'o', 'i', 'r'))

    assert words1.get_ends_with() == 'noir'
    assert words1.get_ends_with() == words2.get_ends_with()
    assert words2.get_ends_with() == words3.get_ends_with()

    Utils.set_disallowed_chars({'1', '2', '3'})
    try:
        Criteria().ends_with('123')
        assert False
    except ArgumentError:
        assert True


def test_remove_ends_with():
    words1 = Criteria().ends_with('noir')
    words1.remove_ends_with('oi')
    assert words1.get_ends_with() == 'nr'

    words1.remove_ends_with()
    assert len(words1.get_ends_with()) == 0

    Utils.set_disallowed_chars({'1', '2', '3'})
    try:
        words1.remove_ends_with('123')
        assert False
    except ArgumentError:
        assert True


def test_contains():
    exp_list = ['or', 'we', 'a', 'moo']
    words1 = Criteria().contains('or', 'a', 'we')
    words1.contains('moo')
    assert Ct(words1.get_contains()) == Ct(exp_list)

    # add more failing cases
    Utils.set_disallowed_chars({'1', '2', '3'})
    try:
        Criteria().contains('a', 'B', '123')
        assert False
    except ArgumentError:
        assert True


def test_remove_contains():
    words1 = Criteria().contains('or', 'a', 'we', 'moo')
    exp_list = ['or']
    words1.remove_contains('we', 'a', 'moo')
    assert Ct(words1.get_contains()) == Ct(exp_list)
    words1.remove_contains('or')

    try:
        words1.remove_contains('nonexistent')
        assert False
    except CriteriaError:
        assert True


def test_contains_at():
    exp_dict = {2: 'b', 1: 'a', 3: 'c'}
    words1 = Criteria().contains_at(('a', 1), ('b', 2), ('c', 3))
    assert exp_dict == words1.get_contains_at()

    # add more failing cases
    try:
        Criteria().contains_at((1, 'a'), ('b', 2), ('c', 3))
        assert False
    except ArgumentError:
        assert True


def test_remove_contains_at():
    words1 = Criteria().contains_at(('a', 1), ('b', 2), ('c', 3))
    exp_dict = {2: 'b'}
    words1.remove_contains_at(('c', 3), ('a', 1))
    assert exp_dict == words1.get_contains_at()

    try:
        words1.remove_contains_at(('a', 1))
        assert False
    except CriteriaError:
        assert True


def test_size_is():
    words1 = Criteria().size_is(8)
    assert words1.get_size() == 8

    # add more failing cases
    try:
        words1.size_is('a')
        assert False
    except ArgumentError:
        assert True


def test_remove_size():
    words1 = Criteria().size_is(8)
    words1.remove_size()
    assert words1.get_size() is None
