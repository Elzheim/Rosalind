def pmutation(data):
    seqs = data.split()
    tup_seq  = zip(seqs[0],seqs[1])
    hamming_d=0
    for nt in tup_seq:
        if nt[0] != nt[1]: hamming_d +=1
    print(hamming_d)
    return hamming_d

fasta = '''GCTGATCTCCCGAGAAGTTCACTATCGGGTTTCTCATTTGTTTCCCCGATGCCTCGCATGCTGGCTGCCTCACACTGCGTTCCCCAATCATATCGACGTAACCCTGACTTCCTGAATAGGGACCGAGTATCGAACCTGGGCACGGTTTCCTTTGAAAAATGAATAGAGTTCCTCTATGTAAGCCGCTATGCCAAAAAATTTAACGGAACTAGCGAAGACACCTCGTTGTATCTTAAGTTTGCAGACCGGATTGTACCGTTTGTGTTTACGTTAAGTCTTATTACAAATGTATACGTGCCGCCAAGCAGCGCAACACCTAGGTTGATTGGATCGAAGATAGCATCTGTAAAACAGGAAATACATCGCTGTGGCTCACCTTCCGCGGTCAGAGGGGAAAATGAAGCAGTGTCTAAACGAACTCCCCACTGCGGGATTAAAAGCGCTACTACAACTCGAGTAACGCGCATATCCGGGATTCCAATTGCAAATGCAGGAGTCGGCGTCGTGTGACCAACTAGGTAAGAGGCTTTGTTGCGCGATCAGAACCTGCCATGGGACCGGTGGACTAGAAATGCCGAATCACACATGACTATCAGGTCGAGTGTCCAGTTCAACTCGAGCGCTATATTAATAGGTTTCCCACTGGTCCGGTCTGCCCCGGTCTATACGCAATTGATTGATTATCCCTAGACTCATCCAAGAGGGTGGTCACTGACCCGATTCACTGTTAATAATCGGTACCTTTTGTTCTCCATACTCTACCCAACTTCCCAAGGGAGGCACTAAGGACAACCCACTGAGAGGAACATTCTGCTTCCTCGTCAACACCGCTACTGTCTTAACGTAACAAATGCTTACTCGCTCTTACGGAAGGTCAACCTAAGAAGTACGAGAGGCGGTGGTCGCCCTGAGGGTTCTTCCTCTTCACTACCTACGCATTCATTCGCTCT
GCGGTTCAGAGGAGAATTTATATTTGGTGTTTATCAGTTCCCTTCTTCAGTACCCGACACCCGGCGGCTACCGACTGGACGCTAAAAACGTCACCACTAAGGCGCATGTTCCAGCTCCCCACGGGAGTATATAAACATGGGACGCATCTGTTCGTCCAAAGTAAGGACCACCTGTAATTACATAGCGCACCTCGTAACGTTTTCCGCACAATCGAAGAGCCGTCACGCTACATGGCCACTGTACTGCTAGGTGAACGAGGTGTGCAGAAGAGTACACTAACGTCGTATCGATATGTTCCGACAGGAACGGTAACGACTAGGTTGCCTCGGGTATTGCCAACATCTGCAAGCCGCCAACGAAAACGCACGAGATAGTCTACGACGGGAAGCGGGACAGGAGAAGTTTTTACGCAGTTCACTCCACACGTGGGCAAGAAAGACGCCACGAAACCTAATGTAACTGAACTATATTGACTTCTAGATACTGATCCGACTACAGGCGTGTGACTACAAGATCTGCACATCGTTTTATTGAGTCACCAGGACCCCCCAAGGGGGACATATACTTGAAATACGTACTGTCACACTACGAACTGACTAGGGCCTCGTAATAGAGACCTGACCTATTATAAGCACTACACAGTCGTCCAGGGCATCTCGCGTTATTTGCGATTCAGTCCTAATCTCTAAGCACATCTAAGGACGTAACCTTTTTCGGGACCTAATCTCATGTATCGGGCCAATTTTTTATACTTATTCTATGAGGCCTGCCGAGGTACTCAGTCACTGATGCCGACACAAGCGATTATTCAGCGTAGTGCTCCGAGCTCATACTGGCCTAACATAGCAATAATTAAAGCGCTCCAGTGGACCCTGATTCCAAGTAATACGACAAACGTTGGTCGTCGAGAGCCTCGCTCTTGTGACCCACTTCTGTATACCTTCTCAGA
'''

ans = pmutation(fasta)
