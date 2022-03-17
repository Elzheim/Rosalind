def rabbit(n,m):
    rabbits = [1,1]
    for i in range(2,n):
        if i>1 and i<=m-1:
            rabbits.append(rabbits[i-1]+rabbits[i-2])
        elif i>m-1:
            rabbits.append(sum(rabbits[i-m:i-1]))
    print(rabbits)
    return rabbits[-1]

ans = rabbit(81,20)
print(ans)