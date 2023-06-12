from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import productlist,billone,billper,billcal,part,partcal,ElectricProduct,PlumbingProduct,HardwareProduct,Billing,MyModel,mytiger,partper
from .forms import plistforms,billforms,partform
from django.contrib import messages
from django.http import HttpResponse,HttpResponseBadRequest
from django.db.models import Sum
import datetime
import math
from datetime import datetime



#return render (request,'import.html')

def home(request):
    electric_products = ElectricProduct.objects.all()
    plumbing_products = PlumbingProduct.objects.all()
    hardware_products = HardwareProduct.objects.all()

    distinct_values_list_sstore_name = list(electric_products) + list(plumbing_products) + list(hardware_products)

    bii = billone.objects.all()

    total_rate = billone.objects.aggregate(Sum('onerate'))['onerate__sum']
    ddi = total_rate
    dis = 0  

    if request.method == 'POST' and 'dis' in request.POST:
        gg = request.POST['dis']
        ddi = round(float(ddi) - int(gg),2)
        dis = round((total_rate) - float(ddi),2)
        print(ddi)
    if request.method == 'POST':
        sn = request.POST.get('prod', None)
        qy = request.POST.get('qty', None)
        pmul = request.POST.get('rate', None)
        noq = request.POST.get('nqty', None)
        if sn is not None and qy is not None and pmul is not None and noq is not None:
            pap = round(int(qy) * float(pmul),2)
            billone.objects.create(oneprod=sn, oneqty=qy, onerate=pap,onenoq = noq, onepra = pmul)
            return redirect('/')

    return render(request, 'index.html', {'distinct_values_sstore_name': distinct_values_list_sstore_name, 'ket': bii, 'tot': ddi,'dd':dis})

from django.http import JsonResponse

def elec(request):
    if request.method== 'POST':      
        prod  = request.POST['prod']
        if ElectricProduct.objects.filter(product = prod):
            messages.success(request,"Product name that has already been given and stored.")
            return redirect('/elec')
        sn  = request.POST['prod']
        oo = request.POST['qty']
        pap = request.POST['rate']
        ElectricProduct.objects.create(product = sn, qty = oo ,rate =pap)
        return redirect('/elec')
    return render(request,'prolis.html')

def plum(request):
    if request.method== 'POST':
        prod  = request.POST['prod']
        if PlumbingProduct.objects.filter(product = prod):
            messages.success(request,"Product name that has already been given and stored.")
            return redirect('/elec')
        sn  = request.POST['prod']
        oo = request.POST['qty']
        pap = request.POST['rate']
        PlumbingProduct.objects.create(product = sn, qty = oo ,rate =pap)
        return redirect('/plum')
    return render(request,'prolis.html')
    

def hard(request):
    if request.method== 'POST':
        prod  = request.POST['prod']
        if HardwareProduct.objects.filter(product = prod):
            messages.success(request,"Product name that has already been given and stored.")
            return redirect('/elec')
        sn  = request.POST['prod']
        oo = request.POST['qty']
        pap = request.POST['rate']
        HardwareProduct.objects.create(product = sn, qty = oo ,rate =pap)
        return redirect('/hard')
    return render(request,'prolis.html')

def prolis(request):
    if request.method == "POST":
        percentage = 0.0
        if 'eper' in request.POST and request.POST['eper'].strip():
            percentage = float(request.POST['eper'])
            products = ElectricProduct.objects.all()
        elif 'pper' in request.POST and request.POST['pper'].strip():
            percentage = float(request.POST['pper'])
            products = PlumbingProduct.objects.all()
        elif 'hper' in request.POST and request.POST['hper'].strip():
            percentage = float(request.POST['hper'])
            products = HardwareProduct.objects.all()
        else:
            messages.error(request, "Invalid percentage value")
            return redirect('/prolis/')

        for product in products:
            rate = float(product.rate)  # Convert rate to float
            increase_amount = rate * (percentage / 100.0)
            new_rate = rate + increase_amount

            product.rate = round(new_rate,2)
            product.save()

    return render(request, 'coose.html')




