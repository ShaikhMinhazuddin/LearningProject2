from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomerForm1(models.Model):
    imag = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,default = None)
    dim1 = models.IntegerField()
    dim2 = models.IntegerField()
    typ = models.CharField( max_length=20, default='mini-truck')
    loadWgt = models.IntegerField()
    tadd = models.CharField(max_length=50)
    fadd = models.CharField(max_length=50)
    ddate = models.DateField()
    budg = models.IntegerField()
    desc = models.CharField(max_length=150)
    
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username,role,password = None):
        if not email:
            raise ValueError("Email Required")
        if not username:
            raise ValueError("Username Required")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            role = role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,role,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            role= role
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField(verbose_name='date Joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField( max_length=10, default='Customer')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','role']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj= None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True