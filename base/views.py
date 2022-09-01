from rest_framework import routers, serializers, viewsets
from base.serializers import TestSerializer, QuestionSerializer, AnswerSerializer
from .models import Question, Test, Answer
from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.shortcuts import render

# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

# done for now 