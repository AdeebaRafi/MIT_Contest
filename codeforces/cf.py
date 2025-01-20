import sys

input = sys.stdin.readline


def is_repetitive_unit(s):
    # Check if a single unit is repetitive (M followed by one or more IT)
    if len(s) < 3 or s[0] != 'M':  # Minimum length is 3 (MIT)
        return False
    i = 1
    while i < len(s) - 1:
        if s[i] != 'I' or s[i + 1] != 'T':
            return False
        i += 2
    return i == len(s)  # Must end exactly after IT pattern


def can_split_into_repetitive(s):
    n = len(s)
    # Dynamic programming array to track if we can split string up to index i
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can be split

    # Try all possible splits
    for i in range(1, n + 1):
        # Try all possible lengths of last repetitive unit
        j = 3  # Minimum length of repetitive unit (MIT)
        while j <= i and j <= n:
            if dp[i - j] and is_repetitive_unit(s[i - j:i]):
                dp[i] = True
                break
            j += 2  # Next possible length (adding IT)

    return dp[n]


def main():
    T = int(input())
    results = []

    for _ in range(T):
        n = int(input())
        s = input().strip()
        results.append("YES" if can_split_into_repetitive(s) else "NO")

    # Print all results
    print('\n'.join(results))


if __name__ == "__main__":
    main()