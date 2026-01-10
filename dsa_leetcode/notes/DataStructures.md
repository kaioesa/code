# Data Structures

Data structures (ordered by level of importance, first is more important):
    More common DS --> More specific study: Changes to the algorithm, edge cases, additional follow-ups, etc:
        - Strings
        - Arrays
        - Hashmaps
        Respective solving patterns:
            - Greedy
            - Binary Search
            - Two Pointers
            - Sliding window
            - Backtracking

    Less common:
        - Trees
        - Matrix
        - Priority Queue
        Respective solving patterns:
            - Breadth-First-Search (BFS)
            - Depth-First-Search (DFS)
            - Recursion

    Rare:
        - Graph
        - Stack
        - Trie
        - Linked List
        Respective solving patterns:
            - Dynamic Programming (DP)
            - Monotonic Stack
            - Union Find

---

## Array 

Is a continuous memory space with data allocated in a certain order.

Most of the languages, we don't need to define / allocate the size of the array. This don't apply to Rust.****

Some languages like JS modify the actual implementation of the array based on how you want to display the data. A array of 8 bit can store the same data as the array of 32 bit, but when displayed, it will be different.

---

## Linked List

In a Linked List, the memory of each list is unrelated between other lists. When we create a relation between 2 lists, if we create a the pointer to a X space in memory and reference other Y space in memory, this becomes a linked list.


Given a N number of linked lists, if we have: 

- Bidirectional pointers -> Double Linked List
- Single directional pointers -> Single Linked List


### Big O for Linked List:

    Search:
    - Best case:
        - When reading the head or tail -> O(1)
    
    - Worst case:
        - When searching over all linked lists -> O(N)

    Write:
      - Best case:
          - When inserting a item at the head or tail -> O(1)
      
      - Worst case:
          - If need a lookup for the number, we have to search all over again and then insert -> O(N)
            - If not, then its -> O(1)

    Delete:
      - Best case:
          - When inserting a item at the head or tail -> O(1)
      
      - Worst case:
          - If need a lookup for the number, we have to search all over again and then insert -> O(N)
            - If not, then its -> O(1)

Code Implementation:

```Python
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_front(self, value):
    new_node = Node(value)

    new_node.next = self.head
    if self.head:
      self.head.prev = new_node
    else:
      self.tail = new_node

    self.head = new_node
  
  def add_to_end(self, value):
    new_node = Node(value)

    new_node.prev = self.tail
    if self.tail:
      self.tail.next = new_node
    else:
      self.head = new_node

    self.tail = new_node
  
  def remove_from_front(self) -> Node:
    if not self.head:
      return None

    removed_value = self.head.value
    
    self.head = self.head.next
    
    if self.head:
      self.head.prev = None
    else: 
      self.tail = None

    return removed_value

  def remove_from_end(self) -> Node:
    if not self.tail:
      return None

    removed_value = self.tail.value
    
    self.tail = self.tail.prev
    
    if self.tail:
      self.tail.next = None
    else: 
      self.tail = None

    return removed_value

```

---

## Queue

- FIFO, First In First Out
- Its implemented using Linked Lists at low level. Also, queues are used for buffering, stream of data, messaging, etc.

## Dequeue

- It's not FIFO
- Have bidirectional pointers across the linked lists. We can insert items in every position, and remove them also in every position of the dequeue.

---

## Hashmap

- In essentially a group of key / value. In Python, it's called dictionary.

- The main feature of hashmap is the searching, always O(1).

This feature is possible because of the hash function:
  - We have a input/request, and the hash function will do a operation to pointer to the slot of the array were we stored our respective value.

### Load Factor:

- Is the size difference between the data we stored and the size of the data structure.

- Given the following scenario, for example:
  - We have a hashmap of 10 spaces
  - We insert a name "John" at space 9
  - There's a certain chance, given the method of how we calculated the data and the mathematical operation, we well have to assign a chance to the data to be stored and retrieved every time consistently.

So, that said, when we fill the hashmap till a certain limit (let's define the limit is 70%), the structure will double the memory amount.

At the end, this is done to evict collisions.

At a low memory level, when we fill a certain threshold of the hashmap load factor, it will create a new array with double of the capacity (and memory), and then it will transfer all the data from the previous created hashmap.

Example:
HS: Hashmap
LF: Load Factor

HS -> LF = 0.3 -> iterates till a threshold... -> LF = 0.7 -> Creates a new HS with double the capacity -> old_HS => new_HS.

### Collisions:

To solve the problem of collisions, we got a key/value. So we can use the key to search for a specific item in the data structure.

How hashmaps handle large amounts of data: 
- Given a really large amount of spaces in a hashmap, we want to insert "John" at space 1 and "Doe" at space 10.
    - If we search for Doe, we will have to travel X amount of spaces to search, so: O(N)
    - If we encapsulate all names in a array or linked list, at space 0. We will get a search for names (O(1)) -> search in the very small array / LL -> and this leads to a (O(1)).
      - In fact, it would be O(N) by definition, but it's a very small sub-array, we can simplify and consider that O(1).


In resume:
- Insert, remove or search: O(1)
  - If we have collisions, a lot of items in a given space: O(N)

---

## Stack

- It's LIFO: Last In, First Out
- Implements Put and Pop.
  - We can conceptualize it with linked lists. Given a value 1, we append/put a value 2, create a relation 2 -> 1 and move the pointer of the last added (LIFO, right?).

---

## Binary Tree

- Its formed by nodes, have a head structure and have relationships to different other nodes. So, we can define it like a linked list which the first element have relationships for 2 other sons at the same time (right and left node).

### Tree

- Have more than two son nodes.

### Heap

- The head have the minor value, and the sons have a greater value than the father node. This logics extends to the infinity.

---

## Graph

- Is a data structure formed by nodes and vertices, the vertices indicates the relation between the nodes.

---

## Trie

- A tree formed by prefixes, prefix - tree -> trie.
- Is the data structure used for Markov chains (keyboard autocomplete, LLM, etc.)

---

## B-Tree

- Is a tree, self-balanced and have some principal rules:
  - Need to define the number of keys and the children, the nodes below
  - The number of children needs to be key + 1
  - All last nodes must be at the same level
  - When the last degree of nodes expand, the b-tree must balance itself