def seldail(request):
    electric_products = ElectricProduct.objects.all()
    plumbing_products = PlumbingProduct.objects.all()
    hardware_products = HardwareProduct.objects.all()

    return render(request, 'mas.html',{'elec':electric_products,'plum':plumbing_products,'hard':hardware_products})




def elecup(request, id):
    student = ElectricProduct.objects.get(id=id)
    if request.method== 'POST':
        student.product = request.POST['product']
        student.qty = request.POST['qty']
        student.rate = request.POST['rate']
        student.save()
        return redirect('/proo/')
    return render(request, 'selfup.html',{'student': student})

def plumup(request, id): 
    student = PlumbingProduct.objects.get(id=id)
    if request.method== 'POST':
        student.product = request.POST['product']
        student.qty = request.POST['qty']
        student.rate = request.POST['rate']
        student.save()
        return redirect('/proo/')
    return render(request, 'selfup.html',{'student': student})

def hardup(request, id): 
    student = HardwareProduct.objects.get(id=id)

    if request.method== 'POST':
        student.product = request.POST['product']
        student.qty = request.POST['qty']
        student.rate = request.POST['rate']
        student.save()
        return redirect('/proo/')
    return render(request, 'selfup.html',{'student': student})




def elecde(request, id):
    student = ElectricProduct.objects.get(id=id)
    student.delete()
    
    return redirect('/proo/')

def plumde(request, id):
    student = PlumbingProduct.objects.get(id=id)
    student.delete()
 
    return redirect('/proo/')

def hardde(request, id):
    student = HardwareProduct.objects.get(id=id)
    student.delete()
    
    return redirect('/proo/')






def bget_product_details(request):
    if request.method == 'GET':
        product_names = request.GET.getlist('pro[]')
        print(product_names)
        data = []

        for pro in product_names:
            try:
                product_obj = ElectricProduct.objects.get(product=pro)
            except ElectricProduct.DoesNotExist:
                try:
                    product_obj = PlumbingProduct.objects.get(product=pro)
                except PlumbingProduct.DoesNotExist:
                    try:
                        product_obj = HardwareProduct.objects.get(product=pro)
                    except HardwareProduct.DoesNotExist:
                        continue

            data.append({
                'pro': product_obj.product,
                'qt': product_obj.qty,
                'rat': product_obj.rate
            })
        
        return JsonResponse(data, safe=False)







def get_product_details(request):
    if request.method == 'GET':
        product_names = request.GET.getlist('prod[]')
        print(product_names)
        data = []

        for prod in product_names:
            try:
                product_obj = ElectricProduct.objects.get(product=prod)
            except ElectricProduct.DoesNotExist:
                try:
                    product_obj = PlumbingProduct.objects.get(product=prod)
                except PlumbingProduct.DoesNotExist:
                    try:
                        product_obj = HardwareProduct.objects.get(product=prod)
                    except HardwareProduct.DoesNotExist:
                        # Handle the case where the product is not found
                        continue

            data.append({
                'prod': product_obj.product,
                'qty': product_obj.qty,
                'rate': product_obj.rate
            })
        
        return JsonResponse(data, safe=False)










from django.shortcuts import render, redirect
from .models import part
from .forms import partform

def upb(request, id):
    student = part.objects.get(id=id)
    formdd = partform(instance=student)
 
    if request.method == 'POST':
        formdd = partform(request.POST, instance=student)
        if formdd.is_valid():
            student = formdd.save(commit=False)
            ss = request.POST.get('peccen')
            print(ss)
            sr = request.POST.get('rate')
            qt = request.POST.get('qty')
            ttp =request.POST.get('toqrate')
            erate = round(float(qt) * float(sr),2)
            student.toqrate = erate
            print(ttp)
            percent = round((float(ss) / 100) * float(erate),2)
            student.come = percent
            totalfee = float(erate) + percent
            student.totalfee = totalfee
            student.save()
            return redirect('/bcout')

    return render(request, 'bselforup.html', {'form': formdd})


