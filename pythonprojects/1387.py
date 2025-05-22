class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Helper function to calculate power value of a number
        def get_power(x: int) -> int:
            steps = 0
            while x != 1:
                if x % 2 == 0:  # If x is even
                    x = x // 2
                else:  # If x is odd
                    x = 3 * x + 1
                steps += 1
            return steps

        # Create list of tuples: (power_value, number)
        power_nums = []
        for num in range(lo, hi + 1):
            power = get_power(num)
            power_nums.append((power, num))

        # Sort by power value first, then by number
        power_nums.sort()

        # Return the k-th number (k is 1-based, so use k-1)
        return power_nums[k - 1][1]