from xml.sax import make_parser, handler
# https://www.python-kurs.eu/python_XML_SAX.php
class BuecherHandler(handler.ContentHandler):

    def __init__(self):
        self.authors = set()
        self.titles = set()
        self.current_content = ""

    def startElement(self, name, attrs):
        self.current_content = ""

    def characters(self, content):
        self.current_content += content.strip()

    def endElement(self, name):
        if name == "title":
            self.titles.add(self.current_content)
        elif name == "author":
            self.authors.add(self.current_content)

    def getTitles(self):
        return self.titles

    def getAuthors(self):
        return self.authors


parser = make_parser()
b = BuecherHandler()
parser.setContentHandler(b)
parser.parse("buecher.xml")

print("Authors: ")
print(b.getAuthors())

print("Titles:")
print(b.getTitles())