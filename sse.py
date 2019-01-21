import json
from os import listdir
from os.path import join

from Delta import Delta
from build_array import build_array
from build_lookup_table import build_lookup_table
from hmac import hmac


#   The Searchable Symmetric Encryption Class.
class SSE(object):
    #   Initialize parameters.
    def __init__(self, pi_key, f_key):
        self.delta = Delta()
        self.pi_key = pi_key
        self.f_key = f_key
        self.file_ids = {}
        self.A = None
        self.T = None

    #   Scan all documents in the given path. Build the index array and look up table.
    def load_file(self, path):
        files = [join(path, x) for x in listdir(path)]
        for i, f in enumerate(files):
            self.file_ids[i] = f
            word_set = set([])
            with open(f, 'r') as infile:
                lines = infile.readlines()
                for line in lines:
                    word_set.update(set(line.split()))
            self._update_delta(i, word_set)
        self.A, plain_T = build_array(self.delta)
        self.T = build_lookup_table(plain_T, self.pi_key, self.f_key)

    #   Change the keys used for hmac.
    def change_key(self, pi_key, f_key):
        self.pi_key = pi_key
        self.f_key = f_key

    #   Return the index array serialized in json format.
    def get_index_array(self):
        return json.dumps(self.A)

    #   Return the look up table serialized in json format.
    def get_index_table(self):
        return json.dumps(self.T)

    #   Generate the trapdoor with given hmac keys and the word to be searched.
    @staticmethod
    def trapdoor(pi_key, f_key, word):
        piw = hmac(word, pi_key)
        fw = hmac(word, f_key)
        return piw, fw

    #   Return the generated identifiers for documents.
    def get_file_ids(self):
        return json.dumps(self.file_ids)

    #   Add word and identifiers to the Delta instance.
    def _update_delta(self, doc_id, words):
        for w in words:
            if not self.delta.has_word(w):
                self.delta.add_word(w)
            self.delta.add_document_id(w, doc_id)
