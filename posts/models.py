from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()


class Tags(models.Model):
    title = models.CharField(max_length=255)


class Post(models.Model):
    header = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tags, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    def __str__(self):
        return f"{self.header}"
