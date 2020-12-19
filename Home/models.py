from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class ToDoList(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Yapılacak Listesi")
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']

class Items(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,related_name="kullanici")
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, verbose_name="Başlık")
    content = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    last_date = models.DateTimeField(verbose_name="Tarih")
    created_date = models.DateTimeField(auto_now_add=True)
    durum = models.BooleanField(default=False, verbose_name="Yapıldı")

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-last_date']

