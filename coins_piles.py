def remove_coins(a, b):
    if (a + b) % 3 != 0:
        return "NO"
    if min(a, b) * 2 < max(a, b):
        return "NO"
    return "YES"

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(remove_coins(a, b))
