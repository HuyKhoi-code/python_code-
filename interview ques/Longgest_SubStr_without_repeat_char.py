NO_OF_CHARS=256
def SubStr(s):
    n=len(s)
    last_index=[-1]* NO_OF_CHARS
    result=0
    i=0
    for j in range (0,n):
        i=max(i,last_index[ord(s[j])]+1)
        result= max(result,j-i+1)
        last_index[ord(s[j])]=j
    return result
s=str("geekforgeek")
print(SubStr(s))