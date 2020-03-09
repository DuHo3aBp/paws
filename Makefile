setup:
	python3.8 -m venv ./.pragai

install:
	pip install -r requirements.txt

test:
	PYTHONPATH=. && pytest -vv --cov=paws tests/*.py
	PYTHONPATH=. && py.test --nbval-lax notebooks/*.ipynb

lint:
	pylint --disable=R,C paws

lint-warnings:
	pylint --disable=R,C *.py

all:install lint test