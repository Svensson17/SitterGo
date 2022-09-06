from rest_framework import serializers
from app.models import Offer, Respond, User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio')


class OfferGetSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Offer
        fields = ('title', 'author', 'text')


class OfferPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('title', 'author', 'text')


class RespondGetSerializer(serializers.ModelSerializer):
    offer = OfferGetSerializer()
    user = UserSerializer()

    class Meta:
        model = Respond
        fields = ('name', 'text', 'user', 'offer')


class RespondPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respond
        fields = ('name', 'text', 'user', 'offer')
        # depth = 1


class ProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'date_of_birth', 'photo')


class ProfilePostSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    bio = serializers.CharField()
    date_of_birth = serializers.CharField()
    # photo = serializers.CharField()

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', 'first_name', 'last_name', 'bio')

    # def create(self, validated_data):
    #     return Profile(**validated_data)

    def update(self, instance, validated_data):
        user = instance.user
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.bio = validated_data['bio']
        user.save()

        instance.date_of_birth = validated_data['date_of_birth']
        # instance.photo = validated_data['photo']
        instance.save()

        return instance

