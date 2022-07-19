from django.urls import path
from app.views import CreateUser,\
    AboutView,\
    IndexView, \
    LoginUser, \
    LogoutUser, \
    OfferList, \
    CreateOffer, \
    DeleteOffer, \
    MyOfferList, \
    UpdateOffer


urlpatterns = [
    path('', OfferList.as_view(), name='index'),
    # path('offers/', OfferList.as_view(), name='offers'),
    path('register/', CreateUser.as_view(), name='register'),
    path('offers/', OfferList.as_view(), name='offers'),
    path('my_offers/<pk>/delete/', DeleteOffer.as_view(), name='delete'),
    path('my_offers/', MyOfferList.as_view(), name='my_offers'),
    path('offers/create/', CreateOffer.as_view(), name='create'),
    path('my_offers/<int:pk>/update/', UpdateOffer.as_view(), name='update'),
    path('about/', AboutView.as_view(), name='about'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
]
