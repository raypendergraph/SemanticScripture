import traceback

from sys import stdout
from os.path import expanduser, join
from django.core.management.base import BaseCommand
from py2neo import rel
from py2neo.neo4j import Node, GraphDatabaseService, ReadBatch, WriteBatch, Relationship
from semantic_scripture.models import Verse, Name

from semantic_scripture.utilities import read_kjv_text
from semantic_scripture.domain import name


def collate_verses_by_unique():
    verses_by_unique = dict()
    kjv_text = read_kjv_text()
    for book_name, content in kjv_text.items():
        for chapter_verse, verse_text in content.items():
            if not chapter_verse: continue
            verse = Verse(book_name, chapter_verse[0], chapter_verse[1], verse_text)
            verses_by_unique[verse.unique] = verse
    return verses_by_unique


def collate_names_by_unique():
    return {name.unique: name for name in [Name(*entry) for entry in name.all_data().items()]}


def collapse_verses(books):
    for book_name, chapter in books.items():
        for chapter, verses in chapter.items():
            for verse, text in enumerate(verses):
                yield Verse(book_name, chapter, verse, text)


def collate_verse_uniques_by_name_unique(names_by_unique, verses_by_unique):
    excludes = ['So', 'so', 'On', 'on', 'No', 'no']
    verse_uniques_by_name_unique = dict()
    for verse_unique, verse in verses_by_unique.items():
        for word in verse.text.split():
            sanitized_word = word.strip('.,;:" ')
            if sanitized_word in excludes:
                continue
            name = names_by_unique.get(sanitized_word)
            if name:
                map_name(verse_uniques_by_name_unique, verse.unique, name.unique)

    return verse_uniques_by_name_unique


def map_name(verse_uniques_by_name_unique, verse_unique, name_unique):
    verse_uniques_for_name_unique = verse_uniques_by_name_unique.get(name_unique, None)
    if not verse_uniques_for_name_unique:
        verse_uniques_for_name_unique = set()
        verse_uniques_by_name_unique[name_unique] = verse_uniques_for_name_unique

    verse_uniques_for_name_unique.add(verse_unique)

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            verses_by_unique = collate_verses_by_unique()
            names_by_unique = collate_names_by_unique()
            verse_uniques_by_name_unique = collate_verse_uniques_by_name_unique(names_by_unique, verses_by_unique)
            graph_db = GraphDatabaseService("http://localhost:7474/db/data/")

            self.stdout.write("Clearing the old graph...")
            #graph_db.clear()

            self.stdout.write("Writing name nodes...")

            names = graph_db.get_or_create_index(Node, 'names')
            print("Created index ",names)
            batch = WriteBatch(graph_db)
            name_nodes = list()
            for count, name in enumerate(names_by_unique.values()):
                abstract = Node.abstract(**name.to_dict())
                batch.create_in_index_or_fail(Node,names,'by_unique',name.unique,abstract)
                if count % 500 is 0:
                    name_nodes.extend(batch.submit())
                    batch = WriteBatch(graph_db)
            name_nodes.extend(batch.submit())

            verses = graph_db.get_or_create_index(Node,'verses')
            batch = WriteBatch(graph_db)
            self.stdout.write("Writing verse nodes...")
            for count, verse in enumerate(verses_by_unique.values()):
                abstract = Node.abstract(**verse.to_dict())
                #batch.add_labels(abstract, 'Test')
                batch.create_in_index_or_fail(Node,verses,'by_unique',verse.unique, abstract)
                if count % 250 is 0:
                    batch.submit()
                    batch = WriteBatch(graph_db)
            batch.submit()

            self.stdout.write("Relating nodes...")

            for name_node in name_nodes:
                name = name_node['name'].lower()
                verse_uniques = verse_uniques_by_name_unique.get(name)
                if not verse_uniques:
                    continue
                read_batch = ReadBatch(graph_db)
                for unique in verse_uniques:
                    read_batch.get_indexed_nodes(verses,'by_unique',unique)
                verse_nodes = read_batch.submit()
                batch = WriteBatch(graph_db)
                for verse_node in verse_nodes:
                    abstract = Relationship.abstract(verse_node[0],'REFERENCES_NAME', name_node)
                    batch.add_indexed_relationship(abstract)
                batch.submit()






        except:
            traceback.print_exc()
