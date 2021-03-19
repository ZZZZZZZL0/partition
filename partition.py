
def card(n,m,k):
    res = []
    if n < 0 or k > m*n:
        pass
    elif n == k or k == m*n:
        res = [k//n for i in range(n)]
    elif n == 1:
        res = [k]
    else:
        botj = max(k-(n-1)*m, 1)
        upj = min(m, k - (n - 1))
        for j in range(botj, upj+1):
            ocard = card(n - 1, m, k - j)
            if len(ocard) == 1:
                res.append([j]+ocard)
            elif len(ocard) > 1:
                for xc in ocard:
                    res.append([j] + xc)
    return res

print("Enter how many group you want to input:")
x = input()
cyc = int(x)


if cyc < 1:
    raise TypeError("Only the positive integer is allowed")
else:
    nmklist = []
    for i in range(cyc):
        str = input()
        strlist = str.split()
        for i in range(len(strlist)):
            strlist[i] = int(strlist[i])
        # length of strlist should be limited by 3
        nmklist.append(strlist)

    # start the computation
    for eitem in nmklist:
        # eitem = nmklist[0]
        n = eitem[0]
        m = eitem[1]
        k = eitem[2]
        # we should guarantee that 0 < n <= k <= m*n
        if n < 0 or k > m * n:
            print("wrong inputs of m n k")
        else:
            outres = card(n, m, k)
            print(len(outres))
