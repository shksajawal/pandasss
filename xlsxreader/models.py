from django.db import models

# Create your models here.
class ExcelFileUpload(models.Model):
    uploaded_file = models.FileField(upload_to='excel/')

