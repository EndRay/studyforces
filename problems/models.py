from django.db import models


class Problem(models.Model):
    statement = models.TextField()
    name = models.CharField(max_length=100)


class Tag(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