def billed(request, id):
    student = productlist.objects.all()   
    bii = part.objects.all()
    total_rate = part.objects.aggregate(Sum('tfee'))['tfee__sum']
    ddi = total_rate

    total_com = part.objects.aggregate(Sum('dpe'))['dpe__sum']
    dpe = total_com

    dis = 0  

    if request.method == 'POST' and 'dis' in request.POST:
        gg = request.POST['dis']
        ddi = int(ddi) - int(gg)
        dis = int(total_rate) - int(ddi)
        print(ddi)

    if request.method == 'POST' and bool(request.POST['qt']):
        # formdd = billforms2(request.POST)
        # if formdd.is_valid():
        sn = request.POST['pro']
        qy = request.POST['qt']
        pap = request.POST['rat']
        trt = request.POST['pec']
        dper = (int(trt)/100)*int(pap)
        tof = int(dper)+ int(pap)
        part.objects.create(pro=sn, qt=qy, rat=pap, pec = trt,dpe = dper,tfee = tof)
        return redirect('/bill2')
    
    return render(request, 'bselforup.html', {'ket': bii, 'tot': ddi,'dd':dis,'dpe':dpe})






def dall(request):
    billone.objects.all().delete()
    billcal.objects.all().delete()
    return redirect('/')

def bdall(request):
    part.objects.all().delete()
    partcal.objects.all().delete()
    return redirect('/bill2')

from django.utils.dateparse import parse_datetime
 


def overalldel(request,id):
    student = Billing.objects.get(id=id)
    student.delete()
    return redirect('/list')


def billing_form(request):
    firstname = request.POST.get('firstname', '')  # Retrieve the value from request.POST
    cont = request.POST.get('address')
    payment = request.POST.get('payment')
    if request.method == 'POST':
        try:
            party_name = request.POST.get('firstname')
            product_name = request.POST.get('cardname')
            contact_number = request.POST.get('address')
            no_of_product = request.POST.get('expyear')
            value = request.POST.get('nqty')
            rate_per_piece = request.POST.get('state')
            payment_method = request.POST.get('payment')
            rate = round(float(no_of_product) * float(rate_per_piece), 2)

            if not payment_method:  # If payment_method is not provided, set a default value
                payment_method = "Not specified"

            billing = Billing(
                party_name=party_name,
                product_name=product_name,
                contact_number=contact_number,
                no_of_product=no_of_product,
                value=value,
                rate_per_piece=rate_per_piece,
                payment_method=payment_method,
                rate=rate
            )
            billing.save()

            return render(request, 'overall.html', {'firstname': firstname, 'cont':cont,'payment':payment})
        except:
            return redirect('/eror')

    return render(request, 'overall.html', {'firstname': firstname})


def stockout(request):
    firstname = request.POST.get('firstname', '')  # Retrieve the value from request.POST
    cont = request.POST.get('address')
    payment = request.POST.get('payment')
    if request.method == 'POST':
        party_name = request.POST.get('firstname')
        product_name = 'nill'
        contact_number = request.POST.get('address')
        no_of_product = '0'
        payment_method = request.POST.get('payment')
        value = '-'
        rate_per_piece = request.POST.get('state')
        rate = rate_per_piece
        billing = Billing(
            party_name=party_name,
            product_name=product_name,
            contact_number=contact_number,
            no_of_product='0',
            value=value,
            rate_per_piece='0',
            payment_method=payment_method,
            rate= -int(rate)
        )
        billing.save()
    return render(request, 'stockout.html', {'firstname': firstname, 'cont':cont,'payment':payment})


def newbil(request):
    Billing.objects.all().delete()
    return redirect('/stock')



def tigall(request):
    mytiger.objects.all().delete()
    return redirect('/totout')



def rodel(request, id):
    student = mytiger.objects.get(id=id)
    student.delete()
    return redirect('/totout')




def out(request):
    total_com = mytiger.objects.aggregate(Sum('name11'))['name11__sum']
    if bool(total_com):
        dpe = round(total_com,2)
    else:
        dpe = 0
    tttout = mytiger.objects.filter().order_by('-name12')
    values = []

    ototal = 0
    mtotal= 0

    for obj in tttout:
        names = obj.name3.split(', ')
        if names:
            values.append(names[0])

        if obj.name11:
            try:
                name11_value = float(obj.name11)
                if name11_value > 0:
                    ototal += round(name11_value,2)
            except ValueError:
                pass
        if obj.name11:
            try:
                name11_value = float(obj.name11)
                if name11_value < 0:
                    mtotal += name11_value
            except ValueError:
                pass

    return render(request, 'totout.html', {'ket': tttout, 'first_value': values, 'tkad': dpe, 'ototal': ototal,'mtotal':mtotal})

















