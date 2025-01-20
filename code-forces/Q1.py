import math

T = int(input())
for _ in range(T):
    N = int(input())
    k = 1
    while math.pow(5, k) < N:
        k += 1
    if k == 1:
        print("MIT time")
    else:
        print(f"MIT^{k} time")
