from django.core.management.base import BaseCommand
from semantic_scripture.domain import name, book

import traceback

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        names_by_verse_key = dict()
        excludes= ['So', 'On', 'No']
        try:
            names = {name.lower(): meaning for (name, meaning) in name.all_data().items()}
            books = book.all_data()
            collapsed = self.collapse_verses(books)
            for verse_key, text in collapsed:
                for word in text.split():
                    sanitized_word = word.strip('.,;:" ')

                    if sanitized_word in excludes:
                        continue

                    if sanitized_word.lower() in names:
                        self.map_name(names_by_verse_key, verse_key, sanitized_word)


        except:
            traceback.print_exc()


    def map_name(self, names_by_verse_key, verse_key, name):

        names_in_verse = names_by_verse_key.get(verse_key, None)
        if not names_in_verse:
            names_in_verse = set()
            names_by_verse_key[verse_key] = names_in_verse

        names_in_verse.add(name)


    def collapse_verses(self, books):
        for book, chapter in books.items():
            for chapter, verses in chapter.items():
                for verse, text in enumerate(verses):
                    yield (book, chapter, verse), text
