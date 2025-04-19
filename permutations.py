p=int(input())
if p==1:
    print(1)
elif p==2 or p==3:
    print("NO SOLUTION")
else:
    even=list(range(2,p+1,2))
    odds=list(range(1,p+1,2))
    perm=even+odds
    print(*perm)

# imp sum
# The idea: split numbers into evens and odds
    # Putting all even numbers first, then odd numbers,
    # ensures that no two adjacent numbers will differ by 1.
    # Because:
    # - Even numbers are at least 2 apart from each other
    # - Odd numbers are also at least 2 apart
    # - The last even and first odd differ by at least 2