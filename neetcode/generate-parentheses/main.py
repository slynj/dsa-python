class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                results.append(current)
                return
            
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        results = []
        backtrack("", 0, 0)
        return results

