APP_NAME = checkip
PORT = 8000
VENV = .venv

.PHONY: init test run deploy

init:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install fastapi uvicorn requests pytest httpx pytest-cov

test:
	$(VENV)/bin/pytest --cov=$(APP_NAME) --cov-report=term-missing test_checkip.py

test-with-report:
	$(VENV)/bin/pytest --cov=$(APP_NAME) --cov-report html:html_coverage_report test_checkip.py

run:
	$(VENV)/bin/uvicorn $(APP_NAME):app --host 0.0.0.0 --port $(PORT)

deploy:
	$(VENV)/bin/uvicorn $(APP_NAME):app --host 0.0.0.0 --port $(PORT) --workers 4 --reload

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf html_coverage_report
