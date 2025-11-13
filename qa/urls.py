from django.urls import path

from .apps import QaConfig
from .views import (
    AnswerCreateAPIView,
    AnswerRetrieveDestroyAPIView,
    QuestionListCreateAPIView,
    QuestionRetrieveDestroyAPIView,
)

app_name = QaConfig.name

urlpatterns = [
    path(
        "questions/", QuestionListCreateAPIView.as_view(), name="question-list-create"
    ),
    path(
        "questions/<int:pk>/",
        QuestionRetrieveDestroyAPIView.as_view(),
        name="question-detail",
    ),
    path(
        "questions/<int:question_pk>/answers/",
        AnswerCreateAPIView.as_view(),
        name="answer-create",
    ),
    path(
        "answers/<int:pk>/",
        AnswerRetrieveDestroyAPIView.as_view(),
        name="answer-detail",
    ),
]