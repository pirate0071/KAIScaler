# Makefile

.PHONY: install test lint run docker-build docker-run clean

install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	flake8 .

run:
	python kaiscaler_operator.py

docker-build:
	docker build -t myrepo/kaiscaler:latest .

docker-run:
	docker run -p 5000:5000 myrepo/kaiscaler:latest

clean:
	rm -rf __pycache__ *.pyc *.pyo .pytest_cache