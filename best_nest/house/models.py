from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from faker import Faker

fake = Faker()


class House(models.Model):
    name = models.CharField(max_length=100)
    passcode = models.CharField(max_length=10)
    start_date = models.DateField(auto_now=True)
    img = models.URLField()
    last_completed_task = models.ForeignKey(
        to="Task", on_delete=models.DO_NOTHING, blank=True, null=True, related_name='houses_last_completed_task')
    last_completer = models.ForeignKey(
        to="User", on_delete=models.DO_NOTHING, blank=True, null=True, related_name='houses_last_completer')
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now=True)
    points = models.IntegerField()
    heating_up = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    last_completed_task = models.ForeignKey(
        to="Task", on_delete=models.DO_NOTHING, blank=True, null=True)
    house = models.ForeignKey(
        to="House", on_delete=models.DO_NOTHING, blank=True, null=True)

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    point_value = models.IntegerField(default=0)
    frequency = models.DurationField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(blank=True, null=True)
    times_completed = models.IntegerField(default=0)
    completed_by = models.ForeignKey(
        to='User', on_delete=models.DO_NOTHING, blank=True, null=True)
    house = models.ForeignKey(
        to="House", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
