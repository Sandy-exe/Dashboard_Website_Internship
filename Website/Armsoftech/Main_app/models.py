from django.db import models

# Create your models here.
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class FinalOutput(models.Model):
    unique_names = models.TextField(db_column='Unique_Names', blank=True, null=True)  # Field name made lowercase.
    jul_23 = models.IntegerField(db_column='Jul_23', blank=True, null=True)  # Field name made lowercase.
    jun_23 = models.IntegerField(db_column='Jun_23', blank=True, null=True)  # Field name made lowercase.
    may_23 = models.IntegerField(db_column='May_23', blank=True, null=True)  # Field name made lowercase.
    total_repeat = models.IntegerField(db_column='Total_repeat')  # Field name made lowercase.
    paid_times = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'final_output'


class Main(models.Model):
    account = models.TextField(db_column='Account', blank=True, null=True)  # Field name made lowercase.
    data_validation = models.TextField(db_column='Data_Validation', blank=True, null=True)  # Field name made lowercase.
    phone1 = models.TextField(db_column='PHONE1', blank=True, null=True)  # Field name made lowercase.
    emi_amount = models.TextField(db_column='EMI_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    cyle_date = models.TextField(db_column='CYLE_DATE', blank=True, null=True)  # Field name made lowercase.
    due_date = models.TextField(db_column='DUE_DATE', blank=True, null=True)  # Field name made lowercase.
    product = models.TextField(db_column='PRODUCT', blank=True, null=True)  # Field name made lowercase.
    zone = models.TextField(db_column='ZONE', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    finl_risk = models.TextField(db_column='FINL_RISK', blank=True, null=True)  # Field name made lowercase.
    language_1 = models.TextField(db_column='Language_1', blank=True, null=True)  # Field name made lowercase.
    language_2 = models.TextField(db_column='Language_2', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    callstatus = models.TextField(db_column='CallStatus', blank=True, null=True)  # Field name made lowercase.
    finalstatus = models.TextField(db_column='FinalStatus', blank=True, null=True)  # Field name made lowercase.
    finalcallduration = models.TextField(db_column='FinalCallduration', blank=True, null=True)  # Field name made lowercase.
    noofattempt = models.TextField(db_column='NoOfAttempt', blank=True, null=True)  # Field name made lowercase.
    noofconnect = models.TextField(db_column='NoOfConnect', blank=True, null=True)  # Field name made lowercase.
    paid_status = models.TextField(db_column='Paid_Status', blank=True, null=True)  # Field name made lowercase.
    paid_date = models.TextField(db_column='Paid_Date', blank=True, null=True)  # Field name made lowercase.
    allocation_date = models.TextField(db_column='Allocation_Date', blank=True, null=True)  # Field name made lowercase.
    month = models.TextField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    product_sort = models.TextField(db_column='PRODUCT Sort', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_type = models.TextField(db_column='PRODUCT TYPE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_product = models.TextField(db_column='Sub Product', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'main'


class Card_data(models.Model):
    id = models.BigAutoField(primary_key=True)
    allocation = models.IntegerField(blank=True, null=True)
    connect_percentage = models.FloatField(blank=True, null=True)
    paid_count = models.IntegerField(blank=True, null=True)
    resolution_percentage = models.FloatField(blank=True, null=True)
    avg_attempt_intensity = models.FloatField(blank=True, null=True)
    avg_connect_intensity = models.FloatField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'Card_data'


class Connect_by_Month(models.Model):
    id= models.BigAutoField(primary_key=True)
    Month = models.CharField(max_length=255, blank=True, null=True)
    Connect_percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Connect_by_Month'

class my_table(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.CharField(max_length=30, blank=True, null=True)
    data_validation = models.CharField(max_length=30, blank=True, null=True)
    phone1 = models.CharField(max_length=30, blank=True, null=True)
    emi_amount = models.CharField(max_length=30, blank=True, null=True)
    pos = models.CharField(max_length=30, blank=True, null=True)
    cyle_date = models.CharField(max_length=30, blank=True, null=True)
    due_date = models.CharField(max_length=30, blank=True, null=True)
    product = models.CharField(max_length=30, blank=True, null=True)
    zone = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    finl_risk = models.CharField(max_length=30, blank=True, null=True)
    language_1 = models.CharField(max_length=30, blank=True, null=True)
    language_2 = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    callstatus = models.CharField(max_length=30, blank=True, null=True)
    finalstatus = models.CharField(max_length=30, blank=True, null=True)
    finalcallduration = models.CharField(max_length=30, blank=True, null=True)
    noofattempt = models.IntegerField(blank=True, null=True)
    noofconnect = models.IntegerField(blank=True, null=True)
    paid_status = models.CharField(max_length=30, blank=True, null=True)
    paid_date = models.CharField(max_length=30, blank=True, null=True)
    allocation_date = models.CharField(max_length=30, blank=True, null=True)
    month = models.CharField(max_length=30, blank=True, null=True)
    product_sort = models.CharField(db_column='PRODUCT Sort', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_type = models.CharField(db_column='PRODUCT TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_product = models.CharField(db_column='Sub Product', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'my_table'