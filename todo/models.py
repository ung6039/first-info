from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=200,null=False,
        help_text="할일을 채워주세요!")
        #help_text :: 프롬프트
        # 상속 두 클래스 사이의 관계
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task