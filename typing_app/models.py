from django.db import models

# Create your models here.

class Word(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class TypingTest(models.Model):
    wpm = models.IntegerField()
    accuracy = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Test {self.id} - WPM: {self.wpm}, Accuracy: {self.accuracy}%"
