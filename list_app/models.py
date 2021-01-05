from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    item_owner_id = models.ForeignKey(User,on_delete=models.CASCADE)
    item_text = models.CharField(max_length=500)
    item_prio = models.IntegerField(default=0)
    item_done = models.BooleanField(default=False)
    def __str__(self):
        return str(self.item_owner_id) + " " + str(self.item_prio)
