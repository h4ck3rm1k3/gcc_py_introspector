gcc_py_introspector
===================

a new stab at .tu parsing in my new favorite language, python


usage
=====

    g++ --verbose -O0 -fdump-tree-all  test.c

convert the tu to python:

    python reader.py file.tu > test_graph.py

now you can split up the output:

    PYTHONPATH=. python dfs.py  testgraph

for now, need to add in an init

    touch cache/__init__.py

And then process one of the files :

    PYTHONPATH=. python ../read_sources.py cache._00001368
