# Sorting

Sort Algorithms have different use cases, and so, different performances.

### Bubble Sort

Iterate in runtime creating a "bubble", store the data and swap the value to the correct order. 

Advantages:
- Don't persist data in memory

Disadvantages:
- It's iteractive, so, always linear time complexity.

Big O

- Time:
  - Best case: O(N)
  - Worst case: O(N^2)

- Space:
  - O(1) -> Don't create any new data structure / persist data in memory 


Code:

```Python

def bubble(nums):
    size = len(nums)
    for _ in nums: 
        is_sorted = True
        for i in range(nums - 1):
            if nums[i] > nums[i + 1]:
                is_sorted = False
                nums[i + 1], nums[i] = nums[i], nums[i + 1]

        if is_sorted:
            return

```

---

### Quicksort

It's a Divide and Conquer algorithm. It get's a pivot, and create pointers to find the greater and lesser numbers than the pivot.

Given this sub-array, it will switch the position accordingly with the pivot and go to the next position.

It will do this recursively. Changing the pivot at each iteration.

Advantages:
- Its efficient and one of the best sorting algorithm for generic problems. 
- Really good for array problems!

Disadvantages:
- Deep recursion (can cause Stack Overflow)
- Poor decision when choosing the pivot leads to a worst time complexity.

Big O:

- Time:
  - Best / Average case: O(N log N)
  - Worst case: O(N^2)

- Space:
  - Best / Average case: O(log N)
  - Worst case: N

Code:

The Recursive way:
```Python


def quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi-1)
        quicksort(arr, pi-1, right)

def partition(arr, left, right):
    pivot = arr[right] # There's many strategies to select the best pivot.

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # sorting considering the pivot position
        arr[i + 1], arr[right] = arr[right], arr[i+1] # inserting the pivot at the right place.
```

The List Comprehension way (Python exclusive and not in-place):
```Python


def quicksort(arr, left, right):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        bigger_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(bigger_than_pivot)

```

### MergeSort

It's implemented using two pointers, a slow and a fast one. Using this pointers, we will split the data, and iterate recursively till we have the elements properly separated.

After the recursion, we will combine the parts comparing and sorting the values.

Advantages:
- Really good for linked list problems!

Big O:

- Time:
  - Best / Average case: O(N log N)
  - Worst case: O(N^2)

- Space:
  - O(log N) -> Proportional to the data length.

Code:

The implementation is quite tricky to memorize:
- It need to:
  - find the middle of the linked list
  - break the two parts and cease the relation
  - sort each part
  - recurse till head or head.next == None

```Python

# Simple Linked List implementation
class Node: 
    __init__(self, val, next=None):
        self.val = val
        self.next = next

# node_1 = Node(1) 
# node_2 = Node(7, next=node_1) 
# node_2 = [7,1]


def find_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow # middle of the linked list.

def merge(l1, l2 ):
    # Dummy Node pattern: head == dummy and tail == actual
    head = Node()
    tail = head
    
    while l1 and l2:
        if l1 < l2:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    tail.next = l1 or l2
    return head.next


def mergesort(head):
    if not head or head.next:
        return head
    
    middle = find_middle(head)
    after_middle = middle.next

    middle.next = None # split the relation between after_middle and middle

    left = mergesort(head)
    right = mergesort(after_middle)


    sorted_list = merge(left, right)

    return sorted_list
```