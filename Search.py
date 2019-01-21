import json
from base64 import b64decode

from AESCihper import AESCipher
from hmac import hmac, sxor


#   Search over the given index array and look up table with trapdoor.
def search(str_A, str_T, piw, fw):
    A = json.loads(str_A)
    T = json.loads(str_T)
    if piw not in T:
        return []
    result = []

    head_node_str = sxor(T[piw], fw)
    # print head_node_str
    head_node = json.loads(head_node_str)
    addr = head_node[0]
    key = head_node[1]
    while addr is not None:    # fixed a bug here.     cannot use 'while addr'
        iv, ct = A[addr]
        d_cipher = AESCipher(b64decode(key))
        pt = d_cipher.decrypt(iv, ct)
        node = json.loads(pt)       # this is a python dictionary (serialized ListNode)
        doc_id = node['doc_id']
        key = node['key_for_next']
        addr = node['next_index']
        result.append(doc_id)
    return result
