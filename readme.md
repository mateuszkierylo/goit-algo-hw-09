## Performance Comparison

### Execution Time

We compared the execution times of both algorithms for different amounts of change. The results are summarized below:

| Amount | Greedy Time (s)         | DP Time (s)            |
|--------|-------------------------|------------------------|
| 113    | 2.1457672119140625e-06  | 5.2928924560546875e-05 |
| 1000   | 0.0                     | 0.0009081363677978516  |
| 10000  | 0.0                     | 0.00527191162109375    |
| 100000 | 1.9073486328125e-06     | 0.05571722984313965    |

### Analysis

- **Greedy Algorithm**: This algorithm is very fast and efficient for small to moderately large sums. However, it does not always guarantee the minimum number of coins, depending on the coin denominations.
- **Dynamic Programming Algorithm**: This algorithm guarantees the minimum number of coins but has higher computational complexity, making it slower for very large sums compared to the greedy algorithm.

### Conclusion

For smaller amounts, the difference in performance between the two algorithms is negligible. However, for larger sums, the greedy algorithm performs significantly faster, although it may not always provide the optimal solution. The dynamic programming algorithm, while slower, guarantees the optimal solution in terms of the minimum number of coins.
