# 💡Approach

### edge cases

- when there is a zero ⇒ all 0 except the indices with zero val
- one element ⇒ always 1 element

### brainstorm

- Bruteforce
    - for each element, copy the array then pop itself
    - multiply all the elements to each other, than append
- division
    - multiply everything then divide by itself
    - edge case for 0s
        - check if 0 in array
        - if it is, the “product” is everything multiplied without the zero
        - then index where zero was in holds that product
        - everything else is 0

### plan

- 0 in array:
    - remove all the 0s, then save product
    - for each element, if it’s not 0 ⇒ make it 0, if it is 0 ⇒ make it product
- no 0 in array:
    - save the product
    - for each element, replace it with product / itself

### time complexity

$O(n)$

- iterates through each element multiple times to find 0s, mutate elements, calculate product

### space complexity

$O(1)$

- creates a new array when there is a 0 in the array, but the output doesn’t count

# 💡 Problem Analysis

### summary

- return a list where each elements are equal to the product of all elements in the array excluding yourself

### code

```python
# https://neetcode.io/problems/products-of-array-discluding-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = nums.copy()
        p = 1
        lst_p = []

        if 0 in nums:
            lst.remove(0)

            for l in lst: p *= l

            for n in nums:
                elem = p if n == 0 else 0
                lst_p.append(p if n == 0 else 0)
        
        else:
            for l in lst: p *= l
            
            for n in nums:
                lst_p.append(p // n)
        
        return lst_p
```

### alternative approach

**division (cleaner)**

```python
# https://neetcode.io/problems/products-of-array-discluding-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
```

**prefix suffix product calculation**

```python
# https://neetcode.io/problems/products-of-array-discluding-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lst = [1] * len(nums)

        pref = 1

        for i in range(len(nums)):
            lst[i] = pref
            pref *= nums[i]
        
        suff = 1

        for i in range(len(nums)-1, -1, -1):
            lst[i] *= suff
            suff *= nums[i]
        
        return lst

```

- basically you can calculate the product of the prefix, product before that element, and suffix, product after that element.
- once you have that you can multiply those 2 to to retrieve the final product
- however having separate prefix and suffix array requires $O(n)$ **SC**
- so instead, we could just work on the final output array
- first put all the prefix values according to that element
- than calculate the suffix value and multiply in on the spot
- this leads to a $O(1)$ **SC**

### cause of failure

**List Copy**

```python
# WRONG!
lst = nums

# RIGHT
lst = nums.copy()
```

- python returns the referrence thus when you mutate `lst`, you’re mutating `nums`
- when you want to copy the list, you should use `.copy()`
- time complexity of `.copy()` is $O(n)$

### take aways & key points

`enumerate(*iterable*, *start=0*)`

```python
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))

# output:
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

- returns the element and the index, default starting at `0`

**prefix & suffix**

- instead of going through the array again to calculate the product of each prefixes and suffixes, you could keep an int variable that keeps track of it

# 💡 One Line Summary

<aside>
📌

create the output array → mutate elements to be the product of all the elements prior → mutate the elements again starting from the back by multiplying the product of all the elements after → product of pref. and suff. kept by var.

</aside>
