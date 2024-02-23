from xml.sax import make_parser, handler

class BuecherHandler(handler.ContentHandler):
    def startElement(self, name, attrs):
        print(name)


parser = make_parser()
b = BuecherHandler()
parser.setContentHandler(b)
parser.parse("buecher.xml")