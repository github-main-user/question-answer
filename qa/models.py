from django.db import models


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

    def __str__(self) -> str:
        return f'Question: "{self.text[:30]}"'


class Answer(TimeStampModel):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
        help_text="Related question",
    )
    user = models.UUIDField(help_text="UUID of author")
    text = models.TextField(blank=False, help_text="Answer content")

    def __str__(self) -> str:
        return f'Answer: "{self.text[:30]}" to "{self.question}" by "{self.user}"'
