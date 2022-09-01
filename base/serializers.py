# TODO: create RDF serializers using the models defined
from dataclasses import fields
from rest_framework import serializers
from base.models import Test, Question, Answer

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