def billing_list(request):
   
    current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M')
    formatted_date_time = current_datetime.replace("T", " ")
    billing_data = Billing.objects.all()
    total_rate = Billing.objects.aggregate(Sum('rate'))['rate__sum']
    gsty = request.POST.get('gst', '')

    if gsty:
        try:
            gst_float = float(gsty)
        except ValueError:
            return HttpResponse("Invalid value for GST")

        gst = (float(gst_float) / 100) * total_rate
        tot_gst = round(total_rate + gst, 2)
    else:
        gst = 0.0
        tot_gst = total_rate

    if 'save' in request.POST and total_rate is not None:
        MyModel.objects.all().delete()
        names1 = [bill.party_name for bill in Billing.objects.all()]
        names1_str = ", ".join(names1)
        names2 = [bill.product_name for bill in Billing.objects.all()]
        names2_str = ", ".join(names2)
        names3 = [bill.contact_number for bill in Billing.objects.all()]
        names3_str = ", ".join(names3)
        names4 = [bill.no_of_product for bill in Billing.objects.all()]
        names4_str = ", ".join(str(name) for name in names4)

        names5 = [bill.value for bill in Billing.objects.all()]
        names5_str = ", ".join(names5)
        names6 = [bill.rate_per_piece for bill in Billing.objects.all()]
        names6_str = ", ".join(names6)
        names7 = [bill.payment_method for bill in Billing.objects.all()]
        names7_str = ", ".join(names7)
        names8 = [bill.rate for bill in Billing.objects.all()]
        names8_str = ", ".join(names8)
        print(tot_gst)
        if tot_gst < 0:
            names13 = 'PAYMENT OUT'
        else:
            names13 = 'PURCHASE'
        MyModel.objects.create(field2=round(total_rate,2), field3=round(gst,2), field4=round(tot_gst,2))
        mytiger.objects.create(name1=names1_str, name2=names2_str, name3=names3_str, name4=names4_str, name5=names5_str, name6=names6_str, name7=names7_str, name8=names8_str, name9=round(total_rate,2), name10=round(gst,2), name11=round(tot_gst,2),name12 = formatted_date_time,name13 = names13)

    return render(request, 'overallout.html', {'billing_data': billing_data, 'tot': total_rate, 'gst': gst, 'tot_gst': tot_gst, 'current_date': formatted_date_time})




# def filter_by_amount_view(request):
#     context = {'billing_data': Billing.objects.order_by('rate')}
#     return render(request, 'overallout.html', context)
   


# def filter_by_date_view(request):
#     context = {'billing_data': Billing.objects.order_by('-date')}
#     return render(request, 'overallout.html', context)







def calculate_discounted_amount(total_amount, gg):
    discount_amount = (gg / 100) * total_amount
    #discounted_amount = total_amount - discount_amount
    return discount_amount

