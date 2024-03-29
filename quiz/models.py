from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.email}"

class Quiz(models.Model):
    savol = models.CharField(max_length=100)
    jav1 = models.CharField(max_length=50)
    jav2 = models.CharField(max_length=50)
    jav3 = models.CharField(max_length=50)
    togri_jav = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.savol}"

class Quiz_Rus(models.Model):
    savol = models.CharField(max_length=100)
    jav1 = models.CharField(max_length=50)
    jav2 = models.CharField(max_length=50)
    jav3 = models.CharField(max_length=50)
    togri_jav = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.savol}"




