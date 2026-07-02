class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, path):

            # Store current subset
            result.append(path[:])

            # Try every possible next element
            for i in range(start, len(nums)):

                # Choose
                path.append(nums[i])

                # Explore
                backtrack(i + 1, path)

                # Undo (Backtrack)
                path.pop()

        backtrack(0, [])

        return result