s= list(map(str,input().split()))
def check(x):
  count=0
  if (x[-4:]=='lios' or x[-5:]=='liala'):
    count+=1
  if (x[-3:]=='etr'or x[-4:]=='etra'):
    count+=2
  if (x[-6:]=='initis' or x[-6:]=='inites'):
    count+=3
  return count
def sex(x):
  t=0
  if (x[-4:]=='lios' or x[-4:]=='etr' or x[-6:]=='initis' ):
    t+=1
  if ( x[-5:]=='liala' or  x[-4:]=='etra' or x[-6:]=='inites'):
    t+=2
  return t
if (len(s)==1):
  if (check(s[0]) !=0):
    print ("YES")
  else:
    print ("NO")
else:
  m=1
  for i in range (len(s)):
    m*=sex(s[i])
  if (m==1 or m//(2**len(s))==1):
    arr=[]
    for i in range (len(s)):
      arr.append(check(s[i]))
    p=1
    for i in range (len(arr)):
        p*=arr[i]
    if (p%2!=0):
        print ("NO")
        exit()
    else:
        k=0
        for i in range (1,len(arr)):
            if (arr[i]==2):
                k+=1
                if(arr[i-1]!=1):
                    print ("NO")
                    exit()
            if (arr[i]==3):
                if (arr[i-1]==2):
                    if(i==1):
                        print('YES')
                        exit()
                    else:
                        if (arr[i-2]!=1):
                            print ("NO")
                            exit()
            if (arr[i]==1):
                if (arr[i-1]!=1):
                    print ("NO")
                    exit()
        if (k>1):
            print ("NO")
            exit()
        print ("YES")
  else:
      print ("NO")