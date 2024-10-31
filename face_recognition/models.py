from django.db import models

# Create your models here.
class Student(models.Model):
    SPECIALITY_CHOICES = [
        ('GL', 'Génie Logiciel'),
        ('DS', 'Data Science'),
        ('RC', 'Réseau et Cloud'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    class_name = models.CharField(max_length=50)
    speciality = models.CharField(
        max_length=2,
        choices=SPECIALITY_CHOICES,
        default='GL'
    )
    image = models.ImageField(upload_to='student_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.speciality}"
