from django.db import models


class Subscriber(models.Model):
    mail = models.EmailField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.mail.__str__()
