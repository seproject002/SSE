#   Dw is the set consisting of the identifiers of all documents that contain the word w.
class Dw(object):
    def __init__(self, word):
        self.word = word
        self.identifiers = set([])  # holds the set of identifiers of documents which have the word

    def add_doc_id(self, identifier):
        self.identifiers.add(identifier)

    def remove_doc_id(self, identifier):
        self.identifiers.remove(identifier)

    def size_of_id_set(self):
        return len(self.identifiers)

    def __str__(self):
        # print self.word + ': ' + str(self.identifiers)
        return 'Dw word= ' + self.word + '\n'
