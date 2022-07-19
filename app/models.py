from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Offer(models.Model):
    title = models.CharField(verbose_name='offer_title', max_length=30)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    # published_date = models.DateTimeField(blank=True, null=True).order_by('-published_date')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




