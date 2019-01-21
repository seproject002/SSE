from os import getcwd

from sse import SSE
from Search import search


if __name__ == '__main__':
    # testing parameters
    cwd = getcwd()
    path = cwd + '/documents'
    pi_k = '123456'
    f_k = '654321'
    # use sse
    sse = SSE(pi_k, f_k)
    sse.load_file(path)
    A_str = sse.get_index_array()
    table_str = sse.get_index_table()
    print sse.get_file_ids()
    print A_str
    print table_str
    # search with trapdoor
    piw, fw = SSE.trapdoor(pi_k, f_k, 'apple')
    result = search(A_str, table_str, piw, fw)
    print result

