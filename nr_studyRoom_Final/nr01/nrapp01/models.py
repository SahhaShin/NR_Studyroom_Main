from django.db import models

# Create your models here.
#성준재
class Board(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    people = models.IntegerField()
    memo = models.TextField()
    m_d = models.CharField(max_length=5)
    def __str__(self):
        return self.name


#재이
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Qa(BaseModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Comment(BaseModel):
    post = models.ForeignKey(Qa, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100)
    content = models.TextField()