def Floyd(num):
    rua=num[0]
    tho=num[0]
    while True:
        rua=num[rua]
        tho=num[num[tho]]
        if (rua==tho):
            break
    pt1=num[0]
    pt2=rua
    while (pt1!=pt2):
        pt1=num[pt1]
        pt2=num[pt2]
    return tho
print (Floyd([3,1,4,5,6,2,7,5]))