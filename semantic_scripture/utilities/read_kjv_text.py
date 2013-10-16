import re

from os import listdir
from os.path import basename, splitext, join, isfile


KJV_TEXT_ROOT = 'data/kjv_text'
CHAPTER_AND_VERSE = '\{[0-9]{1,3}:[0-9]{1,3}\}'

def read_kjv_text():
    kjv_text = dict()
    verse_delimiter = re.compile(CHAPTER_AND_VERSE)
    for file in [_ for _ in listdir(KJV_TEXT_ROOT) if not _.startswith('.')]:
        book_name = splitext(basename(file))[0]
        verses = dict()
        cav = None
        verse_text = list()

        for word in _words_of_file(join(KJV_TEXT_ROOT,file)):
            if verse_delimiter.match(word):
                if cav:
                    verses[cav] = ' '.join(verse_text)
                    verse_text.clear()
                cav = _chapter_and_verse(word)
            else:
                verse_text.append(word)
        verses[cav] = ' '.join(verse_text)
        kjv_text[book_name] = verses

    return kjv_text




def _chapter_and_verse(string):
    tokens = string.strip('{}').split(':')
    return (int(tokens[0]), int(tokens[1]))


def _words_of_file(file):
    with open(file) as f:
        for line in f:
            for word in line.split():
                yield word