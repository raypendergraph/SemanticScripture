from .constants import BOOKS


class Verse(object):
    def __init__(self, book, chapter, verse, text):
        assert book in BOOKS, "Invalid book name {0}".format(book)
        self._book = book
        self._chapter = chapter
        self._verse = verse
        self._text = text

    @property
    def book(self):
        return self._book

    @property
    def chapter(self):
        return self._chapter

    @property
    def verse(self):
        return self._verse

    @property
    def text(self):
        return self._text

    @property
    def unique(self):
        return '-'.join([self.book.replace(' ','-'),str(self.chapter), str(self.verse)]).lower()


    def __hash__(self):
        return hash((self.book, self.chapter, self.verse))

    def to_dict(self):
        return {
            'hash': hash(self),
            'book': self.book,
            'chapter': self.chapter,
            'verse': self.verse,
            'text': self.text
        }


class Name(object):
    def __init__(self, name, meaning):
        self._name = name
        self._meaning = meaning

    @property
    def name(self):
        return self._name

    @property
    def unique(self):
        return self.name.lower()

    @property
    def meaning(self):
        return self._meaning

    def __hash__(self):
        return hash(self.name)


    def to_dict(self):
        return {
            'name': self.name,
            'meaning': self.meaning
        }


class Strongs(object):
    def __init__(self, designator, number, pronunciation, definition):
        assert designator in ['H', 'h', 'G', 'g'], "Designator must be H or G."
        self._designator = designator
        self._number = number
        self._pronunciation = pronunciation
        self._definition = definition

    @property
    def designator(self):
        return self._designator

    @property
    def number(self):
        return self._number

    @property
    def pronunciation(self):
        return self._pronunciation

    @property
    def definition(self):
        return self._definition

    def __hash__(self):
        return hash((self.designator, self.number))

    def to_dict(self):
        return {

        }


