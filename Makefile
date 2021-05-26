
tests:
	poetry run pytest  --ignore=hrvtrt/tests/utils.py --cov hrvtrt/ --cov-report term-missing -vs
	poetry run black .