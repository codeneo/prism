## Categorize Words using Sorted Vowels

### Problem Statement
Given a word categorize it into one of **Good**, **Bad** or **Worst**, using the following rules:

- If there are no vowels in the word, then that word is categorized as **Good**.
- If the word contains all the vowels in alphabetical order, then that word is categorized as **Good**.
- If the word contains the vowels in reverse alphabetical order, then that word is categorized as **Worst**.
- All the other words that do not fall in any of the categories before are categorized as **Bad**.

### Input format:

- The first line of input consists of an integer **_T_** denoting the number of words that need to be classified. Each of the next lines contains a word.

### Output format:

- For each word, output the category to which the word belongs in a new line.

### Constraints:

- The word comprises of lower case English alphabets only.
- 1 &le; **_T_** &le; 10<sup>5</sup>
- 1 &le; |**_S_**| &le; 10<sup>5</sup> where |**_S_**| is the length of the word.

### Sample input:

```
3
discount
weak
goalkeeper
```

### Sample output:

```
Good
Worst
Bad
```

### Explanation:

- For _discount_, the vowels in the word are i,o and u and they occur in the alphabetical order in the word, so this is a **Good** word.
- For _weak_, the vowels in the word are e and a and they occur in reverse order of the alphabetical order in the word, so this is a **Worst** word.
- For _goalkeeper_, the vowels in the word are o, a and e and they occur neither in the reverse order nor in the same order as alphabetical, so this is a **Bad** word.

### Proposed Solution:

Since characters other than vowels do not make a difference let's remove them and store only the vowels in the same order as in the word. The next step is to cast the characters to their ascii value which transforms our problem into determining the order of set of numbers generated.

#### Further Optimizations:

- The vowels extracted could be compressed with run length encoding to save space.
- Another alternative is to use regex to determine the order.