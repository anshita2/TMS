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

class Course_model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)  # Name of the course
    duration = models.CharField(max_length=100)  # Duration (e.g., "3 months")
    start_date = models.DateField()  # Start date of the course
    end_date = models.DateField()  # End date of the course
    venue_name = models.CharField(max_length=200)  # Name of the venue
    trainees_enrolled = models.PositiveIntegerField()  # Number of trainees enrolled
    faculty = models.CharField(max_length=200)  # Faculty name(s)

    def __str__(self):
        return self.name 
    
class Faculty_model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    category = models.CharField(max_length=20, choices=(('In-house', 'In-house'), ('External', 'External')))
    def __str__(self):
        return self.name