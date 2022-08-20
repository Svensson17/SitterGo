from django.urls import path
from app.views import CreateUser, \
    AboutView, \
    LoginUser, \
    LogoutUser, \
    OfferList, \
    CreateOffer, \
    DeleteOffer, \
    MyOfferList, \
    UpdateOffer, \
    ProfileView, CreateRespond, MyRespondList, UpdateRespond, DeleteRespond

urlpatterns = [
    path('', OfferList.as_view(), name='index'),
    path('register/', CreateUser.as_view(), name='register'),
    path('offers/', OfferList.as_view(), name='offers'),
    path('my_offers/<pk>/delete/', DeleteOffer.as_view(), name='delete'),
    path('my_offers/', MyOfferList.as_view(), name='my_offers'),
    path('offers/create/', CreateOffer.as_view(), name='create'),
    path('my_responds/', MyRespondList.as_view(), name='my_responds'),
    path('responds/<int:pk>/create/', CreateRespond.as_view(), name='create_respond'),
    path('my_responds/<int:pk>/update/', UpdateRespond.as_view(), name='update_respond'),
    path('my_responds/<int:pk>/delete/', DeleteRespond.as_view(), name='delete_respond'),
    path('my_offers/<int:pk>/update/', UpdateOffer.as_view(), name='update'),
    path('profile/<int:pk>/update/', ProfileView.as_view(), name='update_profile'),
    path('about/', AboutView.as_view(), name='about'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
]
