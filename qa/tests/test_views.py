import uuid

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from qa.models import Answer, Question

# ========
# fixtures
# ========


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_uuid() -> uuid.UUID:
    return uuid.uuid4()


@pytest.fixture
def question() -> Question:
    return Question.objects.create(text="Question 1")


@pytest.fixture
def answer(question: Question, user_uuid: uuid.UUID) -> Answer:
    return Answer.objects.create(question=question, user=user_uuid, text="Answer 1")


@pytest.fixture
def questions() -> list[Question]:
    return [Question.objects.create(text="Question 1") for _ in range(5)]


# ===================
# tests for questions
# ===================


@pytest.mark.django_db
def test_question_list(api_client, questions):
    response = api_client.get(reverse("qa:question-list-create"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(questions)


@pytest.mark.django_db
def test_question_create(api_client):
    assert Question.objects.filter(text="new question").count() == 0

    response = api_client.post(
        reverse("qa:question-list-create"), {"text": "new question"}
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert Question.objects.filter(text="new question").count() == 1


@pytest.mark.django_db
def test_question_retrieve(api_client, question: Question):
    response = api_client.get(reverse("qa:question-detail", args=[question.pk]))

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("id") == question.pk
    assert response.data.get("text") == question.text


@pytest.mark.django_db
def test_question_destroy(api_client, question: Question, answer: Answer):
    assert Question.objects.filter(pk=question.pk).exists()
    assert Answer.objects.filter(pk=answer.pk).exists()

    response = api_client.delete(reverse("qa:question-detail", args=[question.pk]))

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Question.objects.filter(pk=question.pk).exists()
    assert not Answer.objects.filter(pk=answer.pk).exists()


# =================
# tests for answers
# =================


@pytest.mark.django_db
def test_answer_create(api_client, question: Question, user_uuid: uuid.UUID):
    assert Answer.objects.filter(question=question).count() == 0

    response = api_client.post(
        reverse("qa:answer-create", args=[question.pk]),
        {"text": "new answer", "user": str(user_uuid)},
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert Answer.objects.filter(question=question).count() == 1
    assert Answer.objects.get(question=question).text == "new answer"


@pytest.mark.django_db
def test_answer_create_multiple_by_same_user(
    api_client, question: Question, user_uuid: uuid.UUID
):
    assert Answer.objects.filter(question=question).count() == 0

    # first answer
    response1 = api_client.post(
        reverse("qa:answer-create", args=[question.pk]),
        {"text": "first answer", "user": str(user_uuid)},
    )
    assert response1.status_code == status.HTTP_201_CREATED
    assert Answer.objects.filter(question=question).count() == 1

    # second answer by the same user
    response2 = api_client.post(
        reverse("qa:answer-create", args=[question.pk]),
        {"text": "second answer", "user": str(user_uuid)},
    )
    assert response2.status_code == status.HTTP_201_CREATED
    assert Answer.objects.filter(question=question).count() == 2

    # verify both answers are linked to the same question and user
    answers = Answer.objects.filter(question=question, user=user_uuid)
    assert answers.count() == 2
    assert answers.filter(text="first answer").exists()
    assert answers.filter(text="second answer").exists()


@pytest.mark.django_db
def test_answer_retrieve(api_client, answer: Answer):
    response = api_client.get(reverse("qa:answer-detail", args=[answer.pk]))

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("id") == answer.pk
    assert response.data.get("text") == answer.text
    assert response.data.get("user") == str(answer.user)


@pytest.mark.django_db
def test_answer_destroy(api_client, answer: Answer):
    assert Answer.objects.filter(pk=answer.pk).exists()

    response = api_client.delete(reverse("qa:answer-detail", args=[answer.pk]))

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Answer.objects.filter(pk=answer.pk).exists()


@pytest.mark.django_db
def test_answer_create_non_existent_question(api_client, user_uuid: uuid.UUID):
    non_existent_question_pk = 99999
    assert not Question.objects.filter(pk=non_existent_question_pk).exists()

    response = api_client.post(
        reverse("qa:answer-create", args=[non_existent_question_pk]),
        {"text": "new answer", "user": str(user_uuid)},
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert Answer.objects.count() == 0
