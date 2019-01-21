from Crypto.Random.random import shuffle
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

from ListNode import ListNode
from AESCihper import AESCipher


#   Build the index array as in the scheme.
def build_array(delta):
    # create random permutation for index
    size = 0
    for w in delta.dic:
        size += delta.dic[w].size_of_id_set()
    A = [None for _ in xrange(size)]  # initialize A
    head_keys = {}
    permutation = range(size)
    shuffle(permutation)  # the random permutation for storing ListNodes in A ------ Psi

    # main loop
    ctr = 0  # counter for permutation
    for w in delta.dic:
        key_0 = get_random_bytes(16)
        head_keys[w] = (permutation[ctr], b64encode(key_0).decode('utf-8'))
        length = delta.dic[w].size_of_id_set()  # number of documents containing w
        i = 1   # the i-th identifier in Dw
        for identifier in delta.dic[w].identifiers:
            k = get_random_bytes(16)    # key used to encrypt next node
            k64 = b64encode(k).decode('utf-8')
            if i < length:
                node = ListNode(identifier, k64, permutation[ctr+1])
            else:
                node = ListNode(identifier)  # if it was the last document which has w, next = None
            # encrypt the node
            aes_cipher = AESCipher(key_0)
            iv, ct = aes_cipher.encrypt(str(node))  # serialize the node in json format
            # store the encrypted node into A
            A[permutation[ctr]] = (iv, ct)
            # counters + 1
            i += 1
            ctr += 1
            key_0 = k

    return A, head_keys     # A is an array list; head_keys is a python dictionary {w: (first_address_in_A, key)}
