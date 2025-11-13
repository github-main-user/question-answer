from django.urls import path

from .apps import QaConfig
from .views import QuestionListCreateAPIView, QuestionRetrieveDestroyAPIView

app_name = QaConfig.name

urlpatterns = [
    path("questions/", QuestionListCreateAPIView.as_view(), name="questions-list"),
    path(
        "questions/<int:id>/",
        QuestionRetrieveDestroyAPIView.as_view(),
        name="questions-detail",
    ),
]
