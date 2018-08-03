from pkg_resources import resource_filename as rf
from enum import Enum
from .criteria import Criteria
from .utils import Utils, ArgumentError, ErrorMessage


class SortType(Enum):
    '''
    Enum class providing options for sorting.

    Options:

    SIZE - Sort by Size

    ALPHA - Sort in Alphabetical Order
    '''
    SIZE = 1
    ALPHA = 2


class SortOrder(Enum):
    '''
    Enum class providing order options for sorting.

    Options:

    ASCENDING - A-Z, 0-9

    DESCENDING - Z-A, 9-0
    '''
    ASCENDING = 1
    DESCENDING = 2


class Dictionary(object):
    '''Class providing utilities for finding words with criteria.'''

    def __init__(self, word_list=None):
        self.__accepted_chars = set()

        if word_list is None:
            with open(rf('wordplay', 'data/sample_wordlist.dat')) as wordlist:
                self.__word_list = set(wordlist.read().split())
        elif isinstance(word_list, set):
            self.__word_list = word_list
        else:
            raise ArgumentError(ErrorMessage.TYPE_SET)

    def __iter__(self):
        return iter(self.__word_list)

    def set_wordlist(self, word_list):
        if isinstance(word_list, set):
            self.__word_list = word_list
        else:
            raise ArgumentError(ErrorMessage.TYPE_SET)

    def get_wordlist(self):
        return self.__word_list

    def __get_all_substrings(self, word):
        ln = len(word)
        return [word[i: j] for i in range(ln) for j in range(i + 1, ln + 1)]

    def get_words(self, criteria):
        '''
        Gets words from its wordlist given valid search criteria.

        Args:
            criteria (`Criteria`): Object containing search parameters

        Returns:
            A list of words from its wordlist matching the criteria

        Raises:
            `ArgumentError`: If arg is not of type Criteria
        '''

        if not isinstance(criteria, Criteria):
            raise ArgumentError(ErrorMessage.INVALID_ARG)

        begins = criteria.get_begins_with()
        ends = criteria.get_ends_with()
        u_contains = criteria.get_contains()
        o_contains = criteria.get_contains_at()
        size = criteria.get_size()

        has_u_contains = len(u_contains) is not 0
        has_o_contains = len(o_contains) is not 0
        has_begins = len(begins) is not 0
        has_ends = len(ends) is not 0
        has_size = size is not None and size is not 0

        result = []

        for w in self.__word_list:
            if has_size and len(w) != size:
                continue

            if has_begins:
                if len(w) < len(begins):
                    continue
                elif w[:len(begins)] != begins:
                    continue

            if has_ends:
                if len(w) < len(ends):
                    continue
                elif w[-len(ends):] != ends:
                    continue

            if has_u_contains:
                is_match = True
                for c in u_contains:
                    if w.count(c) != u_contains.count(c):
                        is_match = False
                        break

                if not is_match:
                    continue

            if has_o_contains:
                is_match = True
                for k, v in o_contains.items():
                    if k > len(w) - 1:
                        is_match = False
                        break

                    if w[k - 1] != v:
                        is_match = False
                        break

                if not is_match:
                    continue

            result.append(w)

        return result

    # use kwargs for sort stuff
    def get_words_with_any_letters(
            self,
            word,
            length=None,
            sort_order=SortOrder.ASCENDING,
            sort_type=SortType.ALPHA):
        '''
        Gets words from its wordlist that contain any of the letters in word

        Args:
            word (`str`): Letters to pool words from

        Returns:
            A list of words from its wordlist containing any letters in word

        Raises:
            `ArgumentError`
        '''

        try:
            Utils.validate_args(word)
        except ArgumentError as err:
            raise err

        word = str(word)
        result = []
        has_length = False

        if length is not None:
            if not Utils.is_positive_integer(length):
                raise ArgumentError(ErrorMessage.INVALID_ARG)

            length = int(length)
            if length > len(word):
                raise ArgumentError(ErrorMessage.LEN_GRTR_WORD)
            has_length = True

        for w in self.__word_list:
            w = w.lower()

            if has_length and len(w) != length:
                continue
            elif len(w) > len(word):
                continue

            is_match = True
            for c in w:
                if not w.count(c) <= word.count(c):
                    is_match = False
                    break

            if is_match:
                result.append(w)

        if sort_order == SortOrder.ASCENDING:
            result.sort()
        else:
            result.sort(reverse=True)

        if sort_type == SortType.SIZE:
            result.sort(key=len)

        return result

    # use kwargs for sort stuff
    def get_words_within(
            self,
            word,
            length=None,
            sort_order=SortOrder.ASCENDING,
            sort_type=SortType.ALPHA):
        '''
        Gets words from its wordlist that are substrings of word

        Args:
            word (`str`): Letters to pool words from

        Returns:
            A list of words from its wordlist that are substrings of word

        Raises:
            `ArgumentError`
        '''

        try:
            Utils.validate_args(word)
        except ArgumentError as err:
            raise err

        word = str(word)
        result = []
        has_length = False

        if length is not None:
            if not Utils.is_positive_integer(length):
                raise ArgumentError(ErrorMessage.INVALID_ARG)

            length = int(length)
            if length > len(word):
                raise ArgumentError(ErrorMessage.LEN_GRTR_WORD)
            has_length = True

        substrs = self.__get_all_substrings(word)

        for w in substrs:
            if has_length and len(w) != length:
                continue

            if w in self.__word_list and w not in result:
                result.append(w)

        if sort_order == SortOrder.ASCENDING:
            result.sort()
        else:
            result.sort(reverse=True)

        if sort_type == SortType.SIZE:
            result.sort(key=len)

        return result

    # use kwargs for sort stuff
    def get_anagrams(
            self,
            word,
            sort_order=SortOrder.ASCENDING,
            sort_type=SortType.ALPHA):
        '''
        Gets all anagrams of a word from the wordlist

        Args:
            word (`str`): Letters to pool words from

        Returns:
            A list of words from its wordlist that are anagrams of word

        Raises:
            `ArgumentError`
        '''

        result = self.get_words_with_any_letters(
            word,
            len(word),
            sort_order,
            sort_type)

        if word in result:
            result.remove(word)

        return result


__all__ = ['Dictionary', 'SortType', 'SortOrder']
