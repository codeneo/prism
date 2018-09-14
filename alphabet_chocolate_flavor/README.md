## The Alphabet Chocolate

### Problem Statement
A long chocolate was given as a gift to Alice by Bob. The chocolate is a series of square tiles connected to each other in a straight line. Each chocolate piece contains an alphabet carved on it. Now Alice picks a single part of chocolate and eats it. Taste of a chocolate's part is determined by how many squares are there in that part on which a vowel is carved. Since there are lots of ways for Alice to choose her chocolate part, find the sum of tastes of all the possible chocolate parts that can be cut out of the given chocolate.

> Note: Vowels are any of the following alphabets: aeiouAEIOU


### Input format:
- First line contains an integer **_T_**, denoting the number of test cases.
- Each of the next **_T_** lines contains a string **_S_** which denotes the design of the chocolate as mentioned in the problem.

### Output format:
- For each test case, print the value of taste sum as mentioned in the problem.
- Answer for each test case should be printed in a new line.

### Constraints:

- 1 &le; **_T_** &le; 10
- 1 &le; |**_S_**| &le; 10<sup>5</sup> where |**_S_**| is the length of the string.
- String consists of lowercase and/or uppercase English alphabets only.

### Sample input:

```
1
abcdef
```

### Sample output:

```
16
```

### Explanation:

The chocolate given in the sample is: **abcdef**.

If you number each piece of the chocolate from 0 to length-1 then **part(i , j)** is the count of vowels in that part of the chocolate which Alice can pick considering only those square pieces whose number is in the **range [i , j]**.

Following are the all possible parts of the cholocate:

| ID | Chocolate  | Part       | Taste |
|----|------------|------------|-------|
| 01 | **a**      | part(0, 0) | 1     |
| 02 | **ab**     | part(0, 1) | 1     |
| 03 | **abc**    | part(0, 2) | 1     |
| 04 | **abcd**   | part(0, 3) | 1     |
| 05 | **abcde**  | part(0, 4) | 2     |
| 06 | **abcdef** | part(0, 5) | 2     |
| 07 | **b**      | part(1, 1) | 0     |
| 08 | **bc**     | part(1, 2) | 0     |
| 09 | **bcd**    | part(1, 3) | 0     |
| 10 | **bcde**   | part(1, 4) | 1     |
| 11 | **bcdef**  | part(1, 5) | 1     |
| 12 | **c**      | part(2, 2) | 0     |
| 13 | **cd**     | part(2, 3) | 0     |
| 14 | **cde**    | part(2, 4) | 1     |
| 15 | **cdef**   | part(2, 5) | 1     |
| 16 | **d**      | part(3, 3) | 0     |
| 17 | **de**     | part(3, 4) | 1     |
| 18 | **def**    | part(3, 5) | 1     |
| 19 | **e**      | part(4, 4) | 1     |
| 20 | **ef**     | part(4, 5) | 1     |
| 21 | **f**      | part(5, 5) | 0     |

> The total sum is therefore 16.

### Proposed Solution:

- The initial solution would be to generate the sets of chocolate parts and count the number of vowels in all of them.
- To do this we can use nested loops, the outer one **i** starting from 0 to (length - 1) and the inner loop **j** starting from i to (length - 1).
- However in this process there is no need to generate chocolate parts, instead just count the number of vowels in the inner loop as shown above.

#### Optimizations:

On a closer observation we find that following number of occurences of: `a: 6, b: 10, c: 12, d: 12, e: 10, f: 6`. On further analysis we find that:

- **a** occurs `6` times in parts starting from **a** itself.
- **b** occurs `5` times in parts starting from **b** itself,
  - `(6 - 1) = 5` time in parts starting from **a**.
- **c** occurs `4` times in parts starting from **c** itself,
  - `(5 - 1) = 4` times in parts starting from **b**,
  - `(6 - 2) = 4` times in parts starting from **a**.
- **d** occurs `3` times in parts starting from **d** itself,
  - `(4 - 1) = 3` times in parts starting from **c**,
  - `(5 - 2) = 3` times in parts starting from **b**,
  - `(6 - 3) = 3` times in parts starting from **a**.
- **e** occurs `2` times in parts starting from **e** itself,
  - `(3 - 1) = 2` times in parts starting from **d**,
  - `(4 - 2) = 2` times in parts starting from **c**,
  - `(5 - 3) = 2` times in parts starting from **b**,
  - `(6 - 4) = 2` times in parts starting from **a**.
- **f** occurs `1` time in parts starting from **f** itself,
  - `(2 - 1) = 1` time in parts starting from **e**,
  - `(3 - 1) = 1` time in parts starting from **d**,
  - `(4 - 2) = 1` time in parts starting from **c**,
  - `(5 - 3) = 1` time in parts starting from **b**,
  - `(6 - 4) = 1` time in parts starting from **a**.

In general we can conclude that for an element at index **i** in a list with **N** elements the element occurs `(N - i) * (i + 1)` times.

Using the above mathematical relation we solve this problem by 

- Storing the indexes of vowels
- Multiplying them  using the relation
- And summing them to get our final answer.

#### Further Optimizations:

- This problem is solved in linear time which is acceptable given the above constrains.
