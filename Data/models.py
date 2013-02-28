from django.db import models

# Create your models here.

class TestCase(models.Model):
    test_id= models.AutoField(primary_key=True);
#    test_name= models.TextField(max_length=400);
    test_path= models.TextField(max_length=100,null=True);
    test_area= models.CharField(max_length=100,null=True);
    suite=models.CharField(max_length=100,null=True);
    swfName=models.CharField(max_length=100,null=True);
#    mainArea=models.CharField(max_length=100,null=True);
#    isAir = models.NullBooleanField(default=False);
#    section_id= models.CharField(max_length=100);
    test_caseid = models.IntegerField();
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
#    last_pass=models.DateField();
#    last_fail=models.DateField();
    deleted_flag=models.NullBooleanField(default=False);
    def primary_key(self):
        return self.test_id
    def __unicode__(self):
        return self.swfName

