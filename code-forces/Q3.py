import sys

T = int(input())
for _ in range(T):
    N = int(input())
    min_s = sys.maxsize  # Equivalent to LLONG_MAX in C++
    max_s = -sys.maxsize - 1  # Equivalent to LLONG_MIN in C++

    for _ in range(N):
        x, y = map(int, input().split())
        s = x + y
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s

    print(2 * (max_s - min_s))
