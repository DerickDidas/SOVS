from django.db import models



# Create your models here.
class Position(models.Model):
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.position


class Candidate(models.Model):
    position = models.ForeignKey(Position,on_delete=models.CASCADE,related_name='choices')
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name