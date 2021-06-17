f=open('C:/Users/Admin/Desktop/bb.txt')
arr=[]
b=[]
n=0
count=0
for i in range (9):
    arr.append(f.readline())
    n+=1
for i in range (n):
    for j in arr[i]:
        b.append(j)
for i in range (n-1):
    if(';' not in arr[i]):
        print ('error in line',i+1)
        break
    else:
        if ('clear' in arr[i]):
            print (''.join(b[6:8]),'= 0')
        if ('while'in arr[i]):
            count+=1
            start = arr[i].find("while") + len("while")
            end = arr[i].find("not")
            num = arr[i][start:end]
            print('while',num,'!= 0')
        if ('incr' in arr[i]):
            start = arr[i].find("incr") + len("incr")
            end = arr[i].find(";")
            numberincr = arr[i][start:end]
            print (numberincr,'+=1')
            continue
        if ('decr' in arr[i]):
            start = arr[i].find("decr") + len("decr")
            end = arr[i].find(";")
            numberdecr = arr[i][start:end]
            print (numberdecr,'-=1')
        if ('end'in arr[i]):
            count-=1
        if (count >1):
            print ('error: no end;')
            break


