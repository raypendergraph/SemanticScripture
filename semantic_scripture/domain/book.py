import re
from os.path import join
from semantic_scripture._constants import BOOKS
from .._constants import CHAPTER_AND_VERSE_REGEX, KJV_TEXT_PATH

_books = dict()

def _chapter_and_verse(string):
    tokens = string.strip('{}').split(':')
    return int(tokens[0]), int(tokens[1])

def read_book_data(book_name):
    assert book_name and book_name in BOOKS, "{0} is not a valid book name.".format(book_name)
    chapters = _books.get(book_name, None) or dict()

    if chapters:
        return chapters

    verse_delimiter = re.compile(CHAPTER_AND_VERSE_REGEX)
    with open(join(KJV_TEXT_PATH,'{0}.txt'.format(book_name))) as file:
        words =  [word for word in file.read().split()]
        beginning_index = next((i for i, word in enumerate(words) if verse_delimiter.match(word)), -1)
        chapter_verse = _chapter_and_verse(words[beginning_index])
        last_index = 0
        words = words[beginning_index+1:]
        for index, word in enumerate(words):
            if verse_delimiter.match(word):
                chapter = chapters.get(chapter_verse[0], None)
                if chapter is None:
                    chapter = list()
                    chapters[chapter_verse[0]] = chapter
                chapter.append(' '.join(words[last_index: index]))
                chapter_verse = _chapter_and_verse(word)
                last_index = index+1

    _books[book_name] = chapters
    return chapters

def instance(book_name):
    return {book_name:read_book_data(book_name)}

def all_data():
    return {book:read_book_data(book) for book in BOOKS}





