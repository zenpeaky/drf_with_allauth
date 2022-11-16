from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.
GENDER_CHOICE = [
    (1, 'Laki-laki'),
    (2, 'Perempuan')
]
MARITAL_CHOICE = [
    (1, 'Kawin'),
    (2, 'Belum Kawin'),
    (3, 'Cerai')
]

class Employe(models.Model):
    emp_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    emp_phone = models.CharField('Phone', max_length=255)
    emp_gender = models.IntegerField(choices=GENDER_CHOICE, null=True, blank=True)
    emp_marital = models.IntegerField(choices=MARITAL_CHOICE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="profile")

    def __str__(self):
        return self.user.get_username()

@receiver(post_save, sender=User)
def _post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Employe.objects.create(user=instance)
