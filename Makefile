.PHONY: pre-commit-install pre-commit-run pre-commit-uninstall generate-api-routers-models migrate-init migrate-new migrate-up migrate-down migrate-status

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

# Создать таблицу миграций и применить все новые
# make migrate-init DATABASE_URL="postgresql+psycopg://name:password@host:port/name"
migrate-init:
	yoyo init --database "$(DATABASE_URL)" src/infrastructure/persistence/migrations

# Создать новую миграцию
# make migrate-new NAME=create_users
migrate-new:
	yoyo new migrations -m "$(NAME)"

# Применить все миграции
migrate-up:
	yoyo apply

# Откатить последнюю миграцию
migrate-down:
	yoyo rollback -r 1

# Показать статус миграций
migrate-status:
	yoyo list
