from django.contrib import admin

from .models import Answer, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text",)
    search_fields = ("text",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question__text", "user", "text")
    search_fields = ("question__text", "text")
    list_filter = ("user",)
