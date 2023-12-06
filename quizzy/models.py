from django.db import models
import uuid
import random


class Basemodel(models.Model):
    uid= models.UUIDField(primary_key=True, default=uuid.uuid4)   

    class META:
        abstract = True
    
class Category(Basemodel ):
    category_name = models.TextField()

    def __str__(self) -> str:
        return self.category_name

class Question(Basemodel):
    categories = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question_text
    
    def get_answer(self):
        answer_objs = list(Answer.objects.filter(questions=self))
        data = []
        random.shuffle(answer_objs)
        for answer_obj in answer_objs:
            data.append({
                'answer_text': answer_obj.answer_text,
                'is_correct' : answer_obj.is_correct
            })

        return data

class Answer(Basemodel):
    questions = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer_text
