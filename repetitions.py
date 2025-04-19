s=input().strip()
max_cnt=1
cnt=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cnt+=1
        max_cnt=max(max_cnt,cnt)
    else:
        cnt=1
print(max_cnt)