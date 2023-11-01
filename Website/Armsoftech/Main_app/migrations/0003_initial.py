# Generated by Django 4.2.6 on 2023-10-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Main_app', '0002_delete_modelformysql_delete_modelforsqlite'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FinalOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_names', models.TextField(blank=True, db_column='Unique_Names', null=True)),
                ('jul_23', models.IntegerField(blank=True, db_column='Jul_23', null=True)),
                ('jun_23', models.IntegerField(blank=True, db_column='Jun_23', null=True)),
                ('may_23', models.IntegerField(blank=True, db_column='May_23', null=True)),
                ('total_repeat', models.IntegerField(db_column='Total_repeat')),
                ('paid_times', models.IntegerField()),
            ],
            options={
                'db_table': 'final_output',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.TextField(blank=True, db_column='Account', null=True)),
                ('data_validation', models.TextField(blank=True, db_column='Data_Validation', null=True)),
                ('phone1', models.TextField(blank=True, db_column='PHONE1', null=True)),
                ('emi_amount', models.TextField(blank=True, db_column='EMI_AMOUNT', null=True)),
                ('pos', models.TextField(blank=True, db_column='POS', null=True)),
                ('cyle_date', models.TextField(blank=True, db_column='CYLE_DATE', null=True)),
                ('due_date', models.TextField(blank=True, db_column='DUE_DATE', null=True)),
                ('product', models.TextField(blank=True, db_column='PRODUCT', null=True)),
                ('zone', models.TextField(blank=True, db_column='ZONE', null=True)),
                ('state', models.TextField(blank=True, db_column='STATE', null=True)),
                ('finl_risk', models.TextField(blank=True, db_column='FINL_RISK', null=True)),
                ('language_1', models.TextField(blank=True, db_column='Language_1', null=True)),
                ('language_2', models.TextField(blank=True, db_column='Language_2', null=True)),
                ('language', models.TextField(blank=True, db_column='Language', null=True)),
                ('callstatus', models.TextField(blank=True, db_column='CallStatus', null=True)),
                ('finalstatus', models.TextField(blank=True, db_column='FinalStatus', null=True)),
                ('finalcallduration', models.TextField(blank=True, db_column='FinalCallduration', null=True)),
                ('noofattempt', models.TextField(blank=True, db_column='NoOfAttempt', null=True)),
                ('noofconnect', models.TextField(blank=True, db_column='NoOfConnect', null=True)),
                ('paid_status', models.TextField(blank=True, db_column='Paid_Status', null=True)),
                ('paid_date', models.TextField(blank=True, db_column='Paid_Date', null=True)),
                ('allocation_date', models.TextField(blank=True, db_column='Allocation_Date', null=True)),
                ('month', models.TextField(blank=True, db_column='Month', null=True)),
                ('product_sort', models.TextField(blank=True, db_column='PRODUCT Sort', null=True)),
                ('product_type', models.TextField(blank=True, db_column='PRODUCT TYPE', null=True)),
                ('sub_product', models.TextField(blank=True, db_column='Sub Product', null=True)),
            ],
            options={
                'db_table': 'main',
                'managed': False,
            },
        ),
    ]
