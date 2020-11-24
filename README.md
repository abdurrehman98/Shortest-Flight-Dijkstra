# Shortest-Flight-Dijkstra
Created a shortest flight mapper using Dijkstra's algorithm. Used basic US airports &amp; randomized flight durations from one Airport to the next.


After running the algorithm, the input must be rerun to initialize the distance's we have set up and/or change. The algorithm is optimized to work with large amounts of data and heavily interconnected nodes, so the larger the relationships between multiple airports, the better for the algorithm. One flaw that exists is that the algorithm does not fully address when two locations do not have any possible ways of being connected. I would like to implement a sort of 'getting as close as we can' algorithm to at least provide the user with some benefit. For e.g if SFO and NYC aren't connected, then perhaps get the user to as close to NYC as possible. A form of 'next best alternative' although that may be crude.
