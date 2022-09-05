deps:
	pip3 install -r requirements.txt

test:
	nose2 -v --with-coverage --coverage-report html --coverage-report term --coverage-report xml

code_formatter:
	black database
	black tests

mutation:
	mutmut run --disable-mutation-types=decorator
