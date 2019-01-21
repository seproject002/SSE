from Crypto.Hash import HMAC, SHA256
from Crypto.Util.Padding import pad, unpad


#   Bitwise xor operation on two strings.
def sxor(s1, s2):
    if len(s1) > len(s2):
        pad(s2, len(s1))
    elif len(s1) < len(s2):
        pad(s1, len(s2))
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


#   Compute hmac of given message string with given secret key.
def hmac(msg, secret_key):
    h = HMAC.new(secret_key, digestmod=SHA256)
    h.update(msg)
    return h.hexdigest()


#   test pad and unpad.
if __name__ == '__main__':
    word = 'apple'
    key = '123456'
    fw = hmac(word, key)
    print fw
    tmp = pad('[3, "XNqaThWyQsmKOjJVia6znQ=="]', 64)
    print tmp
    print unpad(tmp, 64)

