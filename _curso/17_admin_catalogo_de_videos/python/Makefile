deps:
	pip3 install -r requirements.txt
	pip3 install -r requirements.dev.txt

test:
	nose2 -v --with-coverage --coverage-report html --coverage-report term --coverage-report xml

code_formatter:
	black src

mutation:
	mutmut run --disable-mutation-types=decorator
