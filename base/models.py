# Tunapakia classes muhimu kutoka Django na Cloudinary
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from cloudinary.models import CloudinaryField


# Custom manager ya kuhandle uundaji wa watumiaji na superusers
class UserManager(BaseUserManager):
    # Method ya kuunda mtumiaji wa kawaida
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')  # Lazima email iwepo
        email = self.normalize_email(email)  # Normalize email (iwe standardized)
        user = self.model(email=email, **extra_fields)  # Tengeneza instance ya user
        user.set_password(password)  # Weka password kwa usalama
        user.save(using=self._db)  # Save kwenye database
        return user

    # Method ya kuunda superuser (admin)
    def create_superuser(self, email, password=None, **extra_fields):
        # Hakikisha superuser ana sifa hizi mbili
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Tunatengeneza Custom User model kwa kurithi kutoka AbstractUser
class User(AbstractUser):
    # Sehemu za ziada kwenye user
    name = models.CharField(max_length=200, null=True, help_text="Enter your name", verbose_name="Name")
    email = models.EmailField(unique=True, null=True, help_text="Enter your email", verbose_name="Email")
    bio = models.TextField(null=True, help_text="A brief description about yourself", verbose_name="Biography")
    
    # Picha ya mtumiaji (avatar) inahifadhiwa kupitia Cloudinary
    avatar = CloudinaryField('avatar')

    # Tunatumia email badala ya username kama field kuu ya login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Hatuhitaji fields nyingine kama default

    # Tunatumia manager wetu tuliyotengeneza
    objects = UserManager()

    def __str__(self):
        return self.email  # Hii itakua ni representation ya mtumiaji


# Model ya Topic inawakilisha mada au group la mazungumzo
class Topic(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the topic name", verbose_name="Topic")

    def __str__(self):
        return self.name


# Model ya Room inawakilisha chumba cha majadiliano
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="Select the host of the room", verbose_name="Host")
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, help_text="Select a topic for the room", verbose_name="Topic")
    name = models.CharField(max_length=200, help_text="Enter the room name", verbose_name="Room Name")
    description = models.TextField(null=True, blank=True, help_text="Enter a description of the room", verbose_name="Description")
    
    # Watumiaji wanaoshiriki kwenye room hii
    participants = models.ManyToManyField(User, related_name='participants', blank=True, help_text="Select participants for the room", verbose_name="Participants")
    
    # Muda wa mwisho wa kubadilisha room hii
    updated = models.DateTimeField(auto_now=True, help_text="Time of the last update", verbose_name="Updated")
    # Muda room ilipoanzishwa
    created = models.DateTimeField(auto_now_add=True, help_text="Time the room was created", verbose_name="Created")

    class Meta:
        ordering = ['-updated', '-created']  # Rooms zitapangwa kwa kuanzia zilizoboreshwa karibuni

    def __str__(self):
        return self.name


# Model ya Message inawakilisha ujumbe ndani ya chumba
class Message(models.Model):
    # Mtumiaji aliyeandika ujumbe
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Author of the message", verbose_name="User")
    # Room ambayo ujumbe umetumwa
    room = models.ForeignKey(Room, on_delete=models.CASCADE, help_text="Room where the message was sent", verbose_name="Room")
    # Maandishi ya ujumbe
    body = models.TextField(help_text="Message text", verbose_name="Message")
    
    # Tarehe ya mwisho ujumbe ulipo haririwa
    updated = models.DateTimeField(auto_now=True, help_text="Time the message was last updated", verbose_name="Updated")
    # Tarehe ujumbe ulipotumwa
    created = models.DateTimeField(auto_now_add=True, help_text="Time the message was created", verbose_name="Created")

    class Meta:
        ordering = ['-updated', '-created']  # Message mpya ziwe juu

    def __str__(self):
        return self.body[0:50]  # Onyesha sehemu ya kwanza ya ujumbe kwenye display
