import csv

amino_code = {}

with open('amino_acid.csv', 'r', encoding='utf-8-sig') as code:
    reader = csv.reader(code)
    amino_code={rows[0].strip():rows[1].rstrip() for rows in reader}

print(amino_code)


def coden(dna):
    dna_len = len(dna)
    codon_list= [dna[i:i+3] for i in range(0,dna_len,3)]
    amino_list = []

    for codon in codon_list:
        conv = codon.replace(codon,amino_code[codon])
        amino_list.append(conv)
    print(amino_list)
    amino_list.remove('Stop')
    print(amino_list)
    code = ''.join(amino_list)
    print(code)

    


dna = 'AUGAGGUCUAAUGUUAUUAUAGACAGGCCGGGUCGAAGGACUAGCUCUGCACGCCCGGACUGUAGGGUGUCAAGCUCCUGUCCCUGCCACAUUUUCCCUGGGUCUUGGUCCUCCAAUUUCGAGUCUGAUACAAGUGGCUCAUCCACGCUCUCUUUCGCCGCAAGAUACAAUAAGAAGACCUACGCUUGUAUGUCAGCGGGCGUCCCGGGGUAUGCAUCUCACUUGCGGGGCGAGCCACCCACACAUUAUUAUGUAUCUCAGAACCUCGGGGGACUGGCGAGUCGAGUUACGCAUCAAUCAUCUAGCAUGGCACCUUUACUACUCAGAAGCAGCUGGUAUAUAGUGCGCGGCUGCCACGGUGGCAAACGUGAACAUAUCGAAGUGCAUCUCUUGAUCAUUACAAAGCAGCCGUCGACUGCACUCAUAGGUGAUGCUACUGACGUUAGAGGAAGCCUAAGCCGUGGGCCAUCGAAAGGGCGGGUCAUGUAUAGAACCCAUGGCCUUCAGGCGAAAAUGCAGGAUUUUAAGCCCGUUUACCUAGUGCCUCAGUUAGAUGAAGACCGCUUUCUCAGGCUGAUGACUCAUGUGGGAUGCAAAAUUCCGGCGAUAAUUGGUGGCAUCCGCGUGGCCUGGUGUGCUCGGAUGUGGGUGCCGUCCUUGAUAAAUUAUCUAAAGUGUAACCGUAUAUUACUUCUAGUCCGUUCUCUCAAGGGUAACCCCACAAUGAUGGUCUAUUCUGGCGUUGAAAUUCGGCUCUCUAUAUUGCCAAAGGUGCAGACAUCUACCAUCGGUUGUUCCCAUGUCUUCAAUCAACGUCACAUUGCGAGGGGUUGCCCGUCAGGCAAGUUCGCGCUUGAGAAAUGCUGGGUCCGCCCCACAUACAAAGAUUUUUGGGGUGGCGUGCGAAAGUUGGGGAUCCACUGGACCCAGGUUCGGAAUGAAUGGCUUGUCAAACGGACUUCUUUUUUAGGCCUAGCAACGUUGGCUGAAACGAAGUACGAUCCACGAUGCCUGGAAAAGCCGGUGUUAGAGCGUAUUACUGGUGACUGUUUAACAGUAAACGCCACGCCGGGAUACUUACUCCGAGUACACUCUUUGUCACAGUGGCCUAAGACGUCUCGGUUAAUUCUAUGUUAUGGUGCAACGUUCUUGGGGGGGUGUCAGGGUGUGAAUCCUUCGGCGCUAUUAAAAUACGCUUAUCGACGUGCACUUGCCGAGGACGUAGUGACCAGGCCCGGACGAGGGCGGACAGGCCGAUACUGGAGGAGAGCCAAAACUCAAAUUAAGGCGCAAGCGCGUGGCUGGUGGUACGUUAAUAGGAACUUACGCGCACGGAGACGCCCGCCCAUCUCACGCCGCGUGAUCCGAAAUUACUACACAUCUAUUCCAGUGGGUGUUCGGUCGUCUACGAACGCCAGUUCCCUACCUCUCGGUCCGUGUAGAUCGGGGCCCACUACAGACGAAGGCUAUAUGCCAAGUGGACUCUAUCCGUCAAUAAAUCAGGUCCGGAGACACCGGCUAAUACGUUGCCUCGCCACCUUGAUGGGCUUCAUUACCUUGUCGCCCAUUGAAACCAAUACAUGUUCUCUUGCUCCCGCGCUGUGGCUAAAGGGCAGCAUCGGCUUGGUUGACAAUCUUCCAGUAUUAAACAAACAGGCCAAUAUGUCCAAGCUACAUGAUGUCACAUCAUCUGUGGUUUUAUCCGGGACACGUGAGGCCCGUCCUGGCCGAUUUAGACAUAGCUCUGGUAACGGGCUGUAUAUUCAGUCACACUACUUGAAAGACUUAGUUGGGGCCAGGGGCAGACUAGCGUGUAGUGCGAUACAACGUGUUGUUGAGAUUUGGACGUGGGCUCACCUUAUCAAACGCGUGUGUUAUAGCGGGGCGGUAACGCUCGGCCGCGAGUACGCGCCCUCGCAGUCGUGUUUGUCGGGCGUCGAAAUGCAUAGCGUGAUGAGUGCUCGAUGCUAUGGCUGGCCAAUAUACUUACAAAGCCAACAGUAUUGGGCGGUCAAAGGCUCACACCAUGACCACAUUCCGAGAAGCAUAUGGACGGUAGUGACGCUACGAGCCCAACUAGAGAAUCAUAUACACAUCAAUCGUGAUUCCUAUCAACGGCAUGUUAAAGGAAUAUAUGGUGUACUAAGCGCAAGCGUCUGGCACGCGACACGAUUCCCGCCUCUAGGCUCGUCCAUGUGGACAACACGAACGAGCUGUUAUGGAGGUCAAGCGAUACUGAUUUAUCGAGCUGAAUCCGCCAGUGAGAAAUAUCUGAACAUGUCUAAUGGGUGUCCCCGAAGCGUCAAAAGACUUAGGCCCUUAGGAGAGCCCUCGCAUAUAAAUCCAAAUGGGGCAGUAAUGCUGAGAGGCGACUAUUUUAAAACGGAUUCUAGUCGCGUUGCAUUACUCAAACUGACGGAUGAGUGGCUAAGAAUACCAUGUUCUCAGGAGACUCGAUGCGAGGUGCAGCUGUGGUUUCCGAGGUCCGGUUAUCCGCCCAGUCUCAUUGCAACAAAACUUAGUACCGCACAAUUGGCUCUCCGAGCUAUCUUGCUUCACGAGAUAACGGUUUGGACGCGUUCAGACUCAGCUCGACACCACGAGGAAGAGGGGCACCCUCGUGUAUUGCCUAAUGUACGCGAACGUACCUGUUUGGGCGUGUCCUUUAUUAUUGCAUCAGGAUAUAGCUCCGGGGUGCUACUCGCGAAGUCAGACCCAGCAACGUCUACCUCAUCAAGUAUCACCCAACGAAGAUCUUGUCAACAACUACGGUACUUACCCGACUUAUGUCUCUUUGCAUACUUUUUACCAACAGUAGCUAGUUACGUAGGUCACUCCCGCGAGCGAGAACUUUAUACUAUGUCGUAUCCCAGCUGUAUUCCAAGCCGGAACCGUUCCAAGCAAUAUUGCAGGGAGUCGGCACUCGAUACGCUCCGAGUCGUGUAUCUCAGAUCAUCGCAAAAACUUGAAUCUUUUUUUGGUUACGUGAGGGAAAGUGGCCAGCAUUUAGGAGUGUGGUUCGGGAACCAAACGUAUCCACGCACACCUAGGUUUGAUUCUACAGAAGAUGCUAAAGGCUGGACAACUACCACGGGUGGGGCAAAGGGCCCGAUUAUCAACUGGCCCGUUAUGGAUCGAAUACGGAUCGGAGGUACGUUGAAGCGGACGUCCCCUAUACGUCUUUUAAAGCGUCUUUACCGUAUCCUAAGGAGAUUUUUAACACACUGGUACUGUUCACUUGCGCUUGUACCUCCACUGCUCACUUGGUUGUUUGGUCGGCAUGUCAUACUCUUCGAGGACAAAACCUCAGAGACCGGAUCAAGUCUCGUUACAACUCUUGCUUCCAAGACCCUCUUCUGCAUGGCACAGACUUGGCUGUGCAAAUUCAACAGCGAGUGGAGCACGCUGUUCACGAGGCCAUCGUAUUGGUGCGAAUGCUAUGGAGACCUGCGCGACGGCGACACAGCAAGUACAUGUACCUGUCAGCGCCCAGCCAAUACCGUGUUGGUGAUCACUAGAACAUUCCGAGUCGACGUACGGAUAAAGUCCUCGGAGCCACCUCGGCAGAUCAAUCUUACGAUCCCACUGGAAUCACUGCGGUAUCGUUUCGCCGACUCAGCUUUCAGUGCUAGAUUGUUGCCAAAUUCAAGUUCUGUUAAUAACGACCGGCGACUGUCGAGUUCUCAGGUCCCGCGUAGCUGGACGGCAACUGCCGGACGGAGAACGGCCUCUGACUGCAUUGGCCGUCAUGAUUCCACUGAUUACAGGCACGAUUCCCCGCUUUCAGCCUACUUCGCUUCCGUUGGAUUUGAAAGGAGGGGUCCAGACUCAGUCCAUGUUCACCUUACGCUCCCCUUGCUAACUUGCCCGGAUAGCCAGUCUGCCGCGGCGGUCGAUCUUACUGUCGGUGGAUCUCCCUAUAACUUCGCUGUUACCCGUCCUCUGGAAGAAGUUAUUCCGGGUCAGUGCUUCCACGAGUCUAGUAAGCGGACGAGAGCGGCCCCGCCAUUUCACGAGGGCCGGGCUUUAAGAACAAAGAGGCGUGGUGGAACAGCUUCGAGUGGGAGGUCAAGUAUAUCUUACUGCGACCUUUCGCUUCCAGGAACGGUCCAUCGACGGGACCCCGAUAGAGCCCCGGCGCAUGGUCCCGUAUUACUUCUAGUUCAAACAAACAUUCGAUACAAUUCAUUAACCGAGAGCCCGAUAGCAUUGUUAAACGAGUUAGGUUUUGUGGCACUUCUGUAUGCCGUUACAGCCAUCAAAUGGGUUAUGAGUGAAUUUAUUACACGGAUUGCAUGGGCAUUCCAUAACUUGGUCCGAUCCGUGAACCUCGUGAAGCAGACUCUCUCGCGGCGUGUUCCGUUUUGCAGCCACGGAGACUGCCUCGAACAUAUCUGUAAUAUCAUCGGUUUCCAGUGGUGUGAACUAAGAGUUCGUCCACUGCGCAACCGCCCUGAAUAUAUCCUUGACCGGGGGGUUUCGUUUACACUCGACCCUUCCCUAAAAAGGUUUGCAAUGCGUGCGGUGUUAGAAGCUCUUACCUUCGGGCUGUAUUACCUAGGGACCCCACGGGCCAUUCGUCUCACUUGUCUAGAUUACUUUUACGAGCCCAAGCGGAACGUUCGUUUGUGUGGGCUCUGCCACAUCAUCGUAACGAUCUGCGCCGGUCUAGUUAACAUUAUGAGAAGUACUAGACCACUGGGUGGGUCCGCCCGGAAGAUUGACGAUACGAAAGCGCUCAAUAGCUGUCAUGGAUGUCUAAAUGCUCUGCACAUGAGACCAACUCAAAGUUGCCUCGGUGCAUCUCAAUAUACAGGUUAUUUGCCAUUGCCGAAUUCAACGAAUUCCCCGCUGUCGUCACUCCUUGAGCCCCACAUCUGUCCCAGACUCACAAUCGGCCGUCCCUUGUGUUGCGGUUUCCGAAAUGAGAUGGCAAAACGACGUCCCGAGUAUACCCCUAACUCAGAAUGUUAUCGGUAUGCACCAUGGGGUUCCAAAGGUAUGCUGAUCCGUCAGCCCAUCGCGUCCUUGAACCUUGAUUCCCUUCCAGUCGGGGGAUCUCGAAUCUAUUGCCAGGCUGCCGUCUUUAGACAGCCGGUCAAUGUCCUUCCUCGUGGUGGUUUCUUCGACAACUUAUGGCAUAAGAAGAUUUUAAAAAAUUGUUCUAGAAACUGCGCGGCAUCGAGUUUCAGCGCUAUCCUAUUGCGCGAGGAAGGACUUGCACACCGUGGGUUUCAGCCCCCGCCUCCCAAGCCGGUGGGGGAGUCUUCUUGGGUAGAGAGCGCCCGGUUGCACGGGGGUGAACCACGUAUUGCCGUGUCACAAGAGGAAGCACCUCCUGAGACAGCAAGUGGCACUGCCUGUAGCGUACUGUCCAGAAGUCAUUAUGGUUUUCGACCGGUCAGAUUUCUGAGAUGGACAGAAGCCCACAGUUAUGUGGCCCUCCCCUGGGGUGGUAACGGCAAAUGCCAGUACUUGCUGACUCGACUCGAACCGAAAUGUACCGCUAACCGUGUUCCUCCAACAAGACAACAGGAGCGCGCUAAAUUGUUCGUUGAUAACACUUGGCUGACCGGUGGGCAGGUUGAGGUAACAGAUCCCUCACAUCAGGUGCGCUAUAAGAGUGAAUCGGGCGUGGUGCUGCCUCCCCAAAUUAGCUUGGAUGGUAUGGGUCCCUCGCAGUAUGCGCCUAAUGACCGCCCAAGCACAUCCCUCAGCUCAUCCAAUGACGUCACAGUAAAUGCAGAGAAGUGGUGCCAACGACGGUAUCCCUUCCAUGUGGUCGUGGUCGCAUAUUGCAUCUUUGCGAAUAUGGGACGGCCUGACAGCUGCCAGCCAAGACCCCGACACUUUUCCAAAGCAGGACGGGCUUACCGAUUCCUUCAUUGUGAGGAAAGAAUUGACUAUUCGGGCCACCGCACGCACUAUUUGACGAGAACGUCCGAGGAGAUCUCCUACUUUCACUCAGGAAAGAUUGUUCGGACACCCAAGCCGGCCGCUCCACGCCGAAGAGGAGAAUUGAUAGAAAGCAAUAGAUGGCGGGUCCGGCGUACGAGUCUACGUAAUGGAAUAGAUAUAUCUACUACCUACGUUUCAAAGUGUGCUCAUCUAAUGACUGCGGCCUCCAGUCCUGACCUCCACGAGCUUCUGCCUCAUGCGACAGAAUGGGCACAAAUCAAAGAACCUUCCGUGUGGGUAAGACCCUCCUGGCCAGUGCAAGGGGAUAGCCUCGAUUCUGGGAACUACAGUUACAACACCCGGCCUUUAGUACGCCAUGCCCAGAGUGAGGGAAUUUUGACCAAACGCAGAUACAAGGUUAACGCUAGGGCAUGGGAGCAACGAUCCCCCUCCGGCGACUGUGAGAUGAACGGGACAGGAUUCCAAAAAGUUCGAUCGCAUUGCCUAACUUUUUACUGGCGUGCUGCAACUUUAGGUCGCCGUGGUACCAGUAGAGGCGGUCAAUGCUGGGUUUUAGUAUGCUACGUGAGAGAACAACUAUGCCGGACGGACAGCACGCUAGCGACUCACACGACGUUGAGAACUCCACUAGAAUACUGGCCUGCCGGGUCAAUGAUAUACGACUGCUUCGGAACCUCACGGCGUAAUUUCCUGCGAGACCUUGCCACAUCUGCUCUCUCUGGAGGGUUAGAGCUCAGUCCCACUCAGGCGGUGGUAUACAGGCUUUUUAGUUCUAUCAUCCCAUUUCUCUUUCUUGGGAACUCUAAGGCUCAUUCUUUAACUAUAGCCUGUGCGUUUCAACGUGCACGUGUAGACUCGGUCCCGCUGGGUUCAAAAGGGUUAAACGCGACUGCCUCGUGCAACGCUAUUAACGUGUCUGACAGAUUAUGUACGAUGCGUUACCCCUGUGCAACGGCGCACGGCUGGGGCAUAUUUCCAGAACAUGUGCAUGGGAAACUACUGGGCACUUCACGUGGCAGCGUUCGGUUGCGCGUCAAGUGCGGAUUUACCUCAGUUCCCAAUCGGAGCCGACGUGCGGGUAGAGACGCGUGGACUUACCUAACGCCAAGUCUUCAUACCAUGGCCGAUCGUGAAAGACAAAUCCGAGCUCCCAAUCAUGGUGGCUUAACGAGGGCAAGUUCAUCACCCAAUGGACUUGGAACUAUAGACCCUAAACUCCUCGUGCCCGAAUUGUUUGGGCGUAUCUACGCAAUCCUUCUGUUUGAUGUUGUGGGACUAAUCUGUAAGGACGUUGAACUGUCGUUUAGCCCGCACGAAAGUCUGACUGAUAGUUCGUCUGUGGGGUUUUGUUUAACAAUACGCUCCUUACCUAAUCAGGCACCCAAAUUGGAGGUCCAAUAUAGCGCCAAGCAGAUCCGCUCACCGUGUCUUCUUGCAAGCGCAUUUGACAAUUGUCAGGUAACGACGAGGUGGCUUUUGCCAUGUCACGUACGCGUCUGGGCCGCGACUGUAAUCGUUCGACGAAACUUUCGGUGCCUCAAACGAUCUACUUUAAUCCGGCUCCCACUGCACUGCAUGCCCUUCGAACAGACGUGUUUUAUCGACGGCAGCAAAAGAAUUCAAAAAAAGUGGGACUCUUGGGUGUCGUGUGGGCCCUCGAACUUCUACCGCGCAAUACGUGCAGUCGGCAGAACUACGAUUCCAGCGACAUGGUUUUUGAAAAGCCAUUCUCACGUUCUACUCCGCUAUACUGCCCUCCUCACUUCCAGUUCUCUUACCCGAGCUCCUUCAAGAUUGAAACCGGUGUCAGUGGCCGGCCGCUUUCCACUCGUCUAUAGCAAACACACUUGUGGACAAAUACGUUUGCAAACGAAGCGGAUAGUACGGGGACCUUUACGCGCUUACGAACUGAGCCGAUCGAGAAGCCCUGACGCUACACCUUCACUCCACCAGUCAGGACCAUGGGCCCCAUUAGGCAUUCGAGUAGGACCCGCUGCAGAAUCCCCUAUGUCUUCGCGAGUCUGCGGGUUUGGGCGUCUGACGCCCCAUCUAGACCAGUUCCAGUCAGAAACGAGAGUUAACAAUUACUACCUCCUCUGCGCUUGUGGUGUACACCAGCUCGGCACAAUCGCUCCGUUCACGAACCUCUCAGGAUUGGUUCCAAAAUCAUAUAAGCAGUUAUCCCCCUGCUUCGUGUUUUCUGCCAUGUCUGAUCUGUUCGCCUGCCCUUAUCCUCGAGCCCUGUAUAGAAUUCUUUAUACAGAUCCAUUGGGCGUCCUGUUGCGCAUACUCUGUCUAGAGAGCUACUGGGUUUACAUACUGUCCCUUCCAGCCGUACCCCGCAGCUUGUUGUGUGAAAAGUGGUUGAAUCCAACAGUUGUAUACGACGAUCUUCAUGGCGUUCGCGCCCCAACUGCAUUGCGCAGGUUUAGUCUUAGUGUCUGCUUCAUGCGCUGCCGCCGCAGCCCCUAUGAGUGGGUGCUCUCCUCGUCUAUCUAUCAUACUCCGCUUUUUAGCAGCACCACCAAAGUACGAGCGAUGGUGCGGCGUUUCGUGCGAAUACGCAUGCUUUCUAGCGUUAACAUGCACACUAUCUCUCGACUUAAGGCAACCUUACGGCCAGAAAAUAAAGGUGCAGCCCUGGUCAAGAACGACAUAAUCGAAUUCCCCGGCAGCGUUCAAUCUAGUGGAGUAAAGAUCCGUAGCACGCGGAUCAUGAUAAUCACAUCAUAUAUGAGUUUUCGUGCGUUUCAUCCGCCGCGUAUAUCGAGACCGGAAGUCCUAUGUCUCUCGGGUCUAUCAGCGCAGAGUUCGGGUUUCCCGGGUUUGGCCCCUUCCGAACGUGCGAACGAUGCAACAAAGCACAAUGCUAGGGGUGGUUUCGCGGCCCUUCAGUUCCCGGGAAACAAGUCGUUGCCCUCACGGUCGAGAGACGUGGAUCCAGCCCGGGAAUUGAUCGGCACGACGCAGAUCCAGUCAACAGGAGAGUUUACCUGGCUCCGCUCGGGGAUGGGGAGGGAACUGCGGACAGAAGACCGCAACUGGCUUCGGAACAUGAGAGGAAGGGAGGGUAAACGAUCGGCGCGAACAGCUCGACACCGCUAUACGAAUGUGCAUGCCGUUCUAAAAGAGUUUAGCCGAUAUAGCUCAGAUCGUUCUUGCGUCAGGUAUACGGACGCCGGCUGGGCUGCUGGGUUCAUCCCAGCGUCACUUGAUACUUUAAUCUCUCUCUGCGACCUAGCCCUGCAUACCACGCGGACGCAUAUCACCAGUGCCGUGACUAGACGACGAUAUUAUGGUAGCCCUACUGAAACGUACGGUCUACCGCCUUUUGACGGUAAUGGCUCUGCGGUGCGACUGCGGGUAGGCACUAACUCAGGAUAUGCUAGUGUGCAUCAACGACUAAUGAGGUUACGUAUGCCUGAUACGUGCUGUAUUGUAGUUGGGGCUAUAGGUCACAAGGAGUUAGGUACCGAAAAACACACAAGUUUCGGCAAUUGUGGUCCUAUUAUGAUCCGGUGUGCGGAGGUCUCGGCUACGACCCGGCGUGGAAAUCACUCGAAACCUUACAUCUACGUGUGGAUACGGGAAUCGCCUAUUUCAAGAACAAAGCGAGGCCCCAAGGCCAUGCGGGGACGCCUUCAAGCGUCGGUGCAGAUAGCUCUUACCUUUUGCCCCGGAACGAACGGGACCGUAUAG'
ans = coden(dna)