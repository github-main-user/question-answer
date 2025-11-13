from typing import override

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics

from .models import Answer, Question
from .serializers import (
    AnswerSerializer,
    QuestionSerializer,
    QuestionWithAnswersSerializer,
)


@extend_schema(tags=["Questions"])
@extend_schema_view(
    get=extend_schema(
        summary="List all questions",
        description="Retrieve a list of all available questions.",
    ),
    post=extend_schema(
        summary="Create a new question",
        description="Create a new question entry.",
    ),
)
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@extend_schema(tags=["Questions"])
@extend_schema_view(
    get=extend_schema(
        summary="Retrieve a specific question",
        description="Retrieve details of a single question, including its answers.",
    ),
    delete=extend_schema(
        summary="Delete a question",
        description="Delete a question.",
    ),
)
class QuestionRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionWithAnswersSerializer


@extend_schema(tags=["Answers"])
@extend_schema_view(
    post=extend_schema(
        summary="Create a new answer for a specific question",
        description="Create a new answer for a question identified by 'question_pk'."
        "Requires authentication.",
    ),
)
class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @override
    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        serializer.save(question=question)


@extend_schema(tags=["Answers"])
@extend_schema_view(
    get=extend_schema(
        summary="Retrieve a specific answer",
        description="Retrieve details of a single answer.",
    ),
    delete=extend_schema(summary="Delete an answer", description="Delete an answer."),
)
class AnswerRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
