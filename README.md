# AccessEvent — День 5 (тестирование и документация)

Скопируйте папки в корень проекта accessevent (структура сохраняется).

- tests/ — conftest.py (общая фикстура client), test_models.py (6 тестов), test_api.py (8 тестов)
- docs/ — test_cases.md, bug_reports.md, user_manual.md, admin_manual.md, api.md, assessment.md
- .github/workflows/day5-check.yml — автопроверка

Запуск тестов: `pytest -v`. Нужны requirements.txt, config.py, models.py и routes/ из Дня 3.
Если имена эндпоинтов или поля ответа у вас другие, подправьте тесты под свой код.
