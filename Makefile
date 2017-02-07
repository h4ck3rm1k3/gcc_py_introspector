testcons:
	python reader.py tests/constructor.tu d
	python load_pickle.py

lsof:
	python runtest.py ../lsof

runall:
	python runtest.py ./tests

testfield:
	python reader.py tests/bitfield.tu 
	python load_pickle.py

testload:
	python load_pickle.py

testlsof:
	python reader.py ../lsof/main.c.001t.tu
	python load_pickle.py
	# ../lsof/arg.c.001t.tu
	# ../lsof/dstore.c.001t.tu
	# ../lsof/proc.c.001t.tu
	# ../lsof/dfile.c.001t.tu
	# ../lsof/empty.c.001t.tu
	# ../lsof/store.c.001t.tu
	# ../lsof/dmnt.c.001t.tu
	# ../lsof/main.c.001t.tu
	# ../lsof/usage.c.001t.tu
	# ../lsof/dnode.c.001t.tu
	# ../lsof/misc.c.001t.tu
	# ../lsof/util.c.001t.tu
	# ../lsof/dproc.c.001t.tu
	# ../lsof/node.c.001t.tu
	# ../lsof/dsock.c.001t.tu
	# ../lsof/print.c.001t.tu


testid:
	python reader.py tests/test_id.tu 	

testnote:
	python reader.py tests/test_note.tu

testfunc2:
	python reader.py tests/funcdecl2.tu

testfunc:
	python reader.py tests/funcdecl1.tu

testchain:
	python reader.py tests/test_chain.tu

testempty:
	python reader.py tests/empty.tu

recurse_all :
	python query_function_example_python_all.py


translate :
	python translate_to_python.py

pairs :
	python pairs.py

quine:
	python quine.py



recurse:
	python query_function_example_python.py

recurse3:
	python query_function_example_direct.py

# query the database and produce the data/body2.py
recurse2:
	python query_function_example.py

types:
	python query_types.py

query :
	python queryviz.py > /var/www/html/sparql/introspector/graphs/example.dot
	dot /var/www/html/sparql/introspector/graphs/example.dot -Tpng -o /var/www/html/sparql/introspector/graphs/example.png

# read in the TU create the data file in produce rdf files, after this you need to  load them into the database and then run some queries
testbash1:
	python reader.py /home/jamesmikedupont/bash/build/test1.tu

testbash:
	python reader.py /home/jamesmikedupont/bash/build/eval.c.001t.tu
	cp output.xml b99f78e7d415e80d1590/
	cp output.xml /tmp/
	sudo /etc/init.d/tomcat8 stop
	rm /var/lib/tomcat8/data/*
	sudo /etc/init.d/tomcat8 start

qual:
	python reader.py tests/test_one_qual.tu x

op01:
	python reader.py tests/op_0_1.tu  d

op0:
	python reader.py tests/op_0.tu

tuaddr :
	python reader.py tests/addr_expr.tu

tu7 :
	python reader.py tests/report1.tu

tu8 :
	python reader.py tests/testmissing4.tu

tu6 :
	python reader.py tests/testmissing4.tu

tu5 :
	python reader.py tests/testmissing3.tu

tu4 :
	python reader.py tests/testmissing2.tu

tu3 :
	python reader.py tests/testmissing.tu

tu1 :
	python reader.py tests/testqual.tu 


tu :
	python reader.py tests/test.tu 

FILES=tu.py tuparser.py tuast.py reader.py

auto2:
	~/.local/bin/autopep8 -v -a -a -a -a  -i $(FILES)

auto :
	~/.local/bin/pep8ify -v -w $(FILES)

fixlines:
	~/.local/bin/autopep8 -v --select=E501 --max-line-length=78 -i -a -a -a -a $(FILES)

lint :
	~/.local/bin/pyflakes $(FILES)
	~/.local/bin/pylint --rcfile=.pylintrc  $(FILES)

test100:
	python reader.py tests/test100.tu

test102:
	python reader.py tests/test102.tu
