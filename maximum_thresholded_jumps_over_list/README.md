## Maximum Thresholded Jumps over a List

### Problem Statement

Given an array **_A_** of size **_N_** you can jump from an index **_i_** to another index **_j_** if **_A_**[ **_j_** ] - **_A_**[ **_i_** ] &ge; **_K_**, for **_j_** &gt; **_i_**. Find the length of the longest sequence of jumps that can be possible in the array. You can start at any index.

### Input format:

- First line contains an integer **_K_**.
- Second line contains the integer **_N_**.
- Third line contains N space separated integers, the array **_A_**.

### Output format:

Print the required length.

### Constraints:

- 1 &le; **_K_** &le; 10<sup>6</sup>
- 1 &le; **_N_** &le; 10<sup>6</sup>
- 1 &le; **_A_**[ **_i_** ] &le; 10<sup>6</sup>


### Sample input:

```
2
7
1 3 1 4 5 7 10
```

### Sample output:

```
5
```

### Explanation:

The sequence `1, 3, 5, 7, 10` satisfies the above criteria.

### Proposed Solution:

Our objective here is to maximize the number of hops taken while satisfying the above conditions.

A possible greedy approach would be to start at the left most index and take the shortest hops, hoping to maximize the number of hops. This can be done iteratively for every index in the list and later the the maximum of them can be returned. However this **Greedy** approach is clearly unfit for this type of problems where we need global optimization instead of local.

**Dynamic Programming** is a technique which can solve this problem correctly.

- We start from the last index and calculate the reward for every index in the reverse order.
- For our base case, the last index, the reward would be 0 since there is no way to go forward.
- For the second last index, the reward would be 1 + reward of the last index if their difference is above the threshold as defined above.
- In general we can say that:
  - **R[ i ]** = 1 + **max( R[ j ] )**
  - where **R[ i ]** is the reward for node **i** satisfying the above conditions.

- Using this rule we can find the rewards for all the nodes and return the maximum reward.
- Our answer would be the maximum reward + 1, since we need the longest sequence and therefore it is necessary to add the starting node to it.


#### Optimizations:

- If the **max(A) - min(A)** is less than **K**, then there exists no sequence because no jumps are possible.
- If **max( A[ j ] - A[ i ] )** for every **j > i** is less than **K**, then there exists no sequence because no jumps are possible.

#### Further Optimizations:

- In the future I would probably replace the native lists with **numpy** arrays and measure the performance gain.
