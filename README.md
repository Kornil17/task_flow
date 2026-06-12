# TaskFlow — API для управления задачами


**TaskFlow** — это бэкенд-сервис для управления задачами в команде, реализованный с применением **Clean Architecture**, **Domain-Driven Design (DDD)** и **Dependency Injection**.

## 🚀 Быстрый старт

### Требования
Смотрите:
- `example.env`
- `uv.lock`
- `pyproject.toml`


### Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/yourusername/taskflow.git
cd taskflow

# Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # или: venv\Scripts\activate (Windows)

# Установите зависимости
uv sync
```

### Запуск

```bash
# development mode с автоперезагрузкой
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# production mode
uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Открытие документации

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🏗️ Архитектура
Смотрите `docs/architecture`

### 📊 Диаграммы

#### диаграмма БД
Смотрите `docs/architecture/db/task_flow.svg`

#### Диаграмма классов
Смотрите `docs/architecture/code/class-diagram.md`

#### Диаграмма последовательности
Смотрите `docs/architecture/code/sequence-diagram.md`

## 🐳 Деплой
Смотрите `docs/deploy`

## 🧪 Тестирование
Смотрите `docs/tests`


## 📄 Лицензия

MIT License. Смотрите [LICENSE](LICENSE) для деталей.
