from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


#   AES cipher class
class AESCipher(object):
    def __init__(self, key):
        self.key = key      # expecting 16 bytes key

    #   encrypt data
    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    #   decrypt data
    def decrypt(self, iv, ct):
        d_cipher = AES.new(self.key, AES.MODE_CBC, b64decode(iv))
        pt = unpad(d_cipher.decrypt(b64decode(ct)), AES.block_size)
        return pt


#   test the encrypt and decrypt functions
if __name__ == "__main__":
    data = 'secret'
    key = '123456'
    key_bytes = PBKDF2(key, get_random_bytes(8))

    cipher = AES.new(key_bytes, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    print 'ct: ' + ct, 'iv: ' + iv

    iv = b64decode(iv)
    ct = b64decode(ct)
    d_cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    pt = unpad(d_cipher.decrypt(ct), AES.block_size)
    print pt


