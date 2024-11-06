from datetime import datetime

from django.db import models

from app_users.models import UserModel


class ContrackType(models.TextChoices):
    borrowed = 'borrowed', 'borrowed'
    lent = 'lent', 'lent'

class ContrackStatus(models.TextChoices):
    active = 'active', 'active'
    deleted = 'deleted', 'deleted'
    waiting = 'waiting', 'waiting'
    done = 'done', 'done'

class ContrackMoney(models.TextChoices):
    usd = 'usd', 'usd'
    uz = 'uz', 'uz'
    eur = 'eur', 'eur'
    rub = 'rub', 'rub'


class ContrackModel(models.Model):
    type = models.CharField(choices=ContrackType.choices, max_length=50)
    status = models.CharField(choices=ContrackStatus.choices, max_length=50)
    currence = models.CharField(choices=ContrackMoney.choices, max_length=50)

    who = models.ForeignKey(UserModel,  on_delete=models.PROTECT, related_name='contract')
    whom = models.CharField(max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    notes = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    back_money = models.DateTimeField( null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Contrack'
        verbose_name_plural = 'Contracks'


