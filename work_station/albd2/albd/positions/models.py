from django.db import models

# Create your models here.


class Position(models.Model):
    display_name = models.CharField(max_length=100, default="Untitled")
    rank = models.IntegerField(blank=False, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Content Position"

    def __str__(self):
        return self.display_name
