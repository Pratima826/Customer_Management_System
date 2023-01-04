from django.shortcuts import render
from django.http import HttpResponse
from CMS.models import Customer
from .forms import CustomerForm

# Create your views here.


def view_cms(request):
    if request.method == 'GET':
        return render(request, 'CMS/cms.html')
    elif request.method == 'POST':
        if 'btnadd' in request.POST:
            cus = Customer()
            cus.name = request.POST.get('txtname', 'NA')
            cus.address = request.POST.get('txtaddress', 'NA')
            cus.age = int(request.POST.get('txtage', 'NA'))
            cus.mobileno = request.POST.get('txtmob', 'NA')
            cus.save()
            return HttpResponse("<h2>Customer Added Successfully with ID !!"+str(cus.id)+"</h2>")
        elif 'btnsearch' in request.POST:
            cusid = int(request.POST.get('cusid', 0))
            cus = Customer.objects.get(id=cusid)
            dict = {'cus': cus}
            return render(request, 'CMS/cms.html', context=dict)
        elif 'btnupdate' in request.POST:
            cus = Customer()
            cus.id = int(request.POST.get('cusid', 0))
            if Customer.objects.filter(id=cus.id):
                cus.name = request.POST.get('txtname', 'NA')
                cus.address = request.POST.get('txtaddress', 'NA')
                cus.age = int(request.POST.get('txtage', 'NA'))
                cus.mobileno = request.POST.get('txtmob', 'NA')
                cus.save()
                return HttpResponse("<h2>Customer Updated Successfully with ID !!"+str(cus.id)+"</h2>")
        elif 'btndelete' in request.POST:
            cus = Customer()
            cus.id = int(request.POST.get('cusid', 0))
            Customer.objects.filter(id=cus.id).delete()
            return HttpResponse("<h2>Customer Deleted Successfully with ID !!"+str(cus.id)+"</h2>")
        elif 'btnshow' in request.POST:
            cus_all = Customer.objects.all()
            dict = {'show': cus_all}
            return render(request, 'CMS/cms.html', context=dict)

def view_customer(request):
    if request.method=='GET':
        frm_unbound=CustomerForm()
        d1={'forms':frm_unbound}
        return render(request,'CMS/cusfrm.html',context=d1)

    elif request.method=='POST':
        frm_bound=CustomerForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse('<h1>Customer Added Successfully</h1>')



