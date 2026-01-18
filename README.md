# CRM Backoffice (Django)

Проект реализован согласно техническому заданию.

## Функциональность
- Управление услугами
- Управление рекламными кампаниями
- Управление лидами
- Перевод лида в активного клиента
- Заключение контрактов
- Статистика рекламных кампаний
- Авторизация и роли (оператор, маркетолог, менеджер)

## Стек
- Python 3.13
- Django 6
- PostgreSQL / SQLite
- Class Based Views
- PermissionRequiredMixin
- Django ORM (annotate, Count, Sum)

## Роли
- Оператор — лиды
- Маркетолог — услуги и рекламные кампании
- Менеджер — клиенты и контракты
- Все роли — статистика

## Запуск
```bash
python -m venv .venv
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py init_roles
python manage.py runserver
```