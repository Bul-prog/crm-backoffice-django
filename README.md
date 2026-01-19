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

# Запуск проекта с нуля
## 1) Клонирование репозитория
```bash
git clone https://github.com/Bul-prog/crm-backoffice-django.git
cd crm_project
python -m venv .venv
```
## 2) Виртуальное окружение и зависимости

### Windows (PowerShell)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux / macOS (bash/zsh)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3) Миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

## 4) Создание суперпользователя (админка)
```bash
python manage.py createsuperuser
```
## 5) Инициализация ролей
```bash
python manage.py init_roles
```
Далее:
- зайдите в http://127.0.0.1:8000/admin/
- создайте пользователей и назначьте им группы (Оператор/Маркетолог/Менеджер)

## 6) Запуск сервера
```bash
python manage.py runserver
```