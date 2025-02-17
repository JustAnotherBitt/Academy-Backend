from django.db import models

belt_choices = (
        ('W', 'White'),
        ('B', 'Blue'),
        ('P', 'Purple'),
        ('Br', 'Brown'),
        ('Bl', 'Black')
    )

class Students(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    belt = models.CharField(max_length=2, choices=belt_choices, default='W')
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class CompletedLessons(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    current_belt = models.CharField(max_length=2, choices=belt_choices, default='W')

    def __str__(self):
        return self.student.name