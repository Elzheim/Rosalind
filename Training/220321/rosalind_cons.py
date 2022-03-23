import numpy as np
import pandas as pd
with open('rosalind_cons.txt','r',encoding='utf-8') as chunk_ori:
    chunk = chunk_ori.read()
    chunk = chunk.split('>')

chunk = chunk[1:]
codes= []
for items in chunk:
    code= items.split('\n')
    code = list(code)
    code = code[1:(len(code)-2)]
    coding=''
    for i in range(len(code)):
        coding += code[i]
    code_len = len(coding)
    coding = list(coding)
    codes.append(coding)


data_np = np.array(codes)
print(np.shape(data_np))

data_np = np.reshape(data_np,newshape=(len(data_np),code_len,1))
conv = {'A':[1,0,0,0],'C':[0,1,0,0],'G':[0,0,1,0],'T':[0,0,0,1]}
data_np = np.where(data_np=='A',[1,0,0,0],data_np)
data_np = np.where(data_np=='C',[0,1,0,0],data_np)
data_np = np.where(data_np=='G',[0,0,1,0],data_np)
data_np = np.where(data_np=='T',[0,0,0,1],data_np)
data_np = np.asarray(data_np,int)
data_np

data_sum = np.sum(data_np,axis=0)
data_sum

code_table = []

code_list = ['A','C','G','T']
for i in range(len(data_sum)):
    for j in range(len(data_sum[i])):
        if max(data_sum[i])==data_sum[i][j] :
            code_table.append(code_list[j])

for x in code_table:
    print(x, end=' ')

print('\n')
code_sheet = pd.DataFrame(data_sum, columns=['A','C','G','T'])
code_sheet = code_sheet.transpose()

code_sheet.to_csv('rosalind_cons_ans.txt')

f= open('rosalind_cons_ans.txt','a',encoding='utf-8') 
for x in code_table:
    f.write(x)
f.close()