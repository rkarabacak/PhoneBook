from django.conf import settings
from django.db import models
from django.utils import timezone
from phone_field import PhoneField

# Create your models here.

class Contacts(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    companyName = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phoneNumber1 = PhoneField(unique=True)
    phoneNumber2 = PhoneField(null=True, blank=True)
    address = models.TextField(max_length=254, blank=True, null=True)

    # def __str__(self):
    #     return self.firstName
           
    def __str__(self):
        if self.companyName:
            return """{} || {} {}""".format(self.companyName, self.firstName, self.lastName)
        else:  
           return """{} {}""".format(self.firstName, self.lastName)
        
        


    # def save(self, *args, **kwargs): # ilk harfı buyuten def
    #         for field_name in ['title', 'price', ... ]:
    #             val = getattr(self, field_name, False)
    #             if val:
    #                 setattr(self, field_name, val.capitalize())
    #         super(Product, self).save(*args, **kwargs)
   

    # class Caller(models.Model):
    #     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #     title = models.CharField(max_length=200)
    #     text = models.TextField()
    #     created_date = models.DateTimeField(default=timezone.now)
    #     published_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def __str__(self):
    #     return self.title
