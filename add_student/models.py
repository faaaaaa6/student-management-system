from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
