from django.db import models

# Create your models here.

class Try_todo(models.Model):
    todo = models.CharField(max_length=200,null=False,
     help_text="할일을 채워주세요!"
    )
    done_false = models.BooleanField(default=False)

    def __str__(self):
        return self.todo