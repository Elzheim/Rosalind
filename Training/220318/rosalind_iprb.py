import math

def medel(hom,het,rec):
    pop_total = 4*math.comb(hom+het+rec,2)

    dom_total = 4*math.comb(hom,2)+4*hom*het+4*hom*rec+3*math.comb(het,2)+2*het*rec

    phom = dom_total/pop_total

    print(phom)

    rec_total = 4*math.comb(rec,2)+2*rec*het + math.comb(het,2)
    prec = rec_total/pop_total
    print(1-prec)

ans = medel(30,18,26)


#https://stackoverflow.com/questions/25119106/rosalind-mendels-first-law-iprb