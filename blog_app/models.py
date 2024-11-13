from django.db import models    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
