install:
		poetry install

brain-games:
		poetry run brain-games

brain-even:
		poetry run brain-even

brain-calc:
		poetry run brain-calc

brain-gcd:
		poetry run brain-gcd

brain-progression:
		poetry run brain-progression

brain-prime:
		poetry run brain-prime

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

line:
		poetry run flake8 brain_games

line-logic:
		poetry run flake8 games
