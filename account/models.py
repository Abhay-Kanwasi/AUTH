from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, name, email, tc, password=None, password2=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, tc, password=None):
        user = self.create_user(
            name=name,
            email=self.normalize_email(email),
            password=password,
            tc=tc
        )
        user.is_admin = True
        user.save(using=self._db)


# Custom User Model
class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True
    )
    tc = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # object of user manager
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        """Does the user have a specific permission?"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Does the user to view the app `app_label`?"""
        return True

    @property
    def is_staff(self):
        return self.is_admin
