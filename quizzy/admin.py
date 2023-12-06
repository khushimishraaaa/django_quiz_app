from django.contrib import admin
from .models import *

class AnswerInline(admin.TabularInline):
    model = Answer
    fk_name = 'questions'

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Answer)
