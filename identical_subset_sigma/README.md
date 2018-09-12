## Identical Sigma Subsets

### Problem Statement

You are given an array consisting of **_N_** integers. You need to determine whether any permutation of given array exist such that the sum of all subarrays of length **_K_** are equal.

### Input format:

- The first line consist of **_T_** denoting the number of testcases.
- The first line of each testcase consists of two space separated integers **_N_** and **_K_**.
- The second line of each tescase consists of **_N_** space separated integers denoting array elements.

### Output format:

Print "**YES**" or "**NO**" for each testcase in a new line.

### Constraints:

- 1 &le; **_T_** &le; 10
- 1 &le; **_K_** &le; **_N_** &le; 10<sup>6</sup>
- 1 &le; **_A<sub>i</sub>_** &le; 10<sup>5</sup>
- **_N_** is divisible by **_K_** _i.e._ **_N_** `mod` **_K_** = 0

### Sample input:

```
2
4 2
3 5 5 2
5 5
1 2 3 4 5
```

### Sample output:

```
NO
YES
```

### Explanation:

- All the subarrays of length 2 have different summations, therefore the answer is **NO**.
- There exists only 1 subarray of length 5 which is the array itself and therefore the answer is **YES**.

### Proposed Solution:

The initial solution would be to find all combinations of length **_K_** and sum each of them. Henceforth find unique  elements in the same and determine if that is equal to 1 or not.

#### Optimizations:

- There is no need to sum all the combinations.
- Sum the first combination to get **_X_**.
- We can stop early as soon as we find a combination with sum not equal to **_X_**.

#### Further Optimizations:

- Iterators in Python save us the space and time required to find all combinations.
- Combination are found in a lazy manner when needed.
- Hence in a scenario with 100 combinations with 4th combination yielding a different sum than the first 3, 96 combinations are never evaluated because of **iterators** and **early stopping**.

