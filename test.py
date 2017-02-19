#!/usr/bin/python3
#PYTHONPATH=~/experiments/gcc_py_introspector/ python3
#import memory_profiler
import gcc.tree.reader
#tests/identifier.tu
import sys
import gcc.tree.attributes
import gcc.tree.nodes

gcc.tree.reader.main()
gcc.tree.attributes.report()
gcc.tree.nodes.report()

