import sys

input = sys.stdin.readline


def is_repetitive(s):
    """Check if the string is a valid repetitive string."""
    n = len(s)
    i = 0

    while i < n:
        if s[i] != 'M':  # Each repetitive substring must start with 'M'
            return False
        i += 1
        # Check for "IT" following 'M'
        if i >= n or s[i] != 'I':
            return False
        i += 1
        if i >= n or s[i] != 'T':
            return False
        i += 1
        # Consume any additional "IT" sequences
        while i < n - 1 and s[i] == 'I' and s[i + 1] == 'T':
            i += 2

    return i == n  # True if the entire string is processed


def main():
    T = int(input().strip())  # Number of test cases
    results = []

    for _ in range(T):
        n = int(input().strip())  # Length of the string
        s = input().strip()  # The string itself
        results.append("YES" if is_repetitive(s) else "NO")

    # Print all results
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
