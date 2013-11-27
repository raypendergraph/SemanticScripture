from collections import namedtuple


Origin = namedtuple('Origin',['ordinal','designator', 'pretty'])
class OriginType(object):
    Greek = Origin(1, 'G', 'Greek')
    Hebrew = Origin(0, 'H','Hebrew')

    @classmethod
    def from_ordinal(cls, ordinal):
        assert ordinal == 0 or ordinal == 1
        return cls.Hebrew if ordinal == 0 else cls.Greek

    @classmethod
    def from_designator(cls, designator):
        assert designator == 'G' or designator == 'H'
        return cls.Hebrew if designator == 'H' else cls.Greek


def _load_strongs_definitions():
    from ..constants import STRONGS_MAIN
    global _strongs_definitions

    _strongs_definitions = dict()
    with open(STRONGS_MAIN) as file:
        for col in [line.split('|') for line in file]:
            key = col[1], col[0]
            assert col[1] == '0' or col[1] == '1'
            value = {'number': col[0],
                     'origin': 'H' if col[1] == '0' else 'G',
                     'word': col[2],
                     'pronunciation': col[3],
                     'meaning': col[4].strip()}
            _strongs_definitions[key] = value


def _load_cross_references():
    from ..constants import STRONGS_MAIN, STRONGS_CROSS_REFERENCES, STRONGS_ROOTS

    global _strongs_by_book_chapter_verse
    global _book_chapter_verse_by_strongs
    _strongs_by_book_chapter_verse = dict()
    _book_chapter_verse_by_strongs = dict()

    with open(STRONGS_CROSS_REFERENCES) as file:
        for col in [line.split() for line in file]:
            _strongs = col[1], col[0]
            bcv = col[2], col[3], col[4]

            strongs_list = _strongs_by_book_chapter_verse.get(bcv, None)
            if not strongs_list:
                strongs_list = list()
                _strongs_by_book_chapter_verse[bcv] = strongs_list
            strongs_list.append(_strongs)

            bcv_list = _book_chapter_verse_by_strongs.get(_strongs, None)
            if not bcv_list:
                bcv_list = list()
                _book_chapter_verse_by_strongs[_strongs] = bcv_list
            bcv_list.append(bcv)



_load_strongs_definitions()
_load_cross_references()

def lookup_definition(origin, number):
    assert origin == 'H' or origin == 'G', "Origin has to be 'H'-Hebrew or 'G'-Greek."
    return _strongs_definitions[origin,number]

def get_definiton_data():
    return _strongs_definitions.copy()

def get_strongs_by_verse():
    return _strongs_by_book_chapter_verse.copy()

def get_verses_by_strongs():
    return _book_chapter_verse_by_strongs.copy()
