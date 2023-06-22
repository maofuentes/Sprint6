from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class UserManager(BaseUserManager):
    """ Clase para los Administradores de la página. Hereda de la clase BaseUserManager.
     Cuenta con el método de crear usuarios y super usuarios. """ 
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """ Clase para los usuarios comunes de la página. Hereda de AbstractBaseUser y PermissionsMixin."""
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    grupo = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set', related_query_name='customuser')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email