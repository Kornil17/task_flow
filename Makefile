.PHONY: pre-commit-install pre-commit-run pre-commit-uninstall generate-api-routers-models

# Переменные для pre-commit команд
PRE_COMMIT = pre-commit
CONFIG_FLAG = --config=.pre-commit-config.yaml

# Переменные для openapi генерации
OPENAPI_FILE := docs/architecture/api/openapi.yaml
OUTPUT_DIR := src/presentation
MODEL_FILE := dtos/models.py

# Установка хуков в git
pre-commit-install:
	$(PRE_COMMIT) install $(CONFIG_FLAG)

# Запуск проверки всех файлов проекта (тестовый)
pre-commit-run:
	$(PRE_COMMIT) run --all-files $(CONFIG_FLAG)

# Удаление хуков из git
pre-commit-uninstall:
	$(PRE_COMMIT) uninstall

# Генерация API моделей из openapi схемы
generate-api-models:
	fastapi-codegen --input $(OPENAPI_FILE) \
		--output $(OUTPUT_DIR) \
		--output-model-type pydantic_v2.BaseModel \
		--model-file $(MODEL_FILE) \
		--python-version 3.13 \
		--use-annotated \
		--reuse-model \
		--enable-faux-immutability

	@if [ -f $(OUTPUT_DIR)/main.py ]; then \
		rm $(OUTPUT_DIR)/main.py; \
		echo "Removed routers in main.py"; \
	else \
		echo "Warning: main.py not found, skipping routers remove"; \
	fi
