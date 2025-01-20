def solve(s):
    if len(s) < 3:  # Minimum length must be 3 (MIT)
        return "NO"

    i = 0
    while i < len(s):
        # Each part must start with 'M'
        if s[i] != 'M':
            return "NO"
        i += 1

        # After M, must have at least one IT
        found_it = False
        while i < len(s) - 1:
            if s[i] == 'I' and s[i + 1] == 'T':
                found_it = True
                i += 2
            else:
                break

        if not found_it:
            return "NO"

    # If we've consumed the entire string successfully
    return "YES" if i == len(s) else "NO"


# Input handling
t = int(input())
for _ in range(t):
    n = int(input())  # Read `n`, though it's not used directly in the solution
    s = input()
    print(solve(s))
