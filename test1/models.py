from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator


# Create your models here.
 
class Language(models.Model):
    NATIVE = 'N'
    EXCELLENT = 'E'
    GOOD = 'G'
    SATISFACTORY='S'
    POOR = 'P'

    READING_CHOICES=[
        (NATIVE,'NATIVE'),
        (EXCELLENT,'EXCELLENT'),
        (GOOD,'GOOD'),
        (SATISFACTORY,'SATISFACTORY'),
        (POOR,'GOOPOORD')
    ]

    WRITING_SKILLS=[
        (NATIVE,'NATIVE'),
        (EXCELLENT,'EXCELLENT'),
        (GOOD,'GOOD'),
        (SATISFACTORY,'SATISFACTORY'),
        (POOR,'GOOPOORD')
    ]

    SPEAKING_SKILLS=[
        (NATIVE,'NATIVE'),
        (EXCELLENT,'EXCELLENT'),
        (GOOD,'GOOD'),
        (SATISFACTORY,'SATISFACTORY'),
        (POOR,'GOOPOORD')
    ]

    name = models.CharField(max_length=255)
    reading = models.CharField(
        max_length=1, choices=READING_CHOICES, default=GOOD)
    writing = models.CharField(
        max_length=1, choices=WRITING_SKILLS, default=GOOD)
    speaking = models.CharField(
        max_length=1, choices=SPEAKING_SKILLS, default=GOOD)

    def __init__(self, name,reading,writing,speaking):
         self.name = name
         self.reading = reading
         self.writing=writing
         self.speaking=speaking

     
        
class Client(models.Model):
    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    ARABIC = 'ar'
    ENGLISH = 'en'
    GENDER_CHOICES = [
        (FEMALE, 'FEMALE'),
        (MALE, 'MALE') ]

    LANGUAGES_CHOICES = [
        (ARABIC, 'Arabic'),
        (MALE, 'English') ]

    client_profile_img = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)
    bio = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=MALE)
    nationality = CountryField(blank_label='(select nationality)')
    country_of_residence = CountryField(blank_label='(select country of residence)')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+970'. Up to 9 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=14)
    linkedin_link = models.CharField(max_length=255,default='')
    language =models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True, blank=True)
    


