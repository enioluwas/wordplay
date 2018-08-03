# Wordplay

[![Build Status](https://travis-ci.org/enioluwa23/wordplay.svg?branch=master)](https://travis-ci.com/enioluwa23/wordplay) [![PyPI version](https://img.shields.io/pypi/v/wordplay.svg)](https://pypi.org/project/wordplay/) [![Supported versions](https://img.shields.io/pypi/wheel/wordplay.svg)](https://pypi.org/project/wordplay/) [![PyPI version](https://img.shields.io/pypi/pyversions/wordplay.svg)](https://pypi.org/project/wordplay/)

Python package for word searching utilities.

Using a convenient API, you can filter a set of strings with detailed criteria. There are also more scrabble-like features such as getting all anagrams of a word.

## Install

```bash
pip install wordplay
```

## Background

I initially built this as an algorithm solely to help my endeavors in word games such as Scrabble. It was useful for finding word combinations in every type of situation. However, I realized it could be used for many other purposes, such as filtering email addresses, phone numbers and any set of data really. So I decided to decouple the API from my personal use.

## Usage

Words are stored in a `Dictionary` object. Initialize the dictionary with a [`set`](https://docs.python.org/2/library/stdtypes.html#set) of strings (there are no restrictions on what the string can contain) or `Dictionary()` with no arguments to use the word set sourced from [here](https://github.com/dwyl/english-words). In the future, I will amass a couple of word lists and make them options for initializing the dictionary.

If you do want restrictions on the string, see the documentation for the [`Utils`](https://enioluwa23.github.io/wordplay/api/utils/) module. For complex query parameters, you can use a `Criteria` object. The class uses the builder pattern, making it easy to construct search parameters.

Here is a an example file:

```python
from __future__ import print_function
from wordplay.dictionary import Dictionary
from wordplay.criteria import Criteria


def main():
    dictionary = Dictionary()

    result = dictionary.get_words_with_any_letters('diction', 6)
    print(result)
    # ['diotic', 'dition', 'indico', 'indict', 'nidiot', 'odinic']

    result = dictionary.get_words_with_any_letters('pox')
    print(result)
    # ['o', 'op', 'ox', 'p', 'po', 'pox', 'x']

    result = dictionary.get_anagrams('aekst')
    print(result)
    # ['keats', 'skate', 'skeat', 'stake', 'steak', 'takes', 'teaks']

    print('car' in dictionary)  # Dictionary is directly iterable
    # True

    criteria = Criteria()
    criteria.begins_with('c').ends_with('s').contains('or')
    criteria.contains_at(('o', 2), ('r', 4)).size_is(10)
    result = dictionary.get_words(criteria)
    print(result)
    # ['corrosives', 'correlates', 'corrugates']


if __name__ == '__main__':
    main()
```

For further example usage see the [Documentation](https://enioluwa23.github.io/wordplay/).

To run tests, use `pytest`.

## Documentation

[API Reference](https://enioluwa23.github.io/wordplay/)

## License

[Apache Software License](https://github.com/enioluwa23/wordplay/blob/master/LICENSE)
