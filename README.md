# AccessEvent — инклюзивная платформа мероприятий

Веб-платформа для организации мероприятий, доступная людям с нарушениями слуха: визуальные уведомления вместо звуковых, текстовый чат, цветовая индикация статусов.

## Стек технологий

- Backend: Python 3.11, Flask
- База данных: PostgreSQL 16 / SQLite (для тестов)
- Frontend: HTML5, CSS3, JavaScript, Jinja2
- Тестирование: pytest
- CI/CD: GitHub Actions
- Контейнеризация: Docker, docker compose, GHCR

## Как запустить

### Вариант 1. Docker (рекомендуется)

docker compose up

Открыть: http://127.0.0.1:5000

### Вариант 2. Локально

1. Скопировать .env.example в .env и заполнить SECRET_KEY и DATABASE_URL
2. pip install -r requirements.txt
3. python app.py

## Тесты

python -m pytest -v

## Структура проекта

- app.py — точка входа, маршруты
- models.py — SQLAlchemy-модели
- config.py — конфигурация
- routes/ — Blueprint-маршруты API
- utils/ — JWT, хеширование, доступность
- templates/ — Jinja2-шаблоны
- static/css, static/js — стили и скрипты
- tests/ — тесты pytest
- docs/ — вся документация
- Dockerfile
- docker-compose.yml

## Документация

- docs/analysis.md — анализ предметной области
- docs/requirements.md — требования и User Stories
- docs/stakeholders.md — стейкхолдеры
- docs/tz.md — техническое задание
- docs/architecture.md — архитектура системы
- docs/schema.sql — схема базы данных
- docs/security.md — подсистема безопасности
- docs/test_cases.md — тест-кейсы
- docs/bug_reports.md — баг-репорты
- docs/user_manual.md — руководство пользователя
- docs/admin_manual.md — руководство администратора
- docs/api.md — описание API
- docs/assessment.md — оценка ИС и направления развития
- docs/speech.md — тезисы выступления

## Docker-образ

Образ публикуется автоматически при push:

ghcr.io/Flux-AS/accessevent:latest

## Автор

Учебная практика ПМ.05, 3 семестр.