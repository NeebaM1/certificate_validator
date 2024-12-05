from django.db import models

# Create your models here.
class Certificate(models.Model):
    certificate_no=models.IntegerField(null=True)
    name=models.CharField(max_length=50)
    expiry_date=models.DateField()


    def __str__(self):
        return self.name
