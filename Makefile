testsave:
	python3 reader.py tests/save_expr.tu

testcons:
	python3 reader.py tests/constructor.tu
	python3 load_pickle.py

lsof:
	python3 runtest.py ../lsof

runall:
	python3 runtest.py ./tests

testfield:
	python3 reader.py tests/bitfield.tu
	python3 load_pickle.py

testload:
	python3 load_pickle.py

testlsof:
	python3 reader.py ../lsof/main.c.001t.tu
	python3 load_pickle.py

testid:
	python3 reader.py tests/test_id.tu

testnote:
	python3 reader.py tests/test_note.tu

testfunc2:
	python3 reader.py tests/funcdecl2.tu

testfunc:
	python3 reader.py tests/funcdecl1.tu

testchain:
	python3 reader.py tests/test_chain.tu

testempty:
	python3 reader.py tests/empty.tu

recurse_all :
	python3 query_function_example_python_all.py


translate :
	python3 translate_to_python.py

pairs :
	python3 pairs.py

quine:
	python3 quine.py



recurse:
	python3 query_function_example_python.py

recurse3:
	python3 query_function_example_direct.py

# query the database and produce the data/body2.py
recurse2:
	python3 query_function_example.py

types:
	python3 query_types.py

query :
	python3 queryviz.py > /var/www/html/sparql/introspector/graphs/example.dot
	dot /var/www/html/sparql/introspector/graphs/example.dot -Tpng -o /var/www/html/sparql/introspector/graphs/example.png

# read in the TU create the data file in produce rdf files, after this you need to  load them into the database and then run some queries
testbash1:
	python3 reader.py /home/jamesmikedupont/bash/build/test1.tu

testbash:
	python3 reader.py /home/jamesmikedupont/bash/build/eval.c.001t.tu
	cp output.xml b99f78e7d415e80d1590/
	cp output.xml /tmp/
	sudo /etc/init.d/tomcat8 stop
	rm /var/lib/tomcat8/data/*
	sudo /etc/init.d/tomcat8 start

qual:
	python3 reader.py tests/test_one_qual.tu x

op01:
	python3 reader.py tests/op_0_1.tu  d

op0:
	python3 reader.py tests/op_0.tu

tuaddr :
	python3 reader.py tests/addr_expr.tu

tu7 :
	python3 reader.py tests/report1.tu

tu8 :
	python3 reader.py tests/testmissing4.tu

tu6 :
	python3 reader.py tests/testmissing4.tu

tu5 :
	python3 reader.py tests/testmissing3.tu

tu4 :
	python3 reader.py tests/testmissing2.tu

tu3 :
	python3 reader.py tests/testmissing.tu

tu1 :
	python3 reader.py tests/testqual.tu


tu :
	python3 reader.py tests/test.tu

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
	python3 reader.py tests/test100.tu

test102:
	python3 reader.py tests/test102.tu
