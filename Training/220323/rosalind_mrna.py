import numpy as np

with open('rosalind_mrna.txt','r',encoding='utf-8') as file:
    aa_code = file.read()

aa_list = ['R','H','K','D','E','S','T','N','Q','C','G','P','A','V','I','L','M','F','Y','W']
aa_count = [2,2,2,2,2,6,4,2,2,2,4,4,4,4,3,6,1,2,2,1]