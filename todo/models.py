from django.db import models

priority_choices = [
    (1,'Heigh'),
    (2,'Medium'),
    (3,'Low'),
]

status_choices = [
    ('c','Completed'),
    ('w','Waiting'),
    ('p','On Progress'),
]

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.SmallIntegerField(choices=priority_choices, default=3)
    status = models.CharField(max_length=15, choices=status_choices, default="w")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.title