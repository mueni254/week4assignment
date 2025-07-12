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


## TASK2 PRACTICAL
AUTOMATED LOGIN
### Summary: Selenium IDE Login Test with AI Plugins

In this task, we used Selenium IDE to automate login test cases for both valid and invalid user credentials. The tests were recorded using Selenium’s browser plugin, allowing us to simulate real user actions like typing and clicking. Assertions were added to verify correct login and error messages.

To enhance test reliability, we explored AI plugins such as Applitools Eyes, which improve test coverage by using visual validation and dynamic element recognition. These tools help reduce false negatives caused by minor UI changes and improve the resilience of test scripts over time.

Running the test cases showed clear pass/fail outcomes, which were captured through Selenium IDE’s built-in test result panel. This method proves useful for rapidly creating and maintaining functional UI tests without deep coding knowledge.

AI-enhanced tools make Selenium IDE not just a record-and-playback tool, but a smart assistant that increases testing efficiency, scalability, and confidence in software delivery.
