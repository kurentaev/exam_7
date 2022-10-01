from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    ACTIVE = 'active', 'Active'
    BLOCKED = 'blocked', 'Blocked'


class GuestsList(models.Model):
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='Author')
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='Email')
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Item text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    status = models.CharField(verbose_name='Status', choices=StatusChoices.choices, max_length=100,
                              default=StatusChoices.ACTIVE)

    def __str__(self):
        return f"{self.author} - {self.email} - {self.content}"
