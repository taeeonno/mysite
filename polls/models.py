from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#CASCADE : 질문이 삭제되면 답도 같이 삭제되겠다
    choice_text= models.CharField(max_length=200)#choice의 question은 Question을 참조하고있는데 하나의 질문에 여러 답이 있을 수 있으므로 1대 다 관계이다
    votes=models.IntegerField(default=0)    