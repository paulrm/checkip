APP_NAME = checkip
PORT = 8000
VENV = .venv

.PHONY: init test run deploy

init:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install fastapi uvicorn requests pytest

test:
	$(VENV)/bin/pytest test_checkip.py

run:
	$(VENV)/bin/uvicorn $(APP_NAME):app --host 0.0.0.0 --port $(PORT)

deploy:
	$(VENV)/bin/uvicorn $(APP_NAME):app --host 0.0.0.0 --port $(PORT) --workers 4 --reload

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache

