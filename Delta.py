from Dw import Dw


#   Delta = {w1, w2, ..., wd} is a dictionary of d words.
class Delta(object):
    def __init__(self):
        self.dic = {}  # key is string "word"; value is Dw objects

    def has_word(self, word):
        if word in self.dic:
            return True
        else:
            return False

    def add_word(self, word):
        self.dic[word] = Dw(word)

    def remove_word(self, word):
        del self.dic[word]

    def add_document_id(self, word, doc_id):
        self.dic[word].add_doc_id(doc_id)

    def __str__(self):
        d = ''
        for w in self.dic:
            d += str(self.dic[w])
        return d
