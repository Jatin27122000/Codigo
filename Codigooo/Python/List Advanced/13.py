'''Write a Python a function to implement a LRU cache.
From Wikipedia -
Least recently used (LRU)
Discards the least recently used items first. This algorithm requires keeping track of what was used when, 
which is expensive if one wants to make sure the algorithm always discards the least recently used item. 
General implementations of this technique require keeping "age bits" for cache-lines and track the "Least 
Recently Used" cache-line based on age-bits. In such an implementation, every time a cache-line is used, 
the age of all other cache-lines changes. LRU is actually a family of caching algorithms with members 
including 2Q by Theodore Johnson and Dennis Shasha, and LRU/K by Pat O'Neil, Betty O'Neil and Gerhard Weikum.'''

