from rest_framework import generics

from .models import Question
from .serializers import QuestionSerializer, QuestionWithAnswersSerializer


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionWithAnswersSerializer
