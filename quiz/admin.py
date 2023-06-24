from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin
from . import models


@admin.register(models.QuizCategory)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right'
    ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
    ]
    inlines = [
        AnswerInlineModel,
    ]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
    ]

# admin.site.register(QuizCategory)
# admin.site.register(Quizzes)
# admin.site.register(Question)
# admin.site.register(Answer)
