from django.db import models
from ads.models import Ad


class Lead(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)

    phone = models.CharField('Телефон', max_length=50)
    email = models.EmailField('Email')

    ad = models.ForeignKey(Ad, on_delete=models.SET_NULL, null=True, related_name='leads')
    created_at = models.DateTimeField(auto_now_add=True)

    # опционально, чтобы пережить переход (можно потом убрать)
    full_name = models.CharField('ФИО (legacy)', max_length=255, blank=True, default='')

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'
