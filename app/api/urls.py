from django.urls import path, include
from app.api.views import OfferAPIView, RespondAPIView, ProfileAPIView, \
    OfferUpdateAPIView, RespondUpdateAPIView, UserViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/user/', UserViewSet.as_view({'get': 'list'})),
    # path('api/v1/user/<int:pk>/', UserViewSet.as_view({'put': 'update'})),
    # path('api/v1/user/<int:pk>/', UserViewSet.as_view({'post': 'create'})),
    # path('api/v1/user/<int:pk>/', UserViewSet.as_view({'delete': 'destroy'})),
    path('api/v1/offer/', OfferAPIView.as_view()),
    path('api/v1/offer/update/<int:pk>/', OfferUpdateAPIView.as_view()),
    path('api/v1/respond/', RespondAPIView.as_view()),
    path('api/v1/respond/update/<int:pk>/', RespondUpdateAPIView.as_view()),
    path('api/v1/profile/<int:pk>/', ProfileAPIView.as_view()),
    path('api/v1/profile/', ProfileAPIView.as_view()),
]
