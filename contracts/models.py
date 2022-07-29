from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from vendors.models import Vendor
from profiles.models import Profile

from datetime import datetime, date, timedelta
from django.utils import timezone
from decimal import Decimal

# Create your models here.
AGREEMENT_TYPE_CHOICES = [
    (None,'Select agreement type'),
    ('Master Service Agreement','Master Service Agreement'),
    ('Service Level Agreement','Service Level Agreement'), 
    ('Fixed Contract','Fixed Contract'),
    ('Subscription Agreement','Subscription Agreement'),
    ('Pay-per-Use','Pay-per-Use'),
]


# Create your models here.
class Contract(models.Model):
    description = models.CharField(max_length=300)
    responsible_unit = models.CharField(max_length=300, verbose_name="Responsible Unit")
    owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, 
                            max_length=300, verbose_name="Responsible Manager")
    supplier = models.ForeignKey(Vendor,default=1, related_name='vendors', 
                                on_delete=models.DO_NOTHING)
    total_value = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10, 
                                    verbose_name="Contract Value")
    amount_outstanding = models.DecimalField(default=Decimal('0.0'),decimal_places=2, max_digits=10,
                                            verbose_name="Amount Outstanding", editable=False)
    agreement_type = models.CharField(verbose_name="Agreement Type" ,max_length=150, 
                                    choices=AGREEMENT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    # duration = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=300, default='Active - Ok', editable=False)
    date_signed = models.DateField(blank=True, null=True)
    ul_signatory = models.CharField(max_length=300, verbose_name="UL Signatory")
    supplier_signatory = models.CharField(max_length=300, verbose_name="Supplier Signatory")
    contract_document = models.FileField(upload_to='contracts/%Y/%F')
    comments = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,editable=False)
    
    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ('-uploaded',)
        
        
    def get_absolute_url(self):
        return reverse ('contracts:contract-admin-detail', kwargs={'pk':self.pk})
    
    @property
    def duration(self):
        # duration_delta  = timedelta(months=12)
        if self.end_date :
            contract_duration_days= self.end_date - self.start_date
            contract_duration =int(str(contract_duration_days).split(' ',1)[0])/366
            duration = round(contract_duration)
        else:
            duration = None
        return duration
    
    
    @property
    def time_until_end(self):
        today = date.today()
        if not self.end_date:
            days_until_int= None
        else:
            days = self.end_date - today
            days_until= str(days).split(' ')[0]
            days_until_int= int(days_until)
        return days_until_int

    
    def save(self, *args, **kwargs):
        if self.time_until_end > 365:  
            self.status = "Active - Ok"
        elif self.time_until_end < 365 and self.time_until_end >= 180:
            self.status = "Active - Alert 1"
        elif self.time_until_end < 180 and self.time_until_end >= 0:
            self.status = "Active - Alert 2"
        else:
            self.status = "Expired"
        return super(Contract, self).save(*args,**kwargs)
        
    @property
    def days_till_renewal(self):
        today = date.today()
        days_to_expiry = self.end_date - today
        days_to_expiry = str(days_to_expiry).split(' ',1)[0]
        int_days_to_expiry = int(days_to_expiry)
        return int_days_to_expiry
    
