from django.db import models

class Task(models.Model):
    fo_task_name = models.CharField(max_length=100, verbose_name='Описание задачи')
