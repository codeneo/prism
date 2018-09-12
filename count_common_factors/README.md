## Count Common Factors

### Problem Statement

Given two integers **_A_** and **_B_**, find the number of common factors between them.

### Input format:

- First line contains an integer **_A_**.
- Second line contains the integer **_B_**.

### Output format:

Print the required number.

### Constraints:

- 1 &le; **_A_** &le; 10<sup>9</sup>
- 1 &le; **_B_** &le; 10<sup>9</sup>

### Sample input:

```
64 8
```

### Sample output:

```
4
```

### Explanation:

`1, 2, 4 and 8`

### Proposed Solution:

A straight forward approach is to build two sets of factors for each number and then take the intersection of the same.

#### Optimizations:

- Common factors for **A** and **B** are in the range **[ 1, min(A, B) ]**.
- There is no need to store the set of factors, only increment the counter once a common factor is encountered.

#### Further Optimizations:

- This is an excellent candidate for parallel processing since the results are idempotent.
- We split the range in batches and sum the results to get our final answer.

