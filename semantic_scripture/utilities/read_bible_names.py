
BIBLE_NAMES = 'data/bible_names.txt'

def read_bible_names():
    with open(BIBLE_NAMES) as file:
        return {tuple[0]:tuple[1] for tuple in (line.strip().split('|') for line in file if line)}