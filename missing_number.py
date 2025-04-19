n=int(input())
arr=list(map(int, input().split()))
num=set(range(1,n+1))
missing_num=num-set(arr)
for i in missing_num:
    print(i)