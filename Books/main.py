import xml.etree.ElementTree as ET

def main():
    with open('/Users/rpendergraph/projects/raypendergraph/SemanticScripture/Books/KJV.xml', 'rt') as f:
        content = f.read()
        root = ET.fromstring(content)        
    for book in root.iter('book'):
        title = book.attrib['title'].replace(' ', '_')
        book.set('xmlns', 'http://example.com/SemanticScripture')
        book.set('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        book.set('schemaLocation', 'http://example.com/SemanticScripture SemanticScripture.xsd')
        with open(f'KJV/{title}.xml', "w", encoding="utf-8") as f:
            ET.ElementTree(book).write(f, encoding="unicode", xml_declaration=True)
if __name__ == '__main__':
    main()