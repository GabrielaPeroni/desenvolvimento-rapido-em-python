PYTHON_VERSION = 3.13

.PHONY: setup start

BOLD=\033[1m
RESET=\033[0m

setup:
# --- On Windows, auto-install make if missing
	@if [ "$$(uname 2>/dev/null || echo Windows)" = "Windows" ] && ! command -v make >/dev/null 2>&1; then \
		echo "Installing make via winget..."; \
		winget install GnuWin32.Make -h; \
	fi

	@echo "\n${BOLD}- Confirmando versao do Python${RESET}"
	@python$(PYTHON_VERSION) --version || python --version
	

	@echo "\n${BOLD}- Criando env e instalando dependencias${RESET}"
	@poetry env use python$(PYTHON_VERSION) || poetry env use python
	@poetry install

	@echo "\n\n${BOLD}✅ Setup completo!${RESET}"
	@echo "Para rodar seu servidor Django:"
	@echo "- make start"

start:
	@poetry run python manage.py migrate
	@poetry run python manage.py runserver
