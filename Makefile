PRE_COMMIT = pre-commit
CONFIG_FLAG = --config=.pre-commit-config.yaml

.PHONY: pre-commit-install pre-commit-run pre-commit-uninstall

# Установка хуков в git
pre-commit-install:
	$(PRE_COMMIT) install $(CONFIG_FLAG)

# Запуск проверки всех файлов проекта (тестовый)
pre-commit-run:
	$(PRE_COMMIT) run --all-files $(CONFIG_FLAG)

# Удаление хуков из git
pre-commit-uninstall:
	$(PRE_COMMIT) uninstall
