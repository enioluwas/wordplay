from wordplay.utils import Utils, ArgumentError


def setup_function(function):
    Utils.set_disallowed_chars(set())


def test_validate_args():
    disallowed_set = {'1', '2', '-'}
    Utils.set_disallowed_chars(disallowed_set)
    should_pass = ['aAa', ['a', 'b', 'C'], ('a', 'B', 'c')]
    should_throw = ['a12', ['aa', '1', 'c'], ('a', '-2', 'cc')]
    passed = True

    for i in should_pass:
        try:
            Utils.validate_args(i)
            passed = True
        except ArgumentError:
            passed = False
            break

    assert passed

    for i in should_throw:
        try:
            Utils.validate_args(i)
            assert False
        except ArgumentError:
            pass

        assert True


def test_is_positive_integer():
    should_true = [1, '1']
    should_false = [0, '0', '-1', -1, 1.0, '1.0', '-1.0', -1.0]

    for i in should_true:
        assert Utils.is_positive_integer(i)

    for i in should_false:
        assert not Utils.is_positive_integer(i)


def test_is_allowed_char():
    Utils.set_disallowed_chars({'1'})
    should_true = ['a', 'A']
    should_false = ['1', 'a1']

    for i in should_true:
        assert Utils.is_allowed_char(i)

    for i in should_false:
        assert not Utils.is_allowed_char(i)
