import pandas as pd

with open('rosalind_grph.txt','r',encoding='utf-8') as chunk_ori:
    chunk = chunk_ori.read()
    chunk = chunk.split('>')

chunk = chunk[1:]
codes= []
for items in chunk:
    key, code_1, code_2, trash = items.split('\n')
    code = code_1+code_2
    head = code[:3]
    tail = code[-3:]
    print(head, tail)
    k_set = [key, head, tail]
    codes.append(k_set)

print(codes)
codes_table = pd.DataFrame(codes, columns=['key','head','tail'])
codes_table