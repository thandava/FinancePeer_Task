from django.db import models

class Profile(models.Model):
   userid = models.IntegerField()
   id=models.IntegerField(primary_key=True)
   title=models.TextField()
   body=models.TextField()


   class Meta:
      db_table = "profile"
