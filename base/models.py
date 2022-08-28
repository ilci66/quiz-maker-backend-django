from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return str(self.name)


class Question(models.Model):
    text = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.text)


class Answer(models.Model):
    text = models.CharField(max_length=255)
    right = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.text)