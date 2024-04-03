from django.db import models


class ProjectsModal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    href = models.URLField(max_length=200, blank=True, null=True)
    links = models.JSONField(default=list)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
