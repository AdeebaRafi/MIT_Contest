def is_valid_grid(grid, n, m):
    """Check if the grid satisfies the condition that no adjacent numbers are equal."""
    # Check horizontal adjacency
    for i in range(n):
        for j in range(m - 1):
            if grid[i][j] == grid[i][j + 1]:
                return False

    # Check vertical adjacency
    for i in range(n - 1):
        for j in range(m):
            if grid[i][j] == grid[i + 1][j]:
                return False

    return True


def get_possible_moves(grid, n, m):
    """Get all possible moves (positions where we can decrease a number)."""
    moves = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:  # Can only decrease positive numbers
                # Try decreasing the number
                grid[i][j] -= 1
                if is_valid_grid(grid, n, m):
                    moves.append((i, j))
                grid[i][j] += 1  # Restore the original value
    return moves


def winning_position(grid, n, m, cache=None):
    """
    Determine if the current position is winning using minimax with memoization.
    Returns True if current player wins, False if they lose.
    """
    if cache is None:
        cache = {}

    # Convert grid to tuple for hashing
    grid_tuple = tuple(tuple(row) for row in grid)
    if grid_tuple in cache:
        return cache[grid_tuple]

    moves = get_possible_moves(grid, n, m)
    if not moves:
        # If no moves available, current player loses
        cache[grid_tuple] = False
        return False

    # Try each possible move
    for i, j in moves:
        grid[i][j] -= 1  # Make move
        # If opponent loses after our move, we win
        if not winning_position(grid, n, m, cache):
            grid[i][j] += 1  # Restore grid
            cache[grid_tuple] = True
            return True
        grid[i][j] += 1  # Restore grid

    # If all moves lead to opponent winning, we lose
    cache[grid_tuple] = False
    return False


def solve_test_case():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    # Determine if Busy Beaver (first player) wins
    result = winning_position(grid, n, m)
    return "YES" if result else "NO"


# Process all test cases
def main():
    t = int(input())  # Number of test cases
    results = []
    for _ in range(t):
        result = solve_test_case()
        print(result)


if __name__ == "__main__":
    main()