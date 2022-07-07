from django.db import models
from users.models import CustomUser

RATING = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Pub(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=250)
    rate = models.PositiveIntegerField(choices=RATING, blank=False, default="-")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bar")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=250)
    bar = models.ForeignKey(Pub, on_delete=models.CASCADE, related_name="drinks")
    rate = models.PositiveIntegerField(choices=RATING, blank=False, default="-")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='drinks')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.name