def cout(request):
    kjkk = billcal.objects.all()
    total_rate = billone.objects.aggregate(Sum('onerate'))['onerate__sum']
    if bool(total_rate):
        ddi = round(total_rate,2)
    else:
        ddi = 0
    dis = 0

    fdf = billone.objects.all()
    billcal.objects.all().delete()
    global kadan
    if request.method == 'POST' and 'dis' in request.POST and bool(ddi):
        gg = request.POST['dis'] or 0
        #dis = int(total_rate) - int(ddi)
        discounted_amount = calculate_discounted_amount(total_rate, int(gg))
        print(discounted_amount)
        dis = round(discounted_amount,2)
        ddi = float(ddi) - float(dis)
        names = [bill.oneprod for bill in billone.objects.all()]
        names_str = ", ".join(names)
        qt = [bill.oneqty for bill in billone.objects.all()]
        qt_str = ", ".join(qt)
        noq = [bill.onenoq for bill in billone.objects.all()]
        noq_str = ", ".join(noq)
        perp = [bill.onepra for bill in billone.objects.all()]
        perp_str = ", ".join(perp)
        ra = [bill.onerate for bill in billone.objects.all()]
        ra_str = ", ".join(ra)
        if 'save' in request.POST:
            if bool(request.POST['kad']):
                amo = request.POST['kad']
                kadan = round(int(ddi) - int(amo),2)
            else:
                kadan = 'nill'
            if bool(request.POST['numm']):
                numb = request.POST['numm']
            else:
                numb  = 'nill'
        
            current_date = datetime.now().date()
            formatted_date = current_date.strftime("%d/%m/%Y")
            current_time = datetime.now().time()
            formatted_time = current_time.strftime("%I:%M %p")

            billper.objects.create(dddat=formatted_date, tttim=formatted_time,perp = perp_str, proddd=names_str, qqty=qt_str, nofqty=noq_str, rrate=ra_str, teto= round(total_rate,2), dedis=dis, tetodis=round(ddi,2), dakad=kadan, ssnumm=numb)
            billcal.objects.create(total=total_rate, discount=dis, todiscount=ddi, amount=kadan)                    
    elif request.method == 'POST': 
        return redirect('/eror')
    return render(request,'hhhg.html',{'ket':fdf, 'tot': ddi,'dd':dis,'tt':total_rate,'unu':kjkk})

if __name__ == "__main__":
    cout()

def bcalculate_discounted_amount(total_amount, gg):
    discount_amount = (gg / 100) * total_amount
    #discounted_amount = total_amount - discount_amount
    return discount_amount

def bcout(request):
    kjkk = partcal.objects.all()
    total_rate = part.objects.aggregate(Sum('totalfee'))['totalfee__sum']
    ddi = total_rate
  

    dis = 0
    fdf = part.objects.all()
    partcal.objects.all().delete()
    global kadan
    if request.method == 'POST' and 'dis' in request.POST and bool(ddi):
        gg = request.POST['dis'] or 0
        discounted_amount = calculate_discounted_amount(total_rate, int(gg))
        print(discounted_amount)
        dis = round(discounted_amount,2)
        ddi = round(float(ddi) - float(dis),2)
        print(ddi)

        fdf = part.objects.all()
        names = [part.product for part in part.objects.all()]
        names_str = ", ".join(names)
        qt = [part.qty for part in part.objects.all()]
        qt_str = ", ".join(qt)
        ra = [part.rate for part in part.objects.all()]
        ra_str = ", ".join(ra)
        pe = [part.peccen for part in part.objects.all()]
        perr_str = ", ".join(pe)
        tfee = [part.come for part in part.objects.all()]
        tfee_str = ", ".join(tfee)
        ttfee = [part.totalfee for part in part.objects.all()]
        pec_str = ", ".join(ttfee)
        noqty = [part.noqty for part in part.objects.all()]
        noqty_str = ", ".join(noqty)
        toqrart = [part.toqrate for part in part.objects.all()]
        toqrart_str = ", ".join(toqrart)
        if 'save' in request.POST:
            if bool(request.POST['kad']):
                amo = request.POST['kad']
                kadan = int(ddi) - int(amo)  
                         
            else:
                kadan = 'nill'
            if bool(request.POST['numm']):
                numb = request.POST['numm']
            
            else:
                numb  = 'nill' 
            current_date = datetime.now().date()
            formatted_date = current_date.strftime("%d/%m/%Y")
            current_time = datetime.now().time()
            formatted_time = current_time.strftime("%I:%M %p")
            partper.objects.create(datt = formatted_date, timm = formatted_time ,bproduct = names_str,bnofq=noqty_str, borr = toqrart_str, bqty = qt_str, brate = ra_str, bper =perr_str,bcfee = tfee_str,btfee=pec_str, btotal = total_rate, bdis = dis, btodisp = ddi,bkad = kadan, bnumm = numb) 
            partcal.objects.create(btotal = total_rate, bdiscount = dis, btodiscount = ddi,bamount = kadan)
    elif request.method == 'POST':
        return redirect('/eror')
    return render(request,'bhhhg.html',{'ket':fdf, 'tot': ddi,'dd':dis,'tt':total_rate,'unu':kjkk})

