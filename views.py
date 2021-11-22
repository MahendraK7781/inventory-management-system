from django.shortcuts import render
from .models import LoginDetails, Employee, Tender,Product,AdminLogin,Vendor,Approve_Vendors,DeliverProducts,Admin_Quotations,Vendor_Quotations,Manager_Vendors
from django.views.generic import View

class AdminLoginCheck(View):
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        type = request.POST.get('type')

        qs = LoginDetails.objects.filter(username=username, password=password, type=type)
        print(qs)
        if not qs:
            return render(request, 'main/login.html', {'message': 'Invalid user'})
        else:
            if type == 'Admin':
                return render(request, 'admin/admin_home.html', {'data': qs})
            elif type == 'Analyzer':
                return render(request, 'analyzer/analyzer_home.html', {'data': qs})
            elif type == 'Area Manager':
                return render(request, 'area manager/areamanager_home.html', {'data': qs})
            elif type == 'Vendor':
                return render(request, 'vendor/vendor_home.html', {'data': qs})

def employee(request):
    qs = Employee.objects.all()
    return render(request, 'admin/employee.html', {'data':qs})

def addEmployee(request):
    idno = request.POST.get('idno')
    username = request.POST.get('username')
    type = request.POST.get('type')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    password = request.POST.get('password')

    Employee(idno=idno,username=username,type=type,contact=contact,email=email,password=password).save()
    LoginDetails(username=username,password=password,type=type).save()
    qs = Employee.objects.all()
    return render(request, 'admin/employee.html', {'message': 'Employee Added', 'data':qs})

def tender(request):
    qs = Tender.objects.all()
    return render(request, 'admin/tender.html', {'data': qs})

