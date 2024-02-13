import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Notes(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    userIdentificationNumber = models.ForeignKey("User", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        db_table = "notes"
        ordering = ["-updatedAt"]


class User(AbstractBaseUser):
    userIdentificationNumber = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password"]

    class Meta:
        db_table = "users"


class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    userIdentificationNumber = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"
