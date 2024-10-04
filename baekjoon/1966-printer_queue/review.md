# 💡  problem analysis & summary

- Determine the print order of a specified document in a queue of documents, where each document has a specific importance level.
- The printer follows a rule where it prints only the document with the highest importance currently in the queue.
- **Process**:
    - For each document at the front of the queue, check if any document behind it has a higher importance.
    - If such a document exists, move the front document to the back of the queue.
    - If not, print the front document.
- **Goal**: Find the print position (order) of the specified document.

# 💡  algorithm structure

- Use a `deque` to store each document.
- For each second:
    - Dequeue the front document.
    - Check if there are any documents with higher importance in the queue.
        - If yes, move the document to the back.
        - If no, print the document and increment the count of printed documents.
    - If the printed document is the one we’re tracking, return the current print count.
- Repeat the above logic.

# 💡  code

```python
from collections import deque

def printer_queue(n, m, priorities):
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])
    count = 0 
    
    while queue:
        current = queue.popleft()
        
        if any(current[1] < item[1] for item in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == m:
                return count

test_cases = int(input())
results = []

for _ in range(test_cases):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    results.append(printer_queue(n, m, priorities))

for result in results:
    print(result)
```

# 💡  time complexity

`O(N^2)`, where `n` is the number of documents.

- Each document may be moved to the back of the queue multiple times, and for each document, we check the priority of all remaining documents in the queue.

# 💡  cause of failure

- Was not looping through again to check the priorities of the rest of the documents.

# 💡  fix & alternative approach

- Had to add another logic for looping through the queue
- maybe using sorting? Some kind of sorted data list

# 💡  take aways & key points

- Properly comparing each document’s priority in each step!
- Maintaining index to identify the target document after reorderings (that might happen).