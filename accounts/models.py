from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class PharmacyUserManager(BaseUserManager):
    def create_user(self, name=None, email=None, password=None):
        """
        Creates and saves a User with the given name, email and password.
        """
        if not name:
        	raise ValueError('Ce champ doit contenir le name de votre pharmacie')
        if not email:
            raise ValueError('Vous devez fournir une adresse email valide.')

        user = self.model(
        	name = name,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email,  password):
        """
        Creates and saves a superuser with the given username, email and password.
        """

        user = self.create_user(
			name=name,
			email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class PharmacyUser(AbstractBaseUser):
	name = models.CharField(
	    max_length=255,
	    unique=True,
	)
	email = models.EmailField(
	    verbose_name='email address',
	    max_length=255,
	    unique=True,
	)
	owner_first_name = models.CharField(
			max_length=120,
			)
	owner_last_name = models.CharField(
			max_length=120,
			)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = PharmacyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
	    # The user is identified by their email address
	    return "%s %s" %(self.owner_first_name, self.owner_last_name)

	def get_short_name(self):
	    # The user is identified by their email address
	    return self.owner_first_name

	def __str__(self):
	    return self.name

	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    return True

	def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_admin
