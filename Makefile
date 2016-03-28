types:
	python query_types.py

query :
	python queryviz.py > /var/www/html/sparql/introspector/graphs/example.dot
	dot /var/www/html/sparql/introspector/graphs/example.dot -Tpng -o /var/www/html/sparql/introspector/graphs/example.png

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
	python reader.py tests/op_0_1.tu 

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

dummy :
	python reader.py tests/test4.tu 

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