if __name__ == "__main__":
    bcout()


def bill2(request):
    electric_products = ElectricProduct.objects.all()
    plumbing_products = PlumbingProduct.objects.all()
    hardware_products = HardwareProduct.objects.all()

    distinct_values_list_sstore_name = list(electric_products) + list(plumbing_products) + list(hardware_products)


    bii = part.objects.all()
    total_rate = part.objects.aggregate(Sum('totalfee'))['totalfee__sum']
    ddi = total_rate

    total_com = part.objects.aggregate(Sum('come'))['come__sum']
    dpe = total_com

    dis = 0  # initialize 'dis' to 0

    if request.method == 'POST' and 'dis' in request.POST:
        gg = request.POST['dis']
        ddi = float(ddi) - int(gg)
        dis = round(float(total_rate) - float(ddi),2)
        print(ddi)

    if request.method == 'POST' and bool(request.POST['qt']):
        # formdd = billforms2(request.POST)
        # if formdd.is_valid():
        sn = request.POST['pro']
        qy = request.POST['qt']
        noq = request.POST['noqty']
        pap = request.POST['rat']
        tnra = round(float(qy)*float(pap),2)
        trt = request.POST['pec']
        dper =  round((float(trt)/100)*float(tnra),2) 
        tof = round(float(dper) + float(tnra),2)
        part.objects.create(product=sn, qty=qy,noqty=noq, rate=pap,toqrate= tnra, peccen = trt,come = dper,totalfee = tof)      
        return redirect('/bill2')
    
    return render(request, 'bill2.html', {'distinct_values_sstore_name': distinct_values_list_sstore_name, 'ket': bii, 'tot': ddi,'dd':dis,'dpe':dpe})

def perdet(request):
    kkk = billper.objects.filter().order_by('-dddat','-tttim')
    total = 0
    for b in kkk:
        if b.dakad and b.dakad.isdigit() and int(b.dakad) > 0:
            total += int(b.dakad)

    print(total)
    return render(request, 'perdet.html', {'ket': kkk, 'tkad': total})



def bperdet(request):
    kkk = partper.objects.filter().order_by('-datt','-timm')
    total = 0
    for b in kkk:
        if b.bkad and b.bkad.isdigit() and int(b.bkad) > 0:
            total += int(b.bkad)

    print(total)
    return render(request, 'bperdet.html', {'ket': kkk, 'tkad': total})

def predictclear(request):
    try:
        billper.objects.all().delete()
        return redirect('/perdet')
    except:
        return redirect('/perdet')
def bpredictclear(request):
    partper.objects.all().delete()
    return redirect('/bperdet')

from .util import get_plot


from datetime import datetime
from django.db.models import Sum

def cusmap(request):
    query = billper.objects.all()
    data = {}
    for obj in query:
        try:
            date_obj = datetime.strptime(obj.dddat, '%d/%m/%Y')
            month_year = date_obj.strftime('%Y-%m')
            tetodis = float(obj.tetodis)  # Convert tetodis to float
            if month_year in data:
                data[month_year] += tetodis
            else:
                data[month_year] = tetodis
        except ValueError:
            pass

    x = sorted(data.keys())  # Sort the dates in ascending order
    y = [data[key] for key in x]
    chart = get_plot(x, y)
    return render(request, 'ch.html', {'chart': chart})


def bcusmap(request):
    query = partper.objects.all()
    data = {}
    for obj in query:
        try:
            date_obj = datetime.strptime(obj.datt, '%d/%m/%Y')
            month_year = date_obj.strftime('%Y-%m')
            btodisp = float(obj.btodisp)  # Convert tetodis to float
            if month_year in data:
                data[month_year] += btodisp
            else:
                data[month_year] = btodisp
        except ValueError:
            pass

    x = sorted(data.keys())  # Sort the dates in ascending order
    y = [data[key] for key in x]
    chart = get_plot(x, y)
    return render(request, 'ch.html', {'chart': chart})



