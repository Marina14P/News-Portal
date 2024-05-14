from django.db import models

class Post(models.Model):
    POST_TYPES = (
        ('news', 'News'),
        ('article', 'Article'),
    )
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    content = models.TextField()
    post_type = models.CharField(max_length=7, choices=POST_TYPES)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title