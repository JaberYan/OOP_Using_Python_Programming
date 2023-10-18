N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Calculate the prefix sum
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + A[i]

# Process the queries
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1  # Adjust L to be 0-based index
    R -= 1  # Adjust R to be 0-based index
    
    # Calculate the sum from L to R using the prefix sum
    query_result = prefix_sum[R + 1] - prefix_sum[L]
    print(query_result)