def bhis(request, id):
    student = partper.objects.get(id=id)
    names = student.bproduct.split(',')
    qqq = student.bqty.split(',')
    rrr = student.brate.split(',')
    pe = student.bper.split(',')
    cfee = student.bcfee.split(',')
    borr  = student.borr.split(',')
    bnofq = student.bnofq.split(',') 
    ctotal = 0
    for number in cfee:
        try:
            ctotal += float(number)
        except ValueError:
            pass
    ct = round(ctotal, 2)
    tfee = student.btfee.split(',')

    to = student.btotal
    dis = student.bdis
    todis = student.btodisp
    kadan = student.bkad
    num = student.bnumm
    return render(request, 'bthhh.html', {'nam': names, 'qq': qqq, 'rr': rrr, 'tt': to, 'dd': dis, 'cfee': cfee, 'ctot': ct,'borr':borr, 'bnof':bnofq, 'tfee': tfee, 'pe': pe, 'tot': todis, 'kad': kadan, 'nu': num})













def rowpage(request, id):
    student = mytiger.objects.get(id=id)
    productname = student.name2.split(',')
    noof = student.name4.split(',')
    split = student.name5.split(',')
    rateper = student.name6.split(',')
    rate = student.name8.split(',')
    totrate = student.name9
    gst = student.name10
    totgst = student.name11
    payty = student.name13
    values = []
    cont = []
    fdfsaa = mytiger.objects.filter(id=id)

    for obj in fdfsaa:
        names = obj.name1.split(', ')
        if names:
            values.append(names[0].strip("[]"))

    for obj in fdfsaa:
        namesc = obj.name3.split(', ')
        if namesc:
            cont.append(namesc[0].strip("[]"))
    new_rate = float(student.name11)
    old_rate = float(student.name9)
    rrr = ((new_rate - old_rate) / old_rate) * 100
    percentage_difference = round(rrr,2)

    return render(request, 'rowpage.html', {'percentage_difference':percentage_difference,'cont': cont, 'name': values, 'ket': student, 'productname': productname,
                                             'noof': noof, 'split': split, 'rateper': rateper,
                                             'rate': rate, 'totrate': totrate, 'gst': gst,
                                             'totgst': totgst, 'payty': payty})
















def det(request, id):
    student = billper.objects.get(id=id)
    names = student.proddd.split(',')
    qqq = student.qqty.split(',')
    rrr = student.rrate.split(',')
    orpr = student.perp.split(',')
    nofno = student.nofqty.split(',')
    to = student.teto
    dis = student.dedis
    todis = student.tetodis
    kadan = student.dakad
    num = student.ssnumm
    
    print(rrr)
    return render (request,'thhh.html',{'nam':names,'qq':qqq,'rr':rrr,'opr':orpr,'tt':to,'dd':dis,'tot':todis,'kad':kadan,'noq':nofno,'nu':num})





def eror(request):
    return render(request,'eror.html')

def bpri(request):
    fdf = part.objects.all()
    vcyy = partcal.objects.first()
    return render(request,'bpri.html',{'ket':fdf,'too':vcyy})

def pri(request):
    fdf = billone.objects.all()
    vcyy = billcal.objects.first()
    return render(request,'pri.html',{'ket':fdf, 'too':vcyy})




def delete_view(request, id):
    student = productlist.objects.get(id=id)
    student.delete()
    return redirect('/proo/')


def htotd(request, id):
    student = partper.objects.get(id=id)
    student.delete()
    return redirect('/bperdet/')

def overdel(request, id):
    student = billper.objects.get(id=id)
    student.delete()
    return redirect('/perdet')




def delete_v(request, id):
    student = billone.objects.get(id=id)
    student.delete()
    return redirect('/cout')


def delete_b(request, id):
    student = part.objects.get(id=id)
    student.delete()
    return redirect('/bcout')



def upd(request, id):
    student = billone.objects.get(id=id)
    formdd = billforms(instance=student)
    if request.method == 'POST':
        formdd = billforms(request.POST, instance=student)
        if formdd.is_valid():
            sd = int(request.POST['oneqty'])
            aa = float(request.POST['onepra'])
            student.onerate = sd * aa
            student.save()
            return redirect('/cout')
    return render(request, 'selforup.html', {'form': formdd})


