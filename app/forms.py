from app.models import Offer, Respond, Profile
from django.forms import ModelForm, CharField, widgets, ImageField
from string import Template
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


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

# class UserEditForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')


class PictureWidget(widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value.url))


class ProfileEditForm(ModelForm):
    photo = ImageField(widget=PictureWidget)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    bio = CharField(max_length=32)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'date_of_birth', 'bio', 'photo')


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = [
            'title',
            'text',
        ]


class RespondForm(ModelForm):
    class Meta:
        model = Respond
        fields = ('name', 'email', 'text')
