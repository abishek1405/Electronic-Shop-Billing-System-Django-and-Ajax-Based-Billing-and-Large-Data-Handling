from django.db import models




class plistManager(models.Manager):
    pass


class productlist(models.Model):
    product = models.CharField(max_length=200)
    qty = models.CharField(max_length=100)
    rate = models.CharField(max_length=20)

    objects = plistManager()

    class Meta:
        abstract = True

class ElectricProduct(productlist):
    pass

class PlumbingProduct(productlist):
    pass

class HardwareProduct(productlist):
    pass


    
class billcal(models.Model):
    total = models.CharField(max_length=50)
    discount = models.CharField(max_length=50)
    todiscount = models.CharField(max_length=50)
    amount = models.CharField(max_length = 50)

class partcal(models.Model):
    btotal = models.CharField(max_length=40)
    bdiscount = models.CharField(max_length=40)
    btodiscount = models.CharField(max_length=40)
    bamount = models.CharField(max_length = 40)

class billone(models.Model):
    oneprod = models.CharField(max_length=100)
    oneqty = models.CharField(max_length=100)
    onenoq = models.CharField(max_length=100)
    onerate = models.CharField(max_length=100)
    onepra = models.CharField(max_length=100)

    

class billper(models.Model):
    dddat = models.CharField(max_length = 1000)
    tttim = models.CharField(max_length = 1000)
    proddd = models.CharField(max_length=1000)
    qqty = models.CharField(max_length=1500)
    nofqty = models.CharField(max_length=1000)
    perp = models.CharField(max_length=700)
    rrate = models.CharField(max_length=1000)
    teto = models.CharField(max_length=1000)
    dedis = models.CharField(max_length=700)
    tetodis = models.CharField(max_length=700)
    dakad =  models.CharField(max_length=1000)
    ssnumm = models.CharField(max_length=1000)

class part(models.Model):
    product = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    noqty = models.CharField(max_length=60)
    rate = models.CharField(max_length=100)
    toqrate = models.CharField(max_length=100)
    peccen = models.CharField(max_length=100)
    come = models.CharField(max_length=100)
    totalfee = models.CharField(max_length=100)


class partper(models.Model):
    datt = models.CharField(max_length = 1000)
    timm = models.CharField(max_length = 1000)
    bproduct = models.CharField(max_length=1050)
    bqty = models.CharField(max_length=1000)
    borr = models.CharField(max_length=1000)
    bnofq = models.CharField(max_length=1000)
    brate = models.CharField(max_length=1000)
    bper = models.CharField(max_length=1000)
    bcfee = models.CharField(max_length=1000)
    btfee = models.CharField(max_length=1000)
    btotal = models.CharField(max_length=1000)
    bdis = models.CharField(max_length=1000)
    btodisp = models.CharField(max_length=1000)
    bkad =  models.CharField(max_length=1000)
    bnumm = models.CharField(max_length=1500)



class Billing(models.Model):
    party_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    no_of_product = models.IntegerField()
    value = models.CharField(max_length=100)  # Adjusted precision value
    rate_per_piece = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)


class MyModel(models.Model):
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)




class mytiger(models.Model):
    name1 = models.CharField(max_length=1000)
    name2 = models.CharField(max_length=1000)
    name3 = models.CharField(max_length=1000)
    name4 = models.CharField(max_length=1000)
    name5 = models.CharField(max_length=1000)
    name6 = models.CharField(max_length=1000)
    name7 = models.CharField(max_length=1000)
    name8 = models.CharField(max_length=1000)
    name9 = models.CharField(max_length=1000)
    name10 = models.CharField(max_length=100)
    name11 = models.CharField(max_length=1000)
    name12 = models.CharField(max_length=1000)
    name13 = models.CharField(max_length=1000)