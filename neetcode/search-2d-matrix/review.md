# 💡Approach

### edge cases

### brainstorm

- Bruteforce
    - go through each array and each elements in the array to find the target
- Binary Search
    - move l r across the arrays?

### plan

### time complexity

$O(m+n)$, Where `m` is the number of rows and `n` is the number of columns of matrix.

- The algorithm starts at the top-right corner of the matrix.
- At each step, you either move **left** (reduce the column index `c`) or **down** (increase the row index `r`).
- In the worst case, you traverse at most:
    - nnn steps moving left across the top row.
    - mmm steps moving down the rightmost column.

### space complexity

$O(1)$

- No additional memory is required

# 💡 Problem Analysis

### summary

- you are given a matrix that has elements in a non-decreasing order. return if the matrix contains target.

### code

`staricase`

```python
m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
```

### alternative approach

`binary search (onepass)`

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
        
TC: O(log(m*n)) #Binary search on m x n elements
SC: O(1)
```

- Treat the matrix as a flattened sorted array

### cause of failure

### take aways & key points

- if its big, move the array, if its small move the element index

# 💡 One Line Summary

<aside>
📌

start from the top-right corner of the matrix → if the value is greater than the target, move left → if the value is smaller than the target, move down → repeat until the target is found or out of bounds.

</aside>