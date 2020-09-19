from django.db import models

# Create your models here.


class Journalist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class NewsModel(models.Model):
    author = models.ForeignKey(
        Journalist, on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"The author name{self.author} and news title is {self.title}"
