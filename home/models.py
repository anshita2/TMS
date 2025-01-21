from django.db import models

# Create your models here.
class Trainee_model(models.Model):
    name=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    course=models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['name', 'phone', 'email', 'course', 'domain'], 
    #             name='unique_trainee'
    #         )
    #     ]