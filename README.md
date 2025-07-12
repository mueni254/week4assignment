# week4assignment
## TASK 1 PRACTICAL
Analysis:

The manual version uses `sorted()` which is non-destructive and straightforward.
The AI version uses `list.sort()` with `dict.get()`, which is more fault-tolerant but modifies the list in-place.

Both achieve the same result with similar time complexity (O(n log n)). 
However, the manual version keeps the original data intact, which is safer in cases where the original order must be preserved.

The AI-suggested code may be more efficient for large in-place operations,
but the manual version is better for immutability and readability.

In summary, both are effective, but context determines which is preferable.
"""