class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr: List[int] = [first]

        for i in range(len(encoded)):

            # arr[i+1] = encoded[i] ^ arr[i]
            next_elem = encoded[i] ^ arr[i]
            arr.append(next_elem)

        return arr