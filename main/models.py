from django.contrib.auth.models import User
from django.db import models
import numpy as np


class Score(models.Model):
    age = models.IntegerField()
    score1 = models.FloatField()
    score2 = models.FloatField()
    score3 = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_kth_percentile(self, k):
        arr = [self.score1, self.score2, self.score3]
        return np.percentile(arr, k)




