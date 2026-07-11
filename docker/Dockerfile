# Скачиваем базовый образ облегченный без (документации, комплияторов, лишних библиотек, man пакетов)
FROM python:3.13.13-slim-bookworm as base

# Переменные окружения
# PYTHONFAULTHANDLER: Добавляет стек вызовов, если пайтон неожиданно падает
# PYTHONUNBUFFERED: Убирает буферизацию логов, чтобы они сразу попадали в docker файл
# PYTHONHASHSEED: При каждом запуске будет разные хэш, для защиты от коллизий хэша
# PYTHONDONTWRITEBYTECODE: Не кэширует пайтон код, то есть убирает создание __pycache__/*.pyc файлов (стандарт при запуске в контейнерах)
# UV_COMPILE_BYTECODE: Комплияция байт кода UV при первом запуске, чтобы каждый раз не компилировать при импорте файлов
# UV_VERSION: Версия UV
# UV_LINK_MODE: Копирует ссылки на пакеты UV
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_VERSION="0.11.17" \
    UV_LINK_MODE=copy

# Этап сборки
FROM base as builder
# Установка UV утилиты для управления пакетами
RUN pip install "uv==${UV_VERSION}"
# Устанавливаем рабочую директорию
WORKDIR /src
# Копируем настройки приложения и скомпилированный пакеты
COPY pyproject.toml uv.lock ./
# Устанавливаем зависимости
RUN uv sync --frozen --no-install-project

# RUNTIME сборка (финальный образ)
FROM base
# Создаем пользователя для запуска контейнера из под него
RUN groupadd -r task_flow && useradd -r -g task_flow task_flow
# Создаем директорию для упаковки приложения
RUN mkdir -p /src && chown task_flow:task_flow /src
# Устанавливаем рабочую директорию
WORKDIR /src
# Копируем виртуальное окружение
COPY --chown=task_flow:task_flow --from=builder /src/.venv /src/.venv
# Копируем файлы приложения
COPY --chown=task_flow:task_flow . /src

# Добавляем перменную для пути до виртуального окружения
ENV VIRTUAL_ENV=/src/.venv
# Добавляем вирутальное окружение в PATH.
ENV PATH="/src/.venv/bin:$PATH"
# Запускаем приложение от созданного нами пользователя.
USER task_flow

# Запуск приложения
CMD ["python", "main.py"]