from os import listdir
from os import getcwd
from os.path import join
import json

import Delta
from build_array import build_array
from build_lookup_table import build_lookup_table


# get the document paths
def get_doc_paths():
    files = map(lambda x: join(getcwd(), 'documents/' + x), sorted(listdir(join(getcwd(), 'documents'))))
    return files


# scan over the documents
def scan_documents(files, delta):
    id_counter = 0
    for document in files:
        id_counter += 1
        words = []
        # read the file,
        # extract words,
        # add to the dictionary.
        with open(document, 'r') as f:
            lines = f.readlines()
            for line in lines:
                words.extend(line.split())
        add_to_dictionary(id_counter, words, delta)  # the function adding info to Dictionary and D(w)


# add information to dictionary
def add_to_dictionary(doc_id, words, delta):
    for w in set(words):
        # add new word if w not already in dictionary
        if not delta.has_word(w):
            delta.add_word(w)
        delta.add_document_id(w, doc_id)


# test
if __name__ == '__main__':
    dictionary = Delta.Delta()  # the dictionary holding the set of words and D(w)
    document_paths = get_doc_paths()
    scan_documents(document_paths, dictionary)
    print dictionary
    # build array A and
    A, T = build_array(dictionary)
    with open('A.json', 'w') as outfile:
        json.dump(A, outfile)
    # build the look up table T
    T = build_lookup_table(T, '123456')
    with open('T.json', 'w') as outfile:
        json.dump(T, outfile)
