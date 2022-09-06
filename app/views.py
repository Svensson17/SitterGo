from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from app.forms import OfferForm, RespondForm, ProfileEditForm, UserForm
from app.models import Offer, Respond, Profile, User
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework import viewsets, permissions
from app.serializers import UserSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserForm

    def form_valid(self, form):
        response = super().form_valid(form)
        profile = Profile.objects.create(user=self.object)
        return response

    def get_success_url(self):
        return reverse('index')

    template_name = 'registration/register.html'
    success_message = 'User was successfully created'


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('index')


class LogoutUser(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You are logged out')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('index')


class CreateOffer(LoginRequiredMixin, CreateView):
    model = Offer
    form_class = OfferForm
    template_name = 'offers/create_offer.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('my_offers')


class DeleteOffer(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Offer
    template_name = 'offers/delete_offer.html'
    success_message = 'Offer successfully deleted'

    def get_success_url(self):
        return reverse('my_offers')


class OfferList(ListView):
    model = Offer
    template_name = 'index.html'
    context_object_name = 'offers'

    def get_success_url(self):
        return reverse('offers')


class MyOfferList(ListView):
    model = Offer
    template_name = 'offers/my_offers.html'
    context_object_name = 'my_offers'

    def get_queryset(self):
        user = self.request.user
        return Offer.objects.filter(author=user)

    def get_success_url(self):
        return reverse('my_offers')


class UpdateOffer(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Offer
    form_class = OfferForm
    template_name = 'offers/update_offer.html'
    success_message = 'Offer successfully updated'

    def get_success_url(self):
        return reverse('my_offers')


class CreateRespond(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    # new_respond.post = offer
    model = Respond
    form_class = RespondForm
    template_name = 'responds/create_respond.html'
    success_message = 'Respond successfully created'

    def form_valid(self, form):
        offer_id = self.kwargs.get(self.pk_url_kwarg)
        offer = Offer.objects.filter(pk=offer_id).first()
        user = self.request.user
        form.instance.offer = offer
        form.instance.user = user
        return super(CreateRespond, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')


class UpdateRespond(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Respond
    form_class = RespondForm
    template_name = 'responds/update_respond.html'
    success_message = 'Respond successfully updated'

    def get_success_url(self):
        return reverse('my_responds')


class DeleteRespond(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Respond
    template_name = 'responds/delete_respond.html'
    success_message = 'Respond successfully deleted'

    def get_success_url(self):
        return reverse('my_responds')


class MyRespondList(ListView):
    model = Respond
    template_name = 'responds/my_responds.html'
    context_object_name = 'my_responds'

    def get_queryset(self):
        user = self.request.user
        return Respond.objects.filter(user=user)

    def get_success_url(self):
        return reverse('my_responds')


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = 'profile/update_profile.html'
    # context_object_name = 'user'
    # queryset = UserProfile.objects.all()
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse('index')

    def get_object(self, queryset=None):
        user_id = self.kwargs.get(self.pk_url_kwarg)
        return Profile.objects.filter(user_id=user_id).first()

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileView, self).get_context_data(**kwargs)
    #     user = self.request.user
    #     context['form'] = ProfileEditForm(
    #         instance=user.profile,
    #         initial={
    #             'first_name': user.first_name,
    #             'last_name': user.last_name,
    #             'bio': user.bio}
    #     )
    #     return context

    def form_valid(self, form):
        from django.http import HttpResponseRedirect
        profile = form.save()
        user = profile.user
        user.last_name = form.cleaned_data['last_name']
        user.first_name = form.cleaned_data['first_name']
        user.bio = form.cleaned_data['bio']
        user.save()
        return HttpResponseRedirect(self.get_success_url())
