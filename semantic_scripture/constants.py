#Texts we don't have: Ecclesiaticus
#Texts we have with no references: {'2 Esdras', 'Sirach', 'Azaria', 'Manasses', '1 Esdras', 'Letters of Jeremiah', 'Susanna', 'Bel'}

BIBLE_NAMES_PATH = 'data/bible_names.txt'

KJV_TEXT_PATH = 'data/kjv_text'

STRONGS_MAIN = 'data/strongs/strong.txt'

STRONGS_ROOTS = 'data/strongs/strongroots.txt'

STRONGS_CROSS_REFERENCES = 'data/strongs/strongxrefs.txt'

CHAPTER_AND_VERSE_REGEX = '\{[0-9]{1,3}:[0-9]{1,3}\}'

BOOKS = set(['Preface',
             'Genesis',
             'Exodus',
             'Leviticus',
             'Numbers',
             'Deuteronomy',
             'Joshua',
             'Judges',
             'Ruth',
             '1 Samuel',
             '2 Samuel',
             '1 Kings',
             '2 Kings',
             '1 Chronicles',
             '2 Chronicles',
             'Ezra',
             'Nehemiah',
             'Esther',
             'Job',
             'Psalms',
             'Proverbs',
             'Ecclesiastes',
             'Song of Solomon',
             'Isaiah',
             'Jeremiah',
             'Lamentations',
             'Ezekiel',
             'Daniel',
             'Hosea',
             'Joel',
             'Amos',
             'Obadiah',
             'Jonah',
             'Micah',
             'Nahum',
             'Habakkuk',
             'Zephaniah',
             'Haggai',
             'Zechariah',
             'Malachi',
             'Matthew',
             'Mark',
             'Luke',
             'John',
             'Acts',
             'Romans',
             '1 Corinthians',
             '2 Corinthians',
             'Galatians',
             'Ephesians',
             'Philippians',
             'Colossians',
             '1 Thessalonians',
             '2 Thessalonians',
             '1 Timothy',
             '2 Timothy',
             'Titus',
             'Philemon',
             'Hebrews',
             'James',
             '1 Peter',
             '2 Peter',
             '1 John',
             '2 John',
             '3 John',
             'Jude',
             'Revelation',
             'Tobit', #Deuterocanonical(Roman Catholic canon)
             'Judith', #Deuterocanonical(Roman Catholic canon)
             'Wisdom', #Deuterocanonical(Roman Catholic canon)
             'Ecclesiasticus', #Deuterocanonical(Roman Catholic canon)
             'Baruch', #Deuterocanonical(Roman Catholic canon)
             '1 Maccabees', #Deuterocanonical(Roman Catholic canon)
             '2 Maccabees',#Deuterocanonical(Roman Catholic canon)
             '1 Esdras',
             '2 Esdras',
             'Bel',
             'Manasses',
             'Letters of Jeremiah',
             'Azaria',
             'Sirach',
             'Susanna'])

BOOK_NUMBERS_BY_NAME = {_[1]: _[0] for _ in enumerate(BOOKS)}