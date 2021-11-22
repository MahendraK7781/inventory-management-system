from django.db import models

class AdminLogin(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=(('Admin', 'admin'), ('Area Manager', 'area manager'), ('Analyzer', 'analyzer'), ('Vendor', 'vendor')))
    contact = models.IntegerField()
    email = models.EmailField(max_length=30)
    address = models.TextField()


class LoginDetails(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=30,choices=(('Admin','admin'),('Area Manager','area manager'),('Analyzer','analyzer'),('Vendor','vendor')))

    def __str__(self):
        return self.username

class Employee(models.Model):
    idno = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30,default=False)
    type = models.CharField(max_length=30,choices=(('Area Manager','area manager'),('Analyzer','analyzer'),('Vendor','vendor')),default=False)
    contact = models.IntegerField()
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

class Tender(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    product = models.CharField(max_length=20,choices=(('samsung','SAMSUNG'),('oppo','OPPO'),('vivo','VIVO'),('mi','MI'),('oneplus','ONEPLUS')))
    quantity = models.IntegerField()
    release_date = models.DateField()
    last_date = models.DateField()

    def __str__(self):
        return str(self.id)

class Vendor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    comp_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=20)
    address = models.TextField()
    status = models.CharField(max_length=20,default=False)

    def __str__(self):
        return str(self.id)
class Manager_Vendors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    comp_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=20)
    address = models.TextField()


class Admin_Quotations(models.Model):
    qid = models.IntegerField(primary_key=True)
    tender_id = models.IntegerField()
    vendor_id = models.IntegerField()
    required_product = models.CharField(max_length=20)
    cost_per_item = models.DecimalField(max_digits=10,decimal_places=2)
    # supply_date = models.DateField()
    # apply_date = models.DateField()
    status = models.CharField(max_length=30,default=False)

class Vendor_Quotations(models.Model):
    qid = models.IntegerField(primary_key=True)
    tender_id = models.IntegerField()
    vendor_id = models.IntegerField()
    required_product = models.CharField(max_length=20)
    cost_per_item = models.DecimalField(max_digits=10,decimal_places=2)
    # supply_date = models.DateField()
    # apply_date = models.DateField()
    status = models.CharField(max_length=30)

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=30)
    Product_description = models.TextField(max_length=500)
    vendor_id = models.IntegerField()

    def __str__(self):
        return self.product_name

class DeliverProducts(models.Model):
    deliver_id = models.IntegerField(primary_key=True)
    tender_id = models.IntegerField()
    product_name = models.CharField(max_length=30)
    deliver_date = models.DateField()

    def __str__(self):
        return str(self.deliver_id)

class Inwards(models.Model):
    delivery_Id = models.IntegerField(primary_key=True)
    tender_idno = models.ForeignKey(Tender,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=False)
    delivery_date = models.DateField()
    status = models.CharField(max_length=20)

class Payment(models.Model):
    payment_Id = models.IntegerField(primary_key=True)
    deliver_idno = models.ForeignKey(DeliverProducts,on_delete=models.CASCADE)
    tender_idno = models.ForeignKey(Tender,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=False)
    payment_date = models.DateField()

class Approve_Vendors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    comp_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=20)
    address = models.TextField()
    status = models.CharField(max_length=20)
