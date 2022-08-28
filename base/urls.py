# TODO: create the urls here using rdf router
from django.urls import include, path
from rest_framework import routers
from base.views import TestViewSet, QuestionViewSet, AnswerViewSet


router = routers.DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]