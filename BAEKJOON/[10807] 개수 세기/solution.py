from collections import Counter

N = int(input())
arr = list(map(int, input().split()))

V = int(input())
counter = Counter(arr)[V]

print(counter)