from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class CreateUserSerializer(ModelSerializer):
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(username=user_data.pop('username'),
                                        email=user_data.pop('email'),
                                        first_name=user_data.pop('first_name'),
                                        last_name=user_data.pop('last_name'))
        user.set_password(user_data.pop('password'))
        user.save()
        ModelClass = self.Meta.model
        return ModelClass.objects.create(user=user, **validated_data)
