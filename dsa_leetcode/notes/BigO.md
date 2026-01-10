# Big O

At interviews, we always seek for the worst case scenario, and we want to be the least bad one.

Is about scale, not performance it self.


### Space Complexity:

    N -> we alocate N number of new data structures
    
    1 -> we alocate a fix number of data structures

### Time Complexity:
    Log N -> exponentially increase the load, but increase the iterations needed linearly.
        - Example: binary search algorithm:
        - Log(10) -> 3.32 -> array with 10 itens takes 3 iterations to find the target
        - Log(20) -> 4.32 -> array with 20 itens takes 4 iterations to find the target

    N -> linearly.

    N^2 -> for inside a for
        - Example: Bubble Sort

    N LOG N -> Usually this mean a algorith that travels a structure, while deepens in their depth
        - Example: Sorting, divide and conquer algoritms
          - Travels a structure -> O(N)
          - Deepens every step -> O(LOG N)
          - So: O(N) + O(LOG N) = O(N LOG N)


Some rare cases, just for knowledge: 

    2^N -> rare in a interview, just for reference.

    sqrt of N -> Exponential Search

    O(N!) -> a bad implementation of fibonacci