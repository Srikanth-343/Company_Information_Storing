from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from webapp.forms import companyForm
from webapp.models import Company_detailes

from django.urls import reverse_lazy
# Create your views here.

def Home(request):
    return render(request,'base.html')



def companyModelView(request):
    if request.method == 'POST':
        form=companyForm(request.POST)
        if form.is_valid():
            cf=form.cleaned_data['Company']
            df=form.cleaned_data['Division']
            sf=form.cleaned_data['Sector']
            pf=form.cleaned_data['Phone']
            ff=form.cleaned_data['Fax']
            gf=form.cleaned_data['Website']
            aa = form.cleaned_data['Industry']
            ab = form.cleaned_data['NAICS_codes']
            ac = form.cleaned_data['Revenue']
            ad = form.cleaned_data['EstimatedPayroll']
            ae = form.cleaned_data['Number_of_Employees']
            af = form.cleaned_data['Number_of_Internal_Employees']
            ag = form.cleaned_data['Number_of_consultants_on_OPT']
            ah = form.cleaned_data['Number_of_consultants_on_CPT']
            ai = form.cleaned_data['Number_of_consultants_on_H1B']
            aj = form.cleaned_data['Number_of_card_consultants']
            ak = form.cleaned_data['Number_of_US_Citizens']
            al = form.cleaned_data['Number_of_consultants_on_other_visa']
            am = form.cleaned_data['AddressLine1']
            an = form.cleaned_data['AddressLine2']
            ao = form.cleaned_data['City']
            ap = form.cleaned_data['State']
            aq = form.cleaned_data['Zipcode']
            ar = form.cleaned_data['FederalID_EIN']
            au = form.cleaned_data['GST_Number']
            at = form.cleaned_data['AddadditionalInformation']

            reg = Company_detailes(Company=cf, Division=df, Sector=sf,Website=gf,
                               Phone=pf, Fax=ff,Industry=aa,NAICS_codes=ab,Revenue=ac,EstimatedPayroll=ad,Number_of_Employees=ae,Number_of_Internal_Employees=af,
                                   Number_of_consultants_on_OPT=ag,Number_of_consultants_on_CPT=ah,Number_of_consultants_on_H1B=ai,Number_of_card_consultants=aj,Number_of_US_Citizens=ak,Number_of_consultants_on_other_visa=al,
                                   AddressLine1=am,AddressLine2=an,City=ao,State=ap,Zipcode=aq,FederalID_EIN=ar,GST_Number=au,AddadditionalInformation=at,
                               )
            reg.save()
            form = companyForm()
    else:
        form =companyForm()
    studs=Company_detailes.objects.all()
    return render(request, 'Table_creation.html', {'form':form,'stud':studs})

def edit_Company(request, id):
    if request.method == 'POST':
        comp=Company_detailes.objects.get(pk=id)
        form=companyForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
    else:
        comp = Company_detailes.objects.get(pk=id)
        form = companyForm(instance=comp)
    return render(request,'update.html',{'form':form})




def delete_Company(request, id):
    if request.method=='POST':
        comp=Company_detailes.objects.get(pk=id)
        comp.delete()
        return HttpResponseRedirect('/')
