from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    post_content = models.TextField()
    post_thumbnail = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.post_title

    def summary(self):
        return self.post_content[:300]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')