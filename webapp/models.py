from django.db import models



class Reservation(models.Model):
    customer_name = models.CharField(max_length=50, null=True)
    number_of_customer = models.IntegerField( null=True)
    Time = models.TimeField(max_length=50, null=True)
    Date = models.DateField(max_length=50, null=True)

    def __str__(self):
        return self.customer_name




class Feedback(models.Model):
    customer = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField(max_length=50, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment



