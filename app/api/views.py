from rest_framework.response import Response

from app.models import Offer, Respond, Profile, User
from rest_framework import generics, viewsets
from app.serializers import UserSerializer, OfferGetSerializer, OfferPostSerializer, \
    RespondGetSerializer, RespondPostSerializer, ProfileGetSerializer, ProfilePostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




# class UserAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserUpdateAPIView(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class OfferAPIView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OfferGetSerializer
        return OfferPostSerializer


class OfferUpdateAPIView(generics.UpdateAPIView):
    queryset = Offer.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OfferGetSerializer
        return OfferPostSerializer


class RespondAPIView(generics.ListCreateAPIView):
    queryset = Respond.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RespondGetSerializer
        return RespondPostSerializer


class RespondUpdateAPIView(generics.UpdateAPIView):
    queryset = Respond.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RespondGetSerializer
        return RespondPostSerializer


class ProfileAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()

    def get_object(self, queryset=None):
        user_id = self.kwargs.get(self.pk_url_kwarg)
        return Profile.objects.filter(user_id=user_id).first()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProfileGetSerializer
        return ProfilePostSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        instance = Profile.objects.filter(user_id=kwargs['pk']).first()
        serializer = serializer(instance, request.data)
        serializer.update(serializer.instance, serializer.validated_data)
        return Response('ok')
    #     # request.data['author'] = request.user
    #     # request.data.extend(request.user)
    #     # copy_data = request.data.copy()
    #
    #     user = request.user
    #     new_offer = Offer.objects.create(
    #         title=request.data['title'],
    #         author=user,
    #         text=request.data['text'],
    #     )
    #     return Response({'offer': model_to_dict(new_offer)})
