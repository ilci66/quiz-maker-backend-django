# TODO: create RDF serializers using the models defined
from dataclasses import fields
from rest_framework import serializers
from base.models import Test, Question, Answer, MyUser

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('name')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('test', 'text')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('test', 'test', 'answer')


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(email=self.validated_data['email'], date_of_birth=self.validated_data['date_of_birth'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value