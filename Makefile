all:
	@echo 'see README.md'

run:
	poetry run python pypong/game.py

.PHONY: all run
