# Python Practice Programs
---

### 1. Check for Palindrome

```python
s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")
```

---

### 2. Factorial of a Number

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

n = int(input("Enter number: "))
print("Factorial:", factorial(n))
```

---

### 3. Fibonacci Series

```python
n = int(input("Enter terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

---

### 4. Count Vowels in a String

```python
s = input("Enter string: ").lower()
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print("Vowel count:", count)
```

---

### 5. Reverse a Number

```python
n = int(input("Enter number: "))
print("Reversed:", int(str(n)[::-1]))
```

---

### 6. Anagram Check

```python
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")
```

---

### 7. Prime Number Check

```python
n = int(input("Enter number: "))
print("Prime" if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)) else "Not Prime")
```

---

### 8. Second Largest Element

```python
arr = list(map(int, input("Enter numbers: ").split()))
uniq = sorted(set(arr))
print("Second largest:", uniq[-2])
```

---

### 9. Find Duplicate Elements

```python
arr = list(map(int, input("Enter numbers: ").split()))
duplicates = set([x for x in arr if arr.count(x) > 1])
print("Duplicates:", duplicates)
```

---

### 10. Sum of Digits

```python
n = int(input("Enter number: "))
print("Sum of digits:", sum(map(int, str(n))))
```

---

### 11. Armstrong Number Check

```python
n = int(input("Enter number: "))
s = sum(int(d)**len(str(n)) for d in str(n))
print("Armstrong" if n == s else "Not Armstrong")
```

---

### 12. Balanced Parentheses

```python
def is_balanced(s):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

s = input("Enter expression: ")
print("Balanced" if is_balanced(s) else "Not Balanced")
```

---

### 13. String Compression (Run-Length Encoding)

```python
s = input("Enter string: ")
res, count = "", 1
for i in range(1, len(s)+1):
    if i < len(s) and s[i] == s[i-1]:
        count += 1
    else:
        res += s[i-1] + str(count)
        count = 1
print("Compressed:", res)
```

---

### 14. Find Missing Number in a List

```python
arr = list(map(int, input("Enter numbers: ").split()))
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
print("Missing number:", expected_sum - sum(arr))
```

---

### 15. Star Pattern - Pyramid

```python
n = int(input("Rows: "))
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))
```

---

### 16. Inverted Pyramid Pattern

```python
n = int(input("Rows: "))
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
```

---

### 17. Right-Angled Triangle Number Pattern

```python
n = int(input("Rows: "))
for i in range(1, n+1):
    print(" ".join(str(j) for j in range(1, i+1)))
```

---

### 18. Diamond Star Pattern

```python
n = int(input("Rows: "))
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))
for i in range(n-2, -1, -1):
    print(" "*(n-i-1) + "*"*(2*i+1))
```

---

### 19. Pascal’s Triangle

```python
from math import comb
n = int(input("Rows: "))
for i in range(n):
    print(" "*(n-i), end="")
    print(" ".join(str(comb(i, k)) for k in range(i+1)))
```

---

### 20. Hollow Square Pattern

```python
n = int(input("Size: "))
for i in range(n):
    for j in range(n):
        if i in (0, n-1) or j in (0, n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

---

### 21. Reverse Words in a Sentence

```python
s = input("Enter sentence: ")
print(" ".join(s.split()[::-1]))
```

---

### 22. Remove Duplicates from String

```python
s = input("Enter string: ")
res = ""
for ch in s:
    if ch not in res:
        res += ch
print("Without duplicates:", res)
```

---

### 23. Find the Longest Word

```python
s = input("Enter sentence: ").split()
print("Longest word:", max(s, key=len))
```

---

### 24. Count Frequency of Each Character

```python
s = input("Enter string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
```

---

### 25. Replace Spaces with Hyphens

```python
s = input("Enter string: ")
print(s.replace(" ", "-"))
```

---

# Additional Questions

---

# 🔹 Sorting & Searching

### 1. Bubble Sort

```python
arr = [5, 2, 9, 1, 5, 6]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Bubble Sort:", arr)
```

---

### 2. Selection Sort

```python
arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print("Selection Sort:", arr)
```

---

### 3. Insertion Sort

```python
arr = [12, 11, 13, 5, 6]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print("Insertion Sort:", arr)
```

---

### 4. Binary Search

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9]
print("Index:", binary_search(arr, 7))
```

---

# 🔹 Matrix Problems

### 5. Transpose of a Matrix

```python
mat = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print("Transpose:", transpose)
```

---

### 6. Print Diagonals

```python
mat = [[1,2,3],[4,5,6],[7,8,9]]
print("Primary diagonal:", [mat[i][i] for i in range(len(mat))])
print("Secondary diagonal:", [mat[i][len(mat)-i-1] for i in range(len(mat))])
```

---

### 7. Rotate Matrix 90°

```python
mat = [[1,2,3],[4,5,6],[7,8,9]]
rotated = list(zip(*mat[::-1]))
print("Rotated 90°:", rotated)
```

---

# 🔹 String Manipulation

### 8. Check Rotation

```python
s1, s2 = "abcde", "cdeab"
print("Rotation" if len(s1)==len(s2) and s2 in s1+s1 else "Not Rotation")
```

---

### 9. Longest Palindrome Substring (brute force)

```python
def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = s[i:j+1]
            if temp == temp[::-1] and len(temp) > len(res):
                res = temp
    return res

print("Longest Palindrome:", longest_palindrome("babad"))
```

---

### 10. Remove Special Characters

```python
import re
s = "he@llo! wo#rld123"
print(re.sub(r'[^a-zA-Z0-9 ]', '', s))
```

---

# 🔹 Array / List Problems

### 11. Majority Element

```python
arr = [3,3,4,2,4,4,2,4,4]
print("Majority element:", max(set(arr), key=arr.count))
```

---

### 12. Kadane’s Algorithm

```python
arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum, curr_sum = arr[0], 0
for x in arr:
    curr_sum = max(x, curr_sum + x)
    max_sum = max(max_sum, curr_sum)
print("Max Subarray Sum:", max_sum)
```

---

### 13. Move Zeros to End

```python
arr = [0,1,0,3,12]
res = [x for x in arr if x != 0] + [0]*arr.count(0)
print("After moving zeros:", res)
```

---

### 14. Merge Two Sorted Arrays

```python
a, b = [1,3,5], [2,4,6]
merged = sorted(a+b)
print("Merged:", merged)
```

---

# 🔹 Stack & Queue

### 15. Stack using List

```python
stack = []
stack.append(10)
stack.append(20)
print(stack.pop())  # 20
```

---

### 16. Queue using Deque

```python
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
print(queue.popleft())  # 10
```

---

# 🔹 Recursion

### 17. GCD (Euclidean)

```python
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print("GCD:", gcd(56, 98))
```

---

### 18. Tower of Hanoi

```python
def hanoi(n, source, target, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, aux, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, aux, target, source)

hanoi(3, 'A', 'C', 'B')
```

---

### 19. Generate Subsets

```python
def subsets(nums):
    res = [[]]
    for num in nums:
        res += [x+[num] for x in res]
    return res

print("Subsets:", subsets([1,2,3]))
```

---

# 🔹 Hashing Problems

### 20. Two-Sum

```python
arr, target = [2,7,11,15], 9
seen = {}
for i, num in enumerate(arr):
    if target-num in seen:
        print("Indices:", (seen[target-num], i))
    seen[num] = i
```

---

### 21. Subarray with Given Sum

```python
arr, target = [1,4,20,3,10,5], 33
s, curr_sum = 0, 0
for e in range(len(arr)):
    curr_sum += arr[e]
    while curr_sum > target:
        curr_sum -= arr[s]
        s += 1
    if curr_sum == target:
        print("Subarray:", arr[s:e+1])
        break
```

---
