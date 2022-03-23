import numpy as np
import math
with open('rosalind_mrna.txt','r',encoding='utf-8') as file:
    aa_code = file.read()

aa_list = ['R','H','K','D','E','S','T','N','Q','C','G','P','A','V','I','L','M','F','Y','W']
aa_count = [6,2,2,2,2,6,4,2,2,2,4,4,4,4,3,6,1,2,2,1]
aa_dict = dict(zip(aa_list,aa_count))
print(aa_dict)
print(type(aa_dict.get('A')))

aa_mod = 3
for aa in aa_code:
    aa_mod = aa_mod*(aa_dict.get(aa))%1000000
print(aa_mod)