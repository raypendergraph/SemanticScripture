from django.core.management.base import BaseCommand
from py2neo import neo4j
from semantic_scripture import constants
from semantic_scripture.domain import name, book
import traceback


import traceback

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        try:
            names = name.all_data()
            all_books = book.all_data()
            for book_name in constants.BOOKS:
                book_chapters = all_books[book_name]
                for chapter in range(1,len(book_chapters)):
                    for (verse, text) in enumerate(book_chapters[chapter]):
                        found_names = set()
                        for word in text.split():
                            sanitized = word.strip('.,;:-')
                            if sanitized in names and sanitized not in found_names:
                                found_names.add(sanitized)
                                print('|'.join([str(hash((book_name, chapter, verse))),book_name,str(chapter),str(verse),sanitized]))
        except Exception as e:
            traceback.print_exc(file=self.stdout)