def releaseTender(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    product = request.POST.get('product')
    quantity = request.POST.get('quantity')
    release_date = request.POST.get('release_date')
    last_date = request.POST.get('last_date')

    Tender(id=id,title=title,product=product,quantity=quantity,release_date=release_date,last_date=last_date).save()
    qs = Tender.objects.all()
    return render(request, 'admin/tender.html', {'message': 'Tender Released', 'data':qs})


def viewAdminProfile(request):
    qs = AdminLogin.objects.all()
    return render(request, 'admin/view_admin_profile.html', {'data':qs})


def product(request):
    qs = Product.objects.all()
    qs1 = Vendor.objects.all()
    return render(request, 'vendor/product.html', {'data':qs, 'data1':qs1})

def addProduct(request):
    product_id = request.POST.get('product_id')
    product_name = request.POST.get('product_name')
    product_description = request.POST.get('description')
    vendor_id = request.POST.get('vendorid')

    Product(product_id=product_id,product_name=product_name,Product_description=product_description,vendor_id=vendor_id).save()
    qs = Product.objects.all()
    qs1 = Vendor.objects.all()
    return render(request, 'vendor/product.html', {'message': 'Product Added', 'data':qs, 'data1':qs1})

def updateAdminProfile(request):
    qs = AdminLogin.objects.all()
    return render(request, 'admin/update_admin_profile.html', {'data': qs})


def updateAdmin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    type = request.POST.get('type')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    address = request.POST.get('address')

    AdminLogin(username=username,password=password,type=type,contact=contact,email=email,address=address).save()
    return render(request, 'admin/admin_home.html')


def changeAdminPassword(request):
    qs = AdminLogin.objects.all()
    return render(request, 'admin/change_admin_password.html', {'data':qs})


def confirmPassword(request):
    username = request.POST.get('username')
    contact = request.POST.get('contact')
    type = request.POST.get('type')
    email = request.POST.get('email')
    address = request.POST.get('address')
    oldpassword = request.POST.get('oldpassword')
    newpassword = request.POST.get('newpassword')
    confirmpassword = request.POST.get('confirmpassword')

    qs1 = AdminLogin.objects.all()
    if newpassword == confirmpassword:
        AdminLogin(username=username,password=confirmpassword,type=type,contact=contact,email=email,address=address).save()
        LoginDetails(username=username,password=confirmpassword,type=type).save()
        return render(request, 'main/login.html', {'message': "Successfully Changed Admin Password"})
    else:
        return render(request, 'admin/change_admin_password.html', {'message': "New Password and Confirm Password Didn't Match", 'data': qs1})


def addVendors(request):
    return render(request, 'vendor/add_vendor.html')


def saveVendor(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    comp_name = request.POST.get('comp_name')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    address = request.POST.get('address')
    status = 'Pending'

    Approve_Vendors(id=id,name=name,comp_name=comp_name,contact=contact,email=email,address=address,status=status).save()
    return render(request, 'main/login.html', {'message': "Vendor Added Successfully. Use ID as Login Password"})

def deliverProducts(request):
    qs = Tender.objects.all()
    qs1 = Product.objects.all()
    return render(request, 'vendor/deliverproducts.html', {'data':qs, 'data1':qs1})

def deliver(request):
    deliver_id = request.POST.get('deliverid')
    tender_id = request.POST.get('tenderid')
    product_name = request.POST.get('productname')
    print(product_name)
    deliver_date = request.POST.get('deliver_date')

    DeliverProducts(deliver_id=deliver_id,tender_id=tender_id,product_name=product_name,deliver_date=deliver_date).save()
    qs = Tender.objects.all()
    qs1 = Product.objects.all()
    return render(request, 'vendor/deliverproducts.html', {'message': 'Product Delivered', 'data':qs, 'data1':qs1})

def viewVendorProfile(request):
    qs = Vendor.objects.all()
    return render(request,'view_vendor_profile.html',{'data':qs})

def accept_Vendor(request):
    id = request.POST.get('id')
    print(id)
    name = request.POST.get('name')
    comp_name = request.POST.get('comp_name')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    address = request.POST.get('address')
    status = 'Approved'

    Vendor(id=id,name=name,comp_name=comp_name,contact=contact,email=email,address=address,status=status).save()
    Manager_Vendors(id=id,name=name,comp_name=comp_name,contact=contact,email=email,address=address).save()
    Approve_Vendors.objects.filter(id=id).delete()
    LoginDetails(username=name,password=id,type='Vendor').save()

    qs = Approve_Vendors.objects.all()
    return render(request, 'admin/approve_vendors.html', {'object_list':qs, 'message': 'Vendor Accepted'})

def giveQuotation(request):
    qs1 = Tender.objects.all()
    qs2 = Vendor.objects.all()
    return render(request, 'vendor/givequotations.html', {'data1':qs1, 'data2':qs2})

def addQuotations(request):
    qid = request.POST.get('qid')
    tender_id = request.POST.get('tenderid')
    vendor_id = request.POST.get('vendorid')
    required_product = request.POST.get('requiredproduct')
    cost_per_item = request.POST.get('costperitem')
    # supply_date = request.POST.get('supplydate')
    # apply_date = request.POST.get('applydate')
    status = 'Pending'

    Admin_Quotations(qid=qid,tender_id=tender_id,vendor_id=vendor_id,required_product=required_product,cost_per_item=cost_per_item,status=status).save()
    Vendor_Quotations(qid=qid,tender_id=tender_id,vendor_id=vendor_id,required_product=required_product,cost_per_item=cost_per_item,status=status).save()
    qs1 = Tender.objects.all()
    qs2 = Vendor.objects.all()
    return render(request, 'vendor/givequotations.html', {'data1':qs1, 'data2':qs2, 'meesage': 'Quotation Added'})


def viewQuotations(request):
    qs = Vendor_Quotations.objects.all()
    return render(request, 'vendor/viewquotations.html', {'data':qs})


def acceptQuotation(request):
    qid = request.POST.get('qid')
    tender_id = request.POST.get('tenderid')
    vendor_id = request.POST.get('vendorid')
    required_product = request.POST.get('requiredproduct')
    cost_per_item = request.POST.get('costperitem')
    # supply_date = request.POST.get('supplydate')
    # apply_date = request.POST.get('applydate')
    status = 'Accepted'

    Vendor_Quotations(qid=qid,tender_id=tender_id,vendor_id=vendor_id,required_product=required_product,cost_per_item=cost_per_item,status=status).save()
    Admin_Quotations.objects.filter(qid=qid).delete()
    qs = Admin_Quotations.objects.all()
    return render(request, 'admin/adminquotations.html', {'object_list':qs, 'message': "Quotation Accepted"})

