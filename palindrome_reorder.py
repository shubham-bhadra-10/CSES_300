s = input()
d={}
for c in s:
    d[c] = d.get(c, 0) + 1
odd_count = 0
odd_char = ''
for c in d:
    if d[c] % 2 != 0:
        odd_count += 1
        odd_char = c
if odd_count > 1:
    print("NO SOLUTION")
else:
    half = ''
    middle = ''
    for c in sorted(d):
        count = d[c]
        if count % 2 == 0:
            half += c * (count // 2)
        else:
            half += c * (count // 2)
            middle = c * count  
    print(half + middle + half[::-1])
