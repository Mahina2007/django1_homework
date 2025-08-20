from django.db import models


class PostAuthorModel(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/')
    bio = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'post author'
        verbose_name_plural = 'posts authors'


class PostModel(models.Model):
    category = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/')
    overview = models.CharField(max_length=255)

    author = models.ForeignKey(
        PostAuthorModel,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


