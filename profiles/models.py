from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from PIL import Image

def user_directory_path(instance, filename):
    return 'users/photos/{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE)
    middlename = models.CharField(max_length=200, blank=True,null=True)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    unit = models.CharField(max_length=200, verbose_name="ICT Unit")
    position = models.CharField(max_length=200, verbose_name="Designation")
    office_ext = models.CharField(max_length=100, verbose_name="Extension No.")
    mobile = models.CharField(max_length=50, verbose_name="Mobile Number")
    speed_dial = models.CharField(max_length=50, blank=True, null=True,verbose_name="Speed Dial")
    photo = models.ImageField(default='default2.png', upload_to=user_directory_path)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
        
    class Meta:
        ordering = ('-id',)
    
    def save(self, *args, **kwargs):
        if self.middlename:
            self.full_name = self.user.first_name + ' ' + self.middlename + ' ' + self.user.last_name
        else:
            self.full_name = self.user.first_name + ' ' + self.user.last_name
        return super(Profile, self).save(*args, **kwargs)
    
            
    
    

