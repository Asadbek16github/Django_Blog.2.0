from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    Sarlovha = models.CharField(max_length=150)
    Qisqacha_Matn = models.CharField(max_length=200)
    Matn = models.TextField()
    Rasm = models.ImageField(upload_to='images/', blank=True)
    Vaqt = models.DateTimeField(auto_now_add=True)
    Mualliff = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    ) 

    def __str__(self):
        return self.Sarlovha
    
    def get_absolute_url(self):
        return reverse('articleDetail', args=[str(self.id)])