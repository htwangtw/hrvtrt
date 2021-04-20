tests:
	poetry run pytest  --ignore=hrvtrt/tests/utils.py --cov hrvtrt/ --cov-report term-missing
	poetry run black .