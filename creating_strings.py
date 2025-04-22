s=input()
perm=set()
counter={}
for c in s:
    counter[c]=1+counter.get(c,0)
def generate_st(cur_sub,counter):
    if len(cur_sub)==len(s):
        perm.add("".join(cur_sub[:]))
        return
    for c in counter:
        if counter[c]>0:
            cur_sub.append(c)
            counter[c]-=1
            generate_st(cur_sub,counter)
            cur_sub.pop()
            counter[c]+=1
generate_st([],counter)
print(len(perm))
for s in sorted(list(perm)):
    print(s)
