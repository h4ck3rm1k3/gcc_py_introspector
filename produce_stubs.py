"""
Produce stubs :

1. start with an identifier
2. find the nodes that use it
3. find the nodes referenced by those
4. put them into a context


For each node, find all the nodes used by it.
For each node, find all the users of that node.
For each node, find all the users of that node, and find all the nodes that are used by it.

"""

from cache._00013930 import data
print data
