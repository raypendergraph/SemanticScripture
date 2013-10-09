The date that this table of contents was created is: 12/01/2008

You have selected to download the material for Strong Numbers

Here is a list of the file(s) found in this .zip file:
                      
1.) strong.txt      - TAB delimited text file.  This file can be used by a developer to load the Strong number information
                      into a database of his/her own choosing.  Each line represents a Strong number information and is 
                      terminated by a carriage return. This file is geared to computer application developers who want 
                      to leverage this data into an application they support or wish to build.  The structure of the 
                      file is provided below.

2.) strongroots.txt - TAB delimited text file.  This file can be used by a developer to load the Strong roots information
                      into a database of his/her own choosing.  Each line represents a Strong root information and is
                      terminated by a carraige return.  This file is geared to computer application developers who want 
                      to leverage this data into an application they support or wish to build.  The structure of the 
                      file is provided below.

3.) strongxref.txt  - TAB delimited text file.  This file can be used by a developer to load into a database of his/her
                      own choosing.  Each line represents a verse where the Strong number can be found and is 
                      terminated by a carriage return.  This file is geared to computer application developers who want 
                      to leverage this data into an application they support or wish to build.  The structure of the 
                      file is provided below. 

Here is the structure to use for strong.txt

+---------------+-------------+
| Field         | Type        |
+---------------+-------------+
| strong_nbr    | integer     | -> represents the Strong number
| origin        | integer     | -> 0 is assigned for Hebrew Strong Numbers, 1 is for Greek Strong numbers.  The combination of strong_nbr and origin is unique.
| word          | varchar(64) | -> the phonetic spelling of the Hebrew or Greek word
| pronunciation | varchar(64) | -> how the the Hebrew or Greek word should be pronounced
| definition    | text        | -> the definition of the Hebrew or Greek word 
+---------------+-------------+

Here is the structure to use for strongroots.txt

+-------------+---------+
| Field       | Type    |
+-------------+---------+
| strong_nbr  | integer | -> represents the Strong number
| origin      | integer | -> 0 is assigned for Hebrew Strong numbers, 1 is for Greek Strong numbers.  The combination of strong_nbr and origin is unique.
| root_nbr    | integer | -> the Strong number of one of the root words (there can be many)
| root_origin | integer | -> the origin of the root Strong number (0 is for Hebrew, 1 is for Greek)
+-------------+---------+
 
Here is the structure to use for strongxref.txt

+-------------+---------+
| Field       | Type    |
+-------------+---------+
| strong_nbr  | integer | -> represents the Strong number
| origin      | integer | -> 0 is assigned for Hebrew Strong numbers, 1 is for Greek Strong numbers.  The combination of strong_nbr and origin is unique.
| book_key    | integer | -> the book where the Strong number has been assigned
| chapter_nbr | integer | -> the chapter number, within the book, where the Strong number is found
| verse_nbr   | integer | -> the verse number, within the chapter numbver, where the Strong number is found
+-------------+---------+
      
What follows is a list of the book_key assignments.  All deuterocanonical books numbering begin after Revelation's book 
number assignment.  The deuterocanonical books will only be found in the Douay Rheims and Vulgate (Jerome's) translations.

+----------+-----------------+
| book_key | book name       |
+----------+-----------------+
|        1 | Genesis         |
|        2 | Exodus          |
|        3 | Leviticus       |
|        4 | Numbers         |
|        5 | Deuteronomy     |
|        6 | Joshua          |
|        7 | Judges          |
|        8 | Ruth            |
|        9 | 1 Samuel        |
|       10 | 2 Samuel        |
|       11 | 1 Kings         |
|       12 | 2 Kings         |
|       13 | 1 Chronicles    |
|       14 | 2 Chronicles    |
|       15 | Ezra            |
|       16 | Nehemiah        |
|       17 | Esther          |
|       18 | Job             |
|       19 | Psalms          |
|       20 | Proverbs        |
|       21 | Ecclesiates     |
|       22 | Song of Solomon |
|       23 | Isaiah          |
|       24 | Jeremiah        |
|       25 | Lamentations    |
|       26 | Ezekiel         |
|       27 | Daniel          |
|       28 | Hosea           |
|       29 | Joel            |
|       30 | Amos            |
|       31 | Obadiah         |
|       32 | Jonah           |
|       33 | Micah           |
|       34 | Nahum           |
|       35 | Habakkuk        |
|       36 | Zephaniah       |
|       37 | Haggi           |
|       38 | Zechariah       |
|       39 | Malachi         |
|       40 | Matthew         |
|       41 | Mark            |
|       42 | Luke            |
|       43 | John            |
|       44 | Acts            |
|       45 | Romans          |
|       46 | 1 Corinthians   |
|       47 | 2 Corinthians   |
|       48 | Galatians       |
|       49 | Ephesians       |
|       50 | Philippians     |
|       51 | Colossians      |
|       52 | 1 Thessalonians |
|       53 | 2 Thessalonians |
|       54 | 1 Timothy       |
|       55 | 2 Timothy       |
|       56 | Titus           |
|       57 | Philemon        |
|       58 | Hebrews         |
|       59 | James           |
|       60 | 1 Peter         |
|       61 | 2 Peter         |
|       62 | 1 John          |
|       63 | 2 John          |
|       64 | 3 John          |
|       65 | Jude            |
|       66 | Revelation      |
|       67 | Tobit           | Deuterocanonical (Roman Catholic canon)
|       68 | Judith          | Deuterocanonical (Roman Catholic canon)
|       69 | Wisdom          | Deuterocanonical (Roman Catholic canon)
|       70 | Ecclesiaticus   | Deuterocanonical (Roman Catholic canon)
|       71 | Baruch          | Deuterocanonical (Roman Catholic canon)
|       72 | 1 Maccabees     | Deuterocanonical (Roman Catholic canon)
|       73 | 2 Maccabees     | Deuterocanonical (Roman Catholic canon)
+----------+-----------------+

Best wishes! I hope you find an interesting way to work with this data!



     
      

