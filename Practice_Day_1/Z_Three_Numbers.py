K, S = map(int, input().split())

count = 0

# Loop through all possible values of X, Y, and Z
for X in range(K + 1):
    for Y in range(K + 1):
        Z = S - X - Y
        if 0 <= Z <= K:
            count += 1

print(count)
