n=int(input())
count_zeros = 0
while n >= 5:
    n //= 5
    count_zeros += n

print(count_zeros)
    
