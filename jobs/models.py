from django.db import models


class JobModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="jobs")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'job'
        verbose_name_plural = 'jobs'
