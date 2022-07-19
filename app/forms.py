from django.contrib.auth.forms import UserCreationForm, get_user_model
from app.models import Offer
from django.forms import ModelForm
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = [
            'title',
            'text',
            # 'published_date'
        ]


