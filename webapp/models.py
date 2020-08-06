from django.db import models
from django.shortcuts import reverse
# Create your models here.
Company_CHOICES=(('1','Rapid Technologies LLC'),('2','Rapid Group of Companies'),('',''))
Division_CHOICES=(('Staffing','Staffing'),('Training','Training'),('IT Services','IT Services'))
Sector_CHOICES=(('USA','USA'),('India','India'))
CONTIGUOUS_STATES = (('US STATES', 'US STATES'),('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))
STATE_CHOICES = (('INDIAN STATES', 'INDIAN STATES'),('TS', 'Telegana'),('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('MH', 'Maharashtra'), ('UP', 'Uttar Pradesh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chattisgarh'), ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Orissa'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'), ('UA', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LD', 'Lakshadweep'), ('PY', 'Pondicherry'))

class Company_detailes(models.Model):
    Company=models.TextField(max_length=80)
    Division=models.TextField(max_length=20, choices=Division_CHOICES,default='1')
    Sector=models.TextField(max_length=20, choices=Sector_CHOICES,default='2')
    Phone=models.IntegerField(blank=False,null=True)
    Fax=models.IntegerField(blank=True, null=True)
    Website=models.TextField(blank=False,null=True)
    Industry=models.TextField(blank=False,null=True)
    NAICS_codes = models.TextField(blank=True, null=True)
    Revenue = models.IntegerField(blank=True, null=True)
    EstimatedPayroll=models.IntegerField(blank=True, null=True)
    Number_of_Employees=models.IntegerField(blank=True, null=True)
    Number_of_Internal_Employees=models.IntegerField(blank=True, null=True)
    Number_of_consultants_on_OPT=models.IntegerField(blank=True, null=True)
    Number_of_consultants_on_CPT=models.IntegerField(blank=True, null=True)
    Number_of_consultants_on_H1B=models.IntegerField(blank=True, null=True)
    Number_of_card_consultants=models.IntegerField(blank=True, null=True)
    Number_of_US_Citizens=models.IntegerField(blank=True, null=True)
    Number_of_consultants_on_other_visa=models.IntegerField(blank=True, null=True)
    AddressLine1=models.TextField(blank=False,null=True)
    AddressLine2=models.TextField(blank=False,null=True)
    City=models.TextField(blank=False,null=True)
    State=models.TextField(blank=True,null=True,choices=STATE_CHOICES,default='INDIAN STATES')
    States=models.TextField(blank=True,null=True,choices=CONTIGUOUS_STATES,default='US STATES',help_text='Any one Indian or US state')
    Zipcode=models.TextField(blank=False,null=True)
    FederalID_EIN=models.TextField(blank=False,null=True)
    GST_Number=models.TextField(blank=False,null=True)
    AddadditionalInformation=models.TextField(blank=True,null=True)



