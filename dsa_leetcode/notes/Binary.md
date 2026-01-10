# Binary  

Doubles each field, base 2, of course.

First bit -> tells if the number is positive or negative

2^0 -> Last bit (from left to right) -> parity bit -> tells if the field is odd or even

## Bitwise Operators

### Shift

Shift moves defined number of spaces for X number of positions, left or right. The operation must respect the limit of the given type: left shift can't left shift a value greater than the type allows, 32 bit, 64 bit, etc.

- 5 >> 1 -> select 5 spaces, shift 1 to left. 
  - 00101 -> 00010 

- 5 << 1 -> select 5 spaces, shift 1 to right. 
  - 00101 -> 01010 


## Operators

The operators are used to handle binary values. It's different from the high level implementation, it handles the logic considering the binary value and how it sums, etc.

| - OR Operator:
- Compares if a number in the same position is equal to it, it one of them is 1, it's true = 1
  - 100 | 010 | 001 -> 111

& - AND Operator:
- Compares if a number in the same position is equal to it:
  - 1101 & 0101 = True
  - All N&N = N.
    - 5&5 = 5 
  - All N & last_bit -> odd or even -> 0 or 1
    - Example: 5&1 = 1, 4&1 = 0 

^ - XOR Operator:
- If a number in the same position is equal to 1, returns true / 1.
- Else, returns 0.
    - Example:
    - 6^2 = 4
    - 110 ^ 010 = 100


NOT -> Get the compliment of X number, to get 1.

---

