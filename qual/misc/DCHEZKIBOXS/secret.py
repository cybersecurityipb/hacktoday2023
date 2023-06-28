def get_password(s):
    pl="DCHEZKIBOXS"
    b={}
    for i in range(65,91):
        b[chr(i)]=0
    for i in range(0,len(pl)):
        b[pl[i]]=1
    n=len(s)
    l=0
    r=l
    v=[]
    mx=0
    password=""
    while(l<n and r<n):
        if(b[s[l]]==1):
            if(r+1>=n):
                break
            r+=1
            while(b[s[r]]==1 and r<n):
                r+=1
                if(r==n):
                    break
            tmp=s[l:r]
            sz=len(tmp)
            if(sz>mx):
                mx=sz
                password=tmp
            l=r
        else:
            r=l
        l+=1

    return password
