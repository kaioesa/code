For LeetCode Linked Lists related problems, the main patterns are:

# The Dummy Node pattern

When we want to do some validation or selection, the Dummy Node pattern is very useful. With this pattern, we create a empty Node to persist the initial value, and other 'actual' to persist the final LinkedList.

- For problems like merge linked lists, select N elements from linked lists, it's simple:
  - the 'actual' variable it's iterated like:
    - To persist: actual.next = list1
      - list1 = 1
      - actual.next = 1
      - actual = 0
    - To move the pointer: actual = actual.next
      - actual.next = None
      - actual = 1

Important concepts:
- We need to move the pointer
- The actual node is called with the variable, not 'val' or other property.

---
  
## Persistence Strategy
Most of the problems you need to reorder, select a sequel of specific nodes, or something.

For this problems, there's two ways to solve it:
- Create some persistence and iterate over it, generally:
  - We can save the position in a hashset or hashmap and do the specific logic from it
  - For example: You can map a linked list in a hashset and iterate over to find a cycle, the inverse of it

Big O:
- Time: 
  - O(N) --> If you need to map the entire thing and just iterate over it.
  - O(N^2) --> If you need to nest conditions
- Space: O(N) --> If you need to map the entire thing, the new data structure need to have some specific value given the original LinkedList 

---  

## Two Pointers Strategy
The most simple way, and don't have to create new data structures into the memory most of the times:
    - Apply the Two Pointer strategy, at this time, you may want to create a fast pointer and a slow pointer, and given a validation or logic, you implement at the runtime, without new data structures.

Big O:
- Time: 
  - O(N) --> If you need to iterate over it.
  - O(N^2) --> If you need to nest conditions
- Space: O(1) --> We don't create new data structures
