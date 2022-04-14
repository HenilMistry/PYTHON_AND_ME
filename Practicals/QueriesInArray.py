n = int(input())
Q = int(input())
array = []

for i in range(n):
    array.append(int(input()))

for i in range(Q):
    start = int(input())
    end = int(input())
    min_elem = int(input())
    ans = 0

    for j in range(end-start):
        if array[j] > min_elem:
            ans = end - j
            break

    print(ans)
