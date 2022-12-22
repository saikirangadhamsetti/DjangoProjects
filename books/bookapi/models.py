from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=100)
    number_of_pages=models.IntegerField()
    published_date=models.DateField()
    quantity=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.title

