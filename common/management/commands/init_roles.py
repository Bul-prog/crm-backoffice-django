from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from ads.models import Ad
from leads.models import Lead
from customers.models import Customer
from contracts.models import Contract


class Command(BaseCommand):
    help = 'Create default roles (groups) and assign permissions'

    def handle(self, *args, **options):
        roles = {
            'Оператор': [
                ('leads', 'lead', ['add', 'change', 'view', 'delete']),
                ('ads', 'ad', ['view']),
            ],
            'Маркетолог': [
                ('products', 'product', ['add', 'change', 'view', 'delete']),
                ('ads', 'ad', ['add', 'change', 'view', 'delete']),
            ],
            'Менеджер': [
                ('contracts', 'contract', ['add', 'change', 'view']),
                ('customers', 'customer', ['add', 'change', 'view', 'delete']),
                ('leads', 'lead', ['view']),
                ('ads', 'ad', ['view']),
            ],
        }

        # создаём/обновляем группы
        for group_name, perms in roles.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            group.permissions.clear()

            for app_label, model_name, actions in perms:
                ct = ContentType.objects.get(app_label=app_label, model=model_name)
                for action in actions:
                    codename = f'{action}_{model_name}'
                    perm = Permission.objects.get(content_type=ct, codename=codename)
                    group.permissions.add(perm)

            self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" настроена'))

        self.stdout.write(self.style.SUCCESS('Готово. Теперь назначь пользователям группы в админке.'))
