# DSA Patterns

## Kind of problem / Patterns / Problems

## Arrays

For operations like array manipulation, sorting or selection, we can use Contains Duplicate as a base case.

[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)

Similar problems:

- [Two Sum](https://leetcode.com/problems/two-sum/)
- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Cheat sheet:

- If need quick lookup/count -> HashMap
- If sorted array or pair finding -> Two Pointers
- If sub-array/substring -> Sliding window
- If sorted array search -> Binary Search

### Two pointers

Best pattern for:

- Sorted Arrays, pair finding.

Key syntax to learn:

- How to do a loop in Python / Java

Solution:

```Java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        if (nums == null) {
            return false;
        }

        // Optimal Space Solution
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;

        
        // Optimal Time Solution
        var hs = new HashSet<Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            if (hs.contains(nums[i])) {
                return true;
            }
            hs.add(nums[i]);
        }

        return false;

        // Bruteforce Solution
        for (int i = 0; i < nums.length; i++) {
            for (int y = i + 1; y < nums.length; y++) {
                if (nums[i] == nums[y]) {
                    return true;
                } 
            }
        }
        return false;
    }
}
```

Line of thought:

- At this problem, we need to verify if there's any duplicate of any number AT LEAST ONCE in the array.

- The brute force method:
  - Create two pointers, x and y, which loops iteratively, one of them nested through the array. At the inner loop, we have to check if it's equals to the first pointer and return the correct answer, in this case, true.

  - TC: O(n2) -> nested loops, so linear time squared.
  - SC: O(1) -> i[0] == j[0]

- The optimal time method:
  - We create a HashSet as hs
  - In the loop, we get nums[i], if doesn't contains in the hs, we continue and add nums[i] to the hs.
  - Now, if there's any duplicate in the hs, it will return true.

### HashMap/HashSet

Best pattern for:

- HashMaps/HashSets are frequently used for Frequency Count technique implementation
  - Frequency Count is a technique to solve a problem aggregating data before processing it
    - Some of the use cases are:
      - Group items
      - Verify if there's the same elements (without a specific order)

Let's use the ValidateAnagram problem for exemplifying the usage of HashMap.

Similar problems:

- ValidAnagram
- RansomNote

Key syntax to learn:

- How to declare a HashMap an handle it: add, count, get the size, keys and values, etc.

Solution:

```Java
class Solution {
    public boolean isAnagram(String s, String t) {
        
        // First Solution 
        if (arrayS.length != arrayT.length) {
            return false;
        }

        char[] arrayS = s.toCharArray();
        char[] arrayT = t.toCharArray();

        var hs = new HashMap<String, String>(arrayS, arrayT);

        Arrays.sort(arrayS);
        Arrays.sort(arrayT);


        for (int i = 0; i < arrayS.length; i++) {    
            if (arrayS[i] == arrayT[i]) {
                continue;
            } else {
                return false;
            }
        }

        return true;

        // Optimal Solution

        var hm = new HashMap<Character, Integer>();

        if (s.length() != t.length()) return false;

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            hm.put(c, hm.getOrDefault(c, 0) + 1);
        }

        for (int y = 0; y < t.length(); y++) {
            char c = t.charAt(y);
            hm.put(c, hm.getOrDefault(c, 0) - 1);
        }

        for (int x: hm.values()) {
            if (x != 0) {
                return false;
            }
        }

        return true;
    }
}
```

Line of thought:

- For this problem at the most optimal solution, we want to implement the Frequency Count pattern.
  - We want to count how many times a certain item appears at the data we stored at the HashMap.
  - The solution need to 's' and 't' to be the same length, if not, we return false, because there's no anagram with different sizes.
  - Then, we count all letters of string 's', map to a HashMap. When this is done, we iterate over the letters in string 't', we decrement each found letter in the string 't'.
  - Finally, if the all hasmap values are 0, we return true, because there's the same letters in both arrays.

Big O analysis:

- We have some loops, but the loops are not nested, so each loop is O(N).
- Searching in the hashmap is linear, but as we are retrained at alphanumeric symbols, we have a limited possibility of letters. So the time complexity is O(k), were 'k' is the max possible letters, in this case, 26.
- We do not create or iterate over any other data than a HashMap, so the space complexity is O(1).

When calculating the overall complexity we have the following equation:

- Time: N + N + 1 = O(N)
  - To this operation we level the final result with the most heavy time complexity in the algorithm, in this case, O(N).  
- Space: O(1)

TLDR: count letters from string 1, decrement the count for found letters at string 2, then compare if all values are 0, if its 0, is a anagram.

---

### Binary Search

- When using this strategy, we have to consider two scenarios: a ordered array of itens, and an unordered one.

Ordered Scenario:
  - The main concept of the binary search, is to have a target element and split the array and sub-arrays using the target till find the closes target element.

Big O analysis:

- Time O(LOG N) -> doubles the elements quantity and iterate the number of steps.
- Space: O(1) -> we don't need to create a new structure / allocate more memory

Code Example:
```Python
def binary_search(nums, n):
    lo = 0
    hi = len(nums)
    steps = 0
    while lo < hi:
        steps += 1
    mid = int((lo + hi) / 2)

    if nums(mid) == n:
        print("step: ", steps)
        return mid
    elif nums(mid) < n:
        lo = mid + 1
    else:
        hi = mid
    return -1
```

### Sliding Window

- The Sliding Window strategy is more applied to problems where you need to get certain intervals and verify or transform the data.
- There's a common pattern for it implementation:
  - Usually, there's two while, one contracting and other retracting the window:
    - While R.
    - Inside there's a While iterating L.

- The logic for getting a certain data, the conditional declarations and so, it depends from problem to problem.
  - Usually, we can use HashMap / HashSet in many scenarios

Code Example:
```Python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        _max = 1
        counter = {}

        counter[s[0]] = 1

        while r < len(s) -1:
            r+=1
            if counter.get(s[r]):
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1

            while counter[s[r]] == 3:
                counter[s[l]] -= 1
                l += 1
            _max = max(_max, r-l+1)
        
        return _max
```

---

### Exponential Search

- Exponential Search it's more applied to massive arrays, because of the exponential nature of it. 
  - We need to create two pointers, the same case as Binary Search, and we'll be exponentially iterate one of the pointers.
  - Pointer R, each time, L will have the previous value of R.
- When we get the ideal sub-array (a window with our target inside), we'll do a Binary Search inside this window.

Big O analysis:
- Time: O(LOG N)
- Space: O(1)

Code Example:
```Python
def binary_search(nums, n, lo=8, hi=None):
    if hi is None:
        hi = len(nums) - 1
    while lo < hi:
        mid = int((10 + hi) / 2)
    if nums[mid] == n:
        return mid
    elif nums[mid] < n:
        lo = mid + 1
    else:
        hi = mid
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] < target:
        i *= 2
    if arr[i] == target:
        return 1
    return binary_search(arr, target, 1 // 2, min(i, n - 1))
```

---