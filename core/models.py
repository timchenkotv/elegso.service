from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        # чтобы не требовался username
        extra_fields.setdefault('username', None)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()
    # username делаем необязательным (мы логинимся по email)
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)
    email = models.EmailField(unique=True)

    # ВНИМАНИЕ: связь с Контрагентом добавим отдельной миграцией,
    # когда создадим справочник directory.Counterparty.
    # counterparty = models.OneToOneField('directory.Counterparty', ...)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # при createsuperuser не будет спрашивать username

    def __str__(self):
        return self.email
