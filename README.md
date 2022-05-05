### Alraedah Assessment

We can check if we traversed all elements in an array without actually keeping a visited array. By calculating the traveling costs (or better traveling distance), we can compare that against the sum of the array. (_crude idea, didn't test._)

Another strategy is to keep an array with all the visited elements and compare them against the original array.

Or we can represent it as a graph and use DFS.

1. We can keep a list of visited nodes and compare that with the length of the original array.
2. Or generate an adjacency matrix, get row sum and check for the vertex degree, where we can check if `index[0] >= 2` as it's a directed graph, where we can't have more than 2 edges unless we visit the first element twice. Also need to keep a `visited` array. (But this an also untested and a very crude idea that may result in a plethora of checks and tests, but it's faster, as edges lookup can scale up dramatically).

I went with an adjacency list generation strategy, and using DFS to count visited nodes, and compare that with the original array.


#### Known Limitations
1. Recursive function limit. I think we need to think about that, and when to switch 
to an iterative approach, especially when the recursion stack default limit is > 1000. Of course, the iterative approach is way more efficient, but as this is a coding assessment, I went with clarity here.
2. JSON iterative and lazy-evaluation can give us a huge performance boost, but due to 
time constraints, I haven't implemented a solution yet.
3. JSON validation needs some work, like checking if the incoming JSON follows the schema defined in the assessment. We can do that using `jsonschema` library.
4. Some `WebSocket` or `PubSub` implementations is the way to go when it's coming to receiving results back, as the current implementation is a race between the task and the connection timing out. 
5. Unit tests are unfortunately not yet done due to time constraints.
6. We return the results in the console 🤨. Sorry, I wanted to implement part two first.

##### Ahmed Aloufi.
