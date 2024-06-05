run:
	@uvicorn src.main:app --reload

test:
	@poetry run pytest


test-matching:
	@poetry run pytest -s -rx $(K) --pdb store ./tests/
