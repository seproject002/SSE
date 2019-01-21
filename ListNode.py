import json


class ListNode(object):
    def __init__(self, doc_id=None, kfn=None, ni=None):
        self.doc_id = doc_id
        self.key_for_next = kfn
        self.next_index = ni

    def __str__(self):
        # print self.doc_id
        return json.dumps({'doc_id': self.doc_id,
                           'key_for_next': self.key_for_next,
                           'next_index': self.next_index})

