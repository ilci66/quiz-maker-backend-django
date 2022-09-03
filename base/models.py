from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


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


class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        
        other_fields.setdefault('is_teacher', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_teacher') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(self, email, user_name, first_name, password, **other_fields)
        

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'email'] 

    def __str__(self) -> str:
        return self.user_name


class UserScore(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    answered_questions = models.ManyToManyField(Question)
    score = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.score