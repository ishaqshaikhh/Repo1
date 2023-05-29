from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Zimmedari = (
    ("Alaqa Zimmedar Naik Aamal","Alaqa Zimmedar Naik Aamal"),
    ("District Zimmedar Naik Aamal","District Zimmedar Naik Aamal"),
    ("Division Zimmedar Naik Aamal","Division Zimmedar Naik Aamal"),
    ("State Zimmedar Naik Aamal","State Zimmedar Naik Aamal"),
    ("Region Zimmedar Naik Aamal","Region Zimmedar Naik Aamal"),
    ("Hind Zimmedar Naik Aamal","Hind Zimmedar Naik Aamal"),
    ("Other Zimmedar","Other Zimmedar"),
)


class Region(models.Model):
    region_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.region_name)


class State(models.Model):
    region_namef = models.ForeignKey(Region, on_delete=models.CASCADE,default="")
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.state_name)


class Division(models.Model):
    state_namef = models.ForeignKey(State, on_delete=models.CASCADE,default="")
    division_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.division_name)

class District(models.Model):
    division_namef = models.ForeignKey(Division, on_delete=models.CASCADE,default="")
    district_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.district_name)


class Zimmedar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    zehliHalqa = models.CharField(max_length=200) 
    alaqa = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Report(models.Model):
    zimmedar = models.ForeignKey(User, on_delete=models.CASCADE)
    zimmedar_name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    zimmedari = models.CharField(choices=Zimmedari,default='madinah',max_length=50)
    alaqa = models.CharField(max_length=100,)
    disrict = models.ForeignKey(District, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    taqseem = models.BigIntegerField(max_length=100000)
    wusool = models.BigIntegerField(max_length=100000)
    islaheaamal_ijtima_maqam = models.BigIntegerField(max_length=10000)
    islaheaamal_ijtima_shuraqa = models.BigIntegerField(max_length=10000)
    tahajjud_ijtima_maqam = models.BigIntegerField(max_length=10000)
    tahajjud_ijtima_shuraqa = models.BigIntegerField(max_length=10000)
    sehri_ijtima_maqam = models.BigIntegerField(max_length=10000)
    sehri_ijtima_shuraqa = models.BigIntegerField(max_length=10000)
    mehboob_e_attar = models.BigIntegerField(max_length=10000)
    yaumequfle_madinah = models.BigIntegerField(max_length=10000)
    haftawar_ijtima_main_raat_guzarne_wale_Shuraqa = models.BigIntegerField(max_length=100000)

    
    def __str__(self):
        return str(self.id)