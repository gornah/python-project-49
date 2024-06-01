install:
	poetry install

brain-games: # Запуск проекта(приветствие)
	poetry run brain-games

brain-even: # Четное нечетное
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games
