from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField()

    def __str__(self):
        return self.get_full_name()


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%d', blank=True)

    def __str__(self):
        return f'Profile {self.user}'


class Offer(models.Model):
    title = models.CharField(verbose_name='offer_title', max_length=30)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Respond(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='responds')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='responds')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.text
