from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Date and time when the object was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Date and time when the object was last updated."
    )

    class Meta:
        abstract = True


class Question(TimeStampModel):
    text = models.TextField(blank=False, help_text="Question content")


class Answer(TimeStampModel):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
        help_text="Related question",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="answers",
        help_text="Author of the answer",
    )
    text = models.TextField(blank=False, help_text="Answer content")
