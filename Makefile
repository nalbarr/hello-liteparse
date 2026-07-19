help:
	@echo make init-env
	@echo make run
	@echo make run-custom
	@echo make test
	@echo make clean
	@echo ""
	@echo make liteparse-run

init-env:
	cp .env.example .env

run: clean
	uv run python -m hello_liteparse.main

run-custom: clean
	uv run python -m hello_liteparse.custom

test:
	uv run pytest

clean:
	rm -fr ./scratch

liteparse-run:
	mkdir -p ./scratch
	uv run lit parse ./inputs/2408.09869v5.pdf --format markdown --no-ocr -o ./scratch/2408.09869v5.md
