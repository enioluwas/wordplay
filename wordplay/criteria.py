from .utils import ArgumentError, CriteriaError, ErrorMessage
from .utils import Utils as Ut


class Criteria(object):
    '''Class providing an interface for building search parameters.'''

    def __init__(self, original=None):
        if original is not None:
            if not isinstance(original, Criteria):
                raise ValueError(Criteria)

            self.__begins_with = str(original.get_begins_with())
            self.__ends_with = str(original.get_ends_with())
            self.__contains_at = dict(original.get_contains_at())
            self.__contains = list(original.get_contains())
            self.__word_length = int(original.get_size())

        else:
            self.__begins_with = str()
            self.__ends_with = str()
            self.__contains_at = {}
            self.__contains = []
            self.__word_length = None

    def begins_with(self, arg):
        '''Set letter or alphabetic string the word should begin with.'''

        try:
            Ut.validate_args(arg)
        except ArgumentError:
            raise ArgumentError(ErrorMessage.INVALID_ARG)

        if not isinstance(arg, str):
            arg = ''.join(arg).lower()
        else:
            arg = arg.lower()

        self.__begins_with = arg
        return self

    def get_begins_with(self):
        return self.__begins_with

    def remove_begins_with(self, arg=None):
        '''Remove part or the whole of what the word should begin with.'''

        if arg is None and len(self.__begins_with) > 0:
            self.__begins_with = str()

        else:
            try:
                Ut.validate_args(arg)
            except ArgumentError:
                raise ArgumentError(ErrorMessage.INVALID_ARG)

            if not isinstance(arg, str):
                arg = ''.join(arg).lower()
            else:
                arg = arg.lower()

            if len(arg) > len(self.__begins_with):
                raise CriteriaError(ErrorMessage.NONEXST_RMV)

            else:
                for a in arg:
                    if arg.count(a) > self.__begins_with.count(a):
                        raise CriteriaError(ErrorMessage.NONEXST_RMV)

            self.__begins_with = self.__begins_with.replace(arg, '')

        return self

    def ends_with(self, arg):
        '''Set letter or alphabetic string the word should end with.'''

        try:
            Ut.validate_args(arg)
        except ArgumentError:
            raise ArgumentError(ErrorMessage.INVALID_ARG)

        if not isinstance(arg, str):
            arg = ''.join(arg).lower()
        else:
            arg = arg.lower()

        self.__ends_with = arg
        return self

    def get_ends_with(self):
        return self.__ends_with

    def remove_ends_with(self, arg=None):
        '''Remove part or the whole of what the word should end with.'''
        if arg is None and len(self.__ends_with) > 0:
            self.__ends_with = str()

        else:
            try:
                Ut.validate_args(arg)
            except ArgumentError:
                raise ArgumentError(ErrorMessage.INVALID_ARG)

            if not isinstance(arg, str):
                arg = ''.join(arg).lower()
            else:
                arg = arg.lower()

            if len(arg) > len(self.__ends_with):
                raise CriteriaError(ErrorMessage.NONEXST_RMV)

            else:
                for a in arg:
                    if arg.count(a) > self.__ends_with.count(a):
                        raise CriteriaError(ErrorMessage.NONEXST_RMV)

            self.__ends_with = self.__ends_with.replace(arg, '')

        return self

    def contains(self, *args):
        '''Add letter(s) or alphabetic strings the word should contain.'''
        try:
            for arg in args:
                Ut.validate_args(arg)
        except ArgumentError:
            raise ArgumentError(ErrorMessage.INVALID_ARG)

        self.__contains.extend(args)

        return self

    def contains_at(self, *args):
        '''Add tuple(s) of (str letter, int position_in_word) e.g (a, 1)'''
        for arg in args:
            if not isinstance(arg, tuple):
                raise ArgumentError(ErrorMessage.INVALID_ARG)

            ch = arg[0]
            pos = arg[1]

            if not (Ut.is_allowed_char(ch) and Ut.is_positive_integer(pos)):
                raise ArgumentError(ErrorMessage.INVALID_ARG)

            if not isinstance(pos, int):
                pos = int(pos)

            self.__contains_at[pos] = ch.lower()

        return self

    def get_contains(self):
        return self.__contains

    def get_contains_at(self):
        return self.__contains_at

    def remove_contains(self, *args):
        '''Remove part or the whole of what the word should contain.'''
        if len(args) == 0:
            self.__contains = []

        elif len(args) > len(self.__contains):
            raise CriteriaError(ErrorMessage.INVALID_CRTRA)

        else:
            for arg in args:
                try:
                    Ut.validate_args(arg)
                except ArgumentError:
                    raise ArgumentError(ErrorMessage.INVALID_ARG)

                if not isinstance(arg, str):
                    arg = ''.join(arg).lower()
                else:
                    arg = arg.lower()

                try:
                    self.__contains.remove(arg)
                except ValueError:
                    raise CriteriaError(ErrorMessage.NONEXST_RMV)

        return self

    def remove_contains_at(self, *args):
        '''
        Remove part or the whole positional criteria the word should fulfill.
        '''

        if len(args) == 0:
            self.__contains_at = {}

        elif len(args) > len(self.__contains_at):
            raise ArgumentError(ErrorMessage.INVALID_ARG)

        for arg in args:
            if not isinstance(arg, tuple):
                raise ArgumentError(ErrorMessage.INVALID_ARG)

            ch = arg[0]
            pos = arg[1]

            if not (Ut.is_allowed_char(ch) or Ut.is_positive_integer(pos)):
                raise ArgumentError(ErrorMessage.INVALID_ARG)

            if not isinstance(pos, int):
                pos = int(pos)

            if pos not in self.__contains_at:
                raise CriteriaError(ErrorMessage.NONEXST_RMV)

            del self.__contains_at[pos]

        return self

    def size_is(self, arg):
        '''Set what the int size/length of the word should be.'''

        if not Ut.is_positive_integer(arg):
            raise ArgumentError(ErrorMessage.INVALID_ARG)

        self.__word_length = int(arg)

        return self

    def get_size(self):
        return self.__word_length

    def remove_size(self):
        '''Remove the size restriction on the word.'''
        self.__word_length = None


__all__ = ['Criteria']
