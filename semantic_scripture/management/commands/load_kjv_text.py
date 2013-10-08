from django.core.management.base import BaseCommand
from semantic_scripture.utilities import read_kjv_text

import traceback

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            kjv_text  = read_kjv_text()
        except:
            traceback.print_exc()