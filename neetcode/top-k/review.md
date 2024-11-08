# 💡Approach

### edge cases

- is the input always valid? (ie. k ≤ number of unique numbers)
- what if there are the same amount of numbers ⇒ always unique

### brainstorm

- Bruteforce
    - have a max int, and check each elements and compare the max value
    - if the current number has the highest max, append to the list to be returned
    - repeat for every element
- Sorting
    - sort the list
    - counter to check how many numbers of that number
- HashMap
    - key: number
    - value: occurrence
    - [?] is there a method to sort the dictionary in terms of keys/values? ⇒ [take aways & key points](https://www.notion.so/take-aways-key-points-137011ff45b9813c8015f05b35085a69?pvs=21)
    - since there are unique values, what if we make the key the occurrences? ⇒ but it can’t be mutable

### plan

- key: number
- value: occurrence
- Then swap key ↔ value
- make list out of the keys, sort it
- find `k` amount of max then append
- return list

---

above didn’t work out (check [cause of failure](https://www.notion.so/cause-of-failure-137011ff45b981b4a8f5f149838bdb87?pvs=21)), **plan B**:

- keep the dictionary the same, find a way to sort the dictionary by value
- search up how to sort by value (`sorted(dict, key=dict.get`)
- reverse the list, then take the slicing `[:k]`

### time complexity

$O(n \cdot logn)$, where `n` is the number of elements in the list

- since we are iterating through each elements in the list and sorting the list at the end

### space complexity

$O(n)$

- since we are creating a hashmap with each elements being a key in worst case

# 💡 Problem Analysis

### summary

- given a list of numbers and an int `k`, return the top `k` numbers that occurs the most in the list

### code

```python
# https://neetcode.io/problems/top-k-elements-in-list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst_h = {}
        sort = {}

        for n in nums:
            lst_h[n] = 1 + lst_h.get(n, 0)
        
        sort = sorted(lst_h, key=lst_h.get, reverse = True)
        
        return sort[:k]
```

### alternative approach

**Bucket Sort**

- basically you make a nested list where each index implies the occurrences of that number, and each element is a list of numbers with `i` occurrences (super smart)
- then return the last `k` elements

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/bfa07b4b-8514-4f55-8c7d-c784032b54c6/0cd9a7c3-272a-49eb-af44-61d3906c9c4f/image.png)

```python
# https://neetcode.io/problems/top-k-elements-in-list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst_h = {}
        lst = [[] for i in range(len(nums) + 1)]

        for n in nums:
            lst_h[n] = 1 + lst_h.get(n, 0)
        
        for key, val in lst_h.items():
            lst[val].append(key)
        
        topk = []

        for i in range(len(lst) - 1, 0, -1):
            for l in lst[i]:
                topk.append(l)
                if (len(topk) == k): return topk
```

### cause of failure

```python
# WRONG! (swapping keys <-> values)
for n in nums:
    lst_h[n] = 1 + lst_h.get(n, 0)

for key in lst_h:
    swap[lst_h[key]] = key
```

- swapping keys and values doesn’t work for the case where `{1: 1, 2: 1}`
- since there already exists the key 1, the next one is not generated

### take aways & key points

**Parameteres in `sorted()`**

```python
sorted(iterable, key=None, reverse=False)
```

- key is kind of like a lambda function applied to each elements in the iterable when being sorted

```python
sorted_keys = sorted(lst_h, key=lst_h.get)
```

- `lst_h.get` (no parentheses) : is a **function reference,** passes the method as a key function
- `lst_h.get()` (with parentheses) : calls the method immediately

**Sorting By Keys & Values**

```python
my_dict = {'b': 3, 'a': 1, 'c': 2}

by_key = dict(sorted(my_dict.items()))
by_value = {key: my_dict[key] for key in sorted(my_dict, key=my_dict.get)}

print(by_key)    # Output: {'a': 1, 'b': 2, 'c': 3}
print(by_value)  # Output: {'a': 1, 'c': 2, 'b': 3}
```

- `sorted(my_dict)` will return the **list** `['a', 'b', 'c']`
- `sorted(my_dict, key=my_dict.get)` will return the **list** `['a', 'c', 'b']`
- `.items()` returns the key & value, and `dict()` needs it because it needs the info of both keys and values

# 💡 One Line Summary

<aside>
📌

create hasmap {num:occurrences} → (sort the “key” list according to the values → return sliced list) || (create a nested list where indexes = occurrences, element = list of numbers → return the last k elements)

</aside>