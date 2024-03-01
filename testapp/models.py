from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    gamesense = models.IntegerField(default=0)
    storygames = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    # class Meta:
        # ordering = ['id']