from collections import namedtuple

Name = namedtuple('Name',['name', 'meaning'])

def __init():
    if '_names' not in globals():
        from ..constants import BIBLE_NAMES_PATH
        with open(BIBLE_NAMES_PATH) as file:
            global _names
            _names = {columns[0]: columns[1] for columns in (record.strip().split('|') for record in file)}

__init()

def create(value):
    assert value in _names
    return Name(value, _names[value])

def all_data():
    return _names.copy()

