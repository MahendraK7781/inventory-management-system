"""Smart_Inventory_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView, ListView, CreateView
from app.models import Employee, Tender, Vendor,Admin_Quotations,Vendor_Quotations,Payment,Approve_Vendors,DeliverProducts,Inwards
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='main/home.html')),
    path('login/',TemplateView.as_view(template_name='main/login.html')),
    path('loginadmin/',views.AdminLoginCheck.as_view()),
    path('employee/',views.employee),
    path('addemployee/',views.addEmployee),
    path('viewemployee<int:pk>/', DetailView.as_view(template_name='admin/viewemployee.html', model=Employee)),
    path('updateemployee<int:pk>/', UpdateView.as_view(template_name='admin/updateemployee.html', model=Employee, fields=['username', 'type', 'contact', 'email', 'password'], success_url='/employee/')),
    path('deleteemployee<int:pk>/', DeleteView.as_view(template_name='admin/deleteemployee.html', model=Employee, success_url='/employee/')),
    path('tender/',views.tender),
    path('releasetender/',views.releaseTender),
    path('viewtender<int:pk>/', DetailView.as_view(template_name='admin/viewtender.html', model=Tender)),
    path('updatetender<int:pk>/', UpdateView.as_view(template_name='admin/updatetender.html', model=Tender, fields='__all__', success_url='/tender/')),
    path('deletetender<int:pk>/', DeleteView.as_view(template_name='admin/deletetender.html', model=Tender, success_url='/tender/')),
    path('employeereports/', ListView.as_view(template_name='admin/employee_reports.html', model=Employee)),
    # path('newvendor/',CreateView.as_view(template_name='vendor.html',model=Vendor,fields='__all__',success_url='/login/')),
    path('vendorreports/', ListView.as_view(template_name='vendor/vendor_reports.html', model=Vendor)),
    path('approvevendors/', ListView.as_view(template_name='admin/approve_vendors.html', model=Approve_Vendors)),
    path('newvendor/',views.addVendors),
    path('savevendor/',views.saveVendor),
    # path('inwardsreports/',ListView.as_view(template_name='inwardsreports.html',model=Inwards)),
    path('paymentreports/', ListView.as_view(template_name='admin/adminpaymentreports.html', model=Payment)),
    path('viewprofile/',views.viewAdminProfile),
    path('viewtenders/', ListView.as_view(template_name='vendor/viewtenders.html', model=Tender)),
    path('aboutus/', TemplateView.as_view(template_name='main/about_us.html')),
    path('contactus/', TemplateView.as_view(template_name='main/contact_us.html')),
    path('viewalltenders/', ListView.as_view(template_name='main/viewalltenders.html', model=Tender)),
    path('viewanalyzer/',DetailView),
    # path("quotationreports/",ListView.as_view(template_name='quotationreports.html',model=Quotations)),
    path('product/',views.product),
    path('addproduct/',views.addProduct),
    path('viewprofile/',views.viewAdminProfile),
    path('updateprofile/',views.updateAdminProfile),
    path('updateadmin/',views.updateAdmin),
    path('changeadminpassword/',views.changeAdminPassword),
    path('changepass/',views.confirmPassword),
    path('deliverproducts/',views.deliverProducts),
    path('deliver/',views.deliver),
    path('vendorprofile/',views.viewVendorProfile),
    path('rejectvendor<int:pk>/', DeleteView.as_view(template_name='admin/rejectvendor.html', model=Approve_Vendors, success_url='/approvevendors/')),
    path('acceptvendor/',views.accept_Vendor),
    path('areamanagervendorreports/', ListView.as_view(template_name='area manager/area_manager_vendor_reports.html', model=Vendor)),
    path('viewdeliveredproducts/', ListView.as_view(template_name='vendor/viewdeliveredproducts.html', model=DeliverProducts)),
    path('amdeliveredproducts/', ListView.as_view(template_name='area manager/amdeliveredproducts.html', model=DeliverProducts)),
    # path('quotations/',views.quotations),
    # path('quotationmanagement/',TemplateView.as_view(template_name='quotation_management.html')),
    path('givequotation/',views.giveQuotation),
    path('addquotation/',views.addQuotations),
    path('viewquotations/',views.viewQuotations),
    path('quotations/', ListView.as_view(template_name='admin/adminquotations.html', model=Admin_Quotations)),
    path('rejectquotation<int:pk>/', DeleteView.as_view(template_name='admin/rejectquotation.html', model=Admin_Quotations, success_url='/quotations/')),
    path('acceptquotation/',views.acceptQuotation),
    path('makepayment/', CreateView.as_view(template_name='area manager/makepayment.html', model=Payment, fields='__all__', success_url='/makepayment/')),
    path('analyzerreports/', TemplateView.as_view(template_name='analyzer/analyzer_reports_menu.html')),
    path('analyzerquotationreports/', ListView.as_view(template_name='analyzer/analyzer_quotations.html', model=Admin_Quotations)),
    path('analyzerdeliverablereports/', ListView.as_view(template_name='analyzer/analyzer_deliverable.html', model=DeliverProducts)),
    path('venodorviewpayments/', ListView.as_view(template_name='vendor/vendorpayments.html', model=Payment)),
    path('inwardsreports/', ListView.as_view(template_name='admin/inwardsreports.html', model=DeliverProducts)),
]

