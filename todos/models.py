from django.db import models

# Create your models here.

class Todos(models.Model):
    task = models.CharField(max_length=200,null=False,
     help_text="할일을 채워주세요!"
    )
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task