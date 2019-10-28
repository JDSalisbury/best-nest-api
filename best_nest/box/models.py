from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from djongo import models as djodels
from django import forms


class Box(models.Model):
    name = models.CharField(max_length=100)
    passcode = models.CharField(max_length=10)
    start_date = models.DateField(auto_now=True)
    img = models.URLField()
    created = models.DateField(auto_now=True)

    last_completed_task = models.ForeignKey(
        to='Task', on_delete=models.DO_NOTHING, related_name='house_last_completed_task', null=True, blank=True)
    last_completer = models.ForeignKey(
        to='User', on_delete=models.DO_NOTHING, related_name='house_last_completer', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Boxes"

    def __str__(self):
        return self.name


class MetaData(djodels.Model):
    current_points = models.IntegerField(default=0)
    heating_up = models.IntegerField(default=0)
    lifetime_points = models.IntegerField(default=0)
    daily_completed_tasks = models.IntegerField(default=0)
    weekly_completed_tasks = models.IntegerField(default=0)
    monthly_completed_tasks = models.IntegerField(default=0)
    yearly_completed_tasks = models.IntegerField(default=0)

    class Meta:
        abstract = True


class MetaDataForm(forms.ModelForm):
    class Meta:
        model = MetaData
        fields = "__all__"


class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    meta_data = djodels.EmbeddedModelField(
        model_container=MetaData, model_form_class=MetaDataForm)
    last_completed_task = models.ForeignKey(
        to='Task', on_delete=models.DO_NOTHING, related_name='User_last_completed_task', null=True, blank=True)
    completed_tasks = models.ManyToManyField("Task", blank=True)
    box = models.ForeignKey(
        Box, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    value = models.IntegerField(default=0)
    diminishing_returns = models.BooleanField(default=False)
    diminishing_returns_value = models.IntegerField(default=0)
    frequency = models.DurationField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(blank=True, null=True)
    times_completed = models.IntegerField(default=0)
    assigned = models.BooleanField(default=False)

    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    last_completed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='last_tasker')
    box = models.ForeignKey(Box, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
