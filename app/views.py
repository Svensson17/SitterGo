from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from app.forms import UserForm, OfferForm
from app.models import Offer
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, UpdateView


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserForm

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

