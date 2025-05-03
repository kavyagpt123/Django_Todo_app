from django.db import models

# Create your models here.
class Transactions(models.Model):
    title=models.CharField(max_length=110)
    amount=models.FloatField()
    description=models.CharField(max_length=110,choices=(("CREDIT","CREDIT"),("DEBIT", "DEBIT")))
    date=models.DateField()

    def save(self, *args, **kwargs):
        if self.description == "DEBIT":
            self.amount=self.amount * -1
        return super().save(*args, **kwargs)