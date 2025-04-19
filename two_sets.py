n=int(input())
s=sum(range(1,n+1))
if s%2==1:
    print("NO")
else:
    print("YES")
    tar=s//2
    set1=[]
    set2=[]
    for i in range(n,0,-1):
        if tar>=i:
            set1.append(i)
            tar-=i
        else:
            set2.append(i)
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)

    