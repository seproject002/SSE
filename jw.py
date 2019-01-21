import json
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

x = '1'
y = '2'
t = {'a': x, 'b': y, 'c': None}
print t

with open('t.json', 'w') as outfile:
    json.dump(t, outfile)

with open('t.json', 'r') as infile:
    d = json.load(infile)
    print d

#   simply test encode and decode functions
k = get_random_bytes(16)
print type(k)
k = b64encode(k).decode('utf-8')
print k
tmp = b64decode(k)
print tmp
print b64encode(tmp).decode('utf-8')
