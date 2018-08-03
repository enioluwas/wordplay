class Utils:
    '''Class providing utility functions for argument validation.'''
    __banned_chars = set()

    @classmethod
    def validate_args(cls, *args):
        '''
        Verifies string, tuple and list args are valid string constructors.

        Args:
            *args (`tuple`): Variadic tuple of arguments to be validated

        Raises:
            `ArgumentError`: if argument is invalid
        '''

        for arg in args:
            if isinstance(arg, str):
                for c in arg:
                    if not cls.is_allowed_char(c):
                        raise ArgumentError(ErrorMessage.INVALID_ARG)
            elif isinstance(arg, list):
                for a in arg:
                    if not cls.is_allowed_char(a):
                        raise ArgumentError(ErrorMessage.INVALID_ARG)
            elif isinstance(arg, tuple):
                for a in arg:
                    if not cls.is_allowed_char(a):
                        raise ArgumentError(ErrorMessage.INVALID_ARG)
            else:
                raise ArgumentError(ErrorMessage.INVALID_ARG)

    @classmethod
    def is_positive_integer(cls, arg):
        '''
        Verifies argument is a valid int constructor.

        Args:
            arg (`int` or `str`): Argument to be validated

        Returns:
            `True` if valid
            `False` if invalid
        '''
        if not (isinstance(arg, int) or isinstance(arg, str)):
            return False

        try:
            val = int(arg)
            if val <= 0:
                return False
            return True
        except ValueError:
            return False

    @classmethod
    def add_disallowed_char(cls, arg):
        '''
        Add character that cannot be used in search.

        Args:
            arg (`str`): character to be added

         Raises:
            `ArgumentError`: if arg is not of type str
        '''
        if not (isinstance(arg, str) and len(arg) == 1):
            raise ArgumentError(ErrorMessage.TYPE_STR)

        cls.__banned_chars.add(arg)

    @classmethod
    def remove_disallowed_char(cls, arg):
        '''
        Make a previously disallowed search character valid.

        Args:
            arg (`str`): character to be removed

         Raises:
            `ArgumentError`: if arg is not of type str
        '''
        if not (isinstance(arg, str) and len(arg) == 1):
            raise ArgumentError(ErrorMessage.TYPE_CHAR)

        try:
            cls.__banned_chars.remove(arg)
        except KeyError:
            raise ArgumentError(ErrorMessage.NONEXST_RMV)

    @classmethod
    def set_disallowed_chars(cls, arg):
        '''
        Override existing set of disallowed search characters.

        Args:
            arg (`set`): set of characters

        Raises:
            `ArgumentError`: if any char in set is empty or len(char) > 1
        '''
        if not isinstance(arg, set):
            raise ArgumentError(ErrorMessage.TYPE_SET)

        elif len(arg) == 0:
            cls.__banned_chars = set()

        else:
            for i in arg:
                if not (isinstance(i, str) and len(i) == 1):
                    raise ArgumentError(ErrorMessage.TYPE_STR)

        cls.__banned_chars = arg

    @classmethod
    def is_allowed_char(cls, arg):
        '''
        Verifies character is an allowed.

        Args:
            arg (`str`): character to be validated

        Returns:
            `True` if valid
            `False` if invalid

        Raises:
            `ArgumentError`: if arg is not of type str
        '''
        if not isinstance(arg, str):
            raise ArgumentError(ErrorMessage.INVALID_ARG)
        if not len(arg) == 1:
            return False
        elif arg in cls.__banned_chars:
            return False

        return True

    @classmethod
    def is_allowed_str(cls, arg):
        '''
        Verifies string is an allowed.

        Args:
            arg (`str`): string to be validated

        Returns:
            `True` if valid
            `False` if invalid
        '''
        if not (isinstance(arg, str) and len(arg) >= 1):
            raise ArgumentError(ErrorMessage.INVALID_STR)
        for c in arg:
            if not cls.is_allowed_char(c):
                return False
            return True


class ArgumentError(AssertionError):
        def __init__(self, *args, **kwargs):
            AssertionError.__init__(self, *args, **kwargs)


class CriteriaError(AssertionError):
    def __init__(self, *args, **kwargs):
            AssertionError.__init__(self, *args, **kwargs)


class ErrorMessage:
    INVALID_ARG = 'Invalid argument passed'
    TYPE_CHAR = 'Argument must be type str and len(char) = 1'
    TYPE_STR = 'Argument must be an str'
    TYPE_SET = 'Argument must be a set'
    INVALID_STR = 'Empty or invalid string passed'
    INVALID_CRTRA = 'Invalid criteria passed'
    NONEXST_RMV = 'Tried to remove nonexistent element'
    LEN_GRTR_WORD = 'Length passed > than length of word'


__all__ = ['Utils', 'ArgumentError', 'CriteriaError', 'ErrorMessage']
