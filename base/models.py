
from contextlib import nullcontext
from hashlib import blake2b
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser


CATEGORY = (
    ('Sell', 'Sell'),
    ('Rent', 'Rent'),
    ('PG', 'PG'),
)

PROPERTY_TYPE = (
    ('Apartment', 'Apartment'),
    ('Independent House', 'Independent House'),
)

NEGOTIABLE  = (
    ('Negotiable', 'Negotiable'),
    ('Not Negotiable', 'Not Negotiable'),
)

FURNISHING = (
    ('Furnished', 'Furnished'),
    ('Semi Furnished', 'Semi Furnished'),
    ('Un-Furnished', 'Un-Furnished'),
)

AGE_OF_PROPERTY = (
    ('0-1 years', '0-1 years'),
    ('1-5 years', '1-5 years'),
    ('5-10 years', '5-10 years'),
    ('10+ years', '10+ years'),
)

RENT_OUT_TO = (
    ('Family', 'Family'),
    ('Men', 'Men'),
    ('Girls', 'Girls'),
)

SECURITY_DEPOSIT = (
    ('Fixed', 'Fixed'),
    ('Multiple of Rent', 'Multiple of Rent'),
    ('None', 'None')
)

BEDROOM = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

BATHROOM = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

BALCONIES = (    
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)





class User(AbstractUser):
    name  = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, unique=True)
    profile = models.ImageField(null=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
    


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.CharField(choices=CATEGORY, max_length=100, null=True)
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE, null=True)
    address = models.CharField(max_length=100, null=True)
    negotiable = models.CharField(max_length=100, choices=NEGOTIABLE, null=True)
    furnishing = models.CharField(max_length=100, choices=FURNISHING, null=True)
    age_of_property = models.CharField(max_length=50, choices=AGE_OF_PROPERTY, null=True)
    rent_out_to = models.CharField(max_length=50, choices=RENT_OUT_TO, null=True)
    security_deposite = models.CharField(max_length=100, choices=SECURITY_DEPOSIT, null=True)
    bedroom = models.CharField(max_length=2, choices=BEDROOM)
    bathroom = models.CharField(max_length=2, choices=BATHROOM)
    balconies = models.CharField(max_length=2, choices=BALCONIES)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)



class Property_Image(models.Model):
    Property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(null=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    message = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)