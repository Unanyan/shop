from django.db import models


class Subscriber(models.Model):
    mail = models.EmailField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.mail.__str__()


class Customer(models.Model):
    name = models.CharField(max_length=45)
    mail = models.EmailField()
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=9, null=True)

    def __str__(self):
        return self.name.__str__() + ' ' + self.phone.__str__() + ' ' + self.mail.__str__() + ' ' + self.address.__str__()
