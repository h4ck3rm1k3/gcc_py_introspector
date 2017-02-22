.headers on
.mode csv 
delete from gcc_tu_parser_sourcefile  ;
.import /home/mdupont/experiments/gcc_py_introspector/files.csv gcc_tu_parser_sourcefile  
delete from gcc_tu_parser_node ;
.import /home/mdupont/experiments/gcc_py_introspector/nodes.csv gcc_tu_parser_nodes
