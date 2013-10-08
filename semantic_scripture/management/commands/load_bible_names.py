from django.core.management.base import BaseCommand
from semantic_scripture.utilities import read_bible_names

import traceback

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            bible_names = read_bible_names()
            print(bible_names)
        except:
            traceback.print_exc()