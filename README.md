### Alraedah Assessment


We can check if we traversed all elements in an array without actually keeping a visited array.
By calculating the traveling costs (or better traveling distance), we can compare that against the sum of the array. (_crude idea, didn't test._)

Another strategy, is keep an array with with all the visited elements and and compare them against the original array.

Or we can represnt it as graph and use DFS.

1. We can keep a list of visited nodes and compare that with the length of the original array.
2. Or generate an adjacency matrix, get row sum and check for the vertex degree, where we can check if `index[0] >= 2]` as it's a directed graph, where we can't have more than 2 edges unless we visit the first element twice. It goes without saying that also need to keep a `visited` array.
(But this an also untested and a very crude idea that may result in a plethora of checks and tests, but it's faster, as edges lookup can scaless).

I went with an adjacency _list_ generation strategy, and using DFS to count visited nodes, and compare that with the original array.

#### Known Limitations
1. Recursive function limit. I think we need to think about that, and when to switch 
to an iterative approach, especially when the recursion stack default limit is > 1000.
2. JSON iterative and lazy-evaluation can give us a huge performance boost, but due to 
time constraints, I haven't implemented a solution yet.
3. JSON validation needs some work, like checking if the incoming JSON follows the schema defined in the assessment.


##### Ahmed Aloufi.