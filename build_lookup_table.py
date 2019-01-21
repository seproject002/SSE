import json
from hmac import hmac, sxor


def build_lookup_table(table, pi_key, f_key):
    T = {}
    for w in table:
        data = json.dumps(table[w])
        piw = hmac(w, pi_key)   # pi(w)
        fw = hmac(w, f_key)     # f(w)
        T[piw] = sxor(data, fw)
    return T
