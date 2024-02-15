import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    userIdentificationNumber = models.UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4,
    )
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(
        max_length=255,
        unique=True,
        default="your_default@example.com",
    )
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    userIdentificationNumber = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"


class Notes(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    userIdentificationNumber = models.ForeignKey("User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "notes"
        ordering = ["-updatedAt"]
