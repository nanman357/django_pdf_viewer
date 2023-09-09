from django.db import models

class PDF(models.Model):
    file = models.FileField(upload_to='pdfs/')