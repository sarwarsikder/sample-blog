from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator


def validate_video_size(value):
    max_size = 250 * 1024 * 1024  # 250 MB
    if value.size > max_size:
        raise ValidationError("File size must be no more than 250 MB.")


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    video = models.FileField(
        upload_to='videos/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv']),
            validate_video_size,
        ]
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.post.title} - Image {self.pk}"
