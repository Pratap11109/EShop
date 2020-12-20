from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
import datetime
from django.shortcuts import render ,redirect 
from .form import *

def Home(request):
    pro = Product.objects.all()
    print(type(pro))
    return render (request,'html/base.html',{ 'pro':pro })


def custregi(request):
    form=registerForm
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            group=Group.objects.get(name='Customer')
            user.groups.add(group)
            
            username = form.cleaned_data.get('username')
            messages.success(request,"New account created:"+username )
            return redirect('login')
        else:
            messages.error(request,"not register")
    return render (request,'html/regi.html',{"form":form})
    

def supregi(request):
    form= registerForm
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            group=Group.objects.get(name='Supplier')
            user.groups.add(group)
            
            username = form.cleaned_data.get('username')
            messages.success(request,"New account created:"+username )
            return redirect('Home')
        else:
            messages.error(request,"not register")
    print(form)
    return render(request,'html/regi.html',{"form":form})


def loginfun (request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('view')
        else :
            msg = 'enter right Detailes'
            
    return render (request,'html/login.html' ,{'msg' : msg })

@login_required(login_url='login')
def product(request):
    msg = ''
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = form.save()
            return redirect('Product')
        else :
            msg = 'enter right Detailes'
    return render(request,'html/Product.html',{'msg': msg ,'form':form})

@login_required(login_url='login')
def chart(request,pid):
    msg = ''
    form = OrderDetails
    pro = Product.objects.get(id=pid)
    if request.method == 'POST':
        user = request.user
        pro = Product.objects.get(id = pid) 
        qu=request.POST.get('qut')
        print(qu)
        p = int(pro.p_countity) -int(qu)
        if p >= 0:
            print(p)
            pro.p_countity=p
            pro.save()
            od=OrderDetails(product=pro,user=user,qut = qu ,OrderDate = date.today() )
            od.save()
            print(od.id)
            return redirect('addrese' , oid= od.id)
        else:
            return redirect('chart')
    else :
        msg = 'enter right Detailes'
    return render (request,'html/chart.html',{'form':form,'pro':pro })

@login_required(login_url='login')
def viewproduct(request):
    mw = Product.objects.filter(cat= 'mw')
    lt = Product.objects.filter(cat= 'laptop')
    elec = Product.objects.filter(cat= 'ele')
    mob = Product.objects.filter(cat= 'mobile')
    if request.user.groups.filter(name='Supplier').exists():
        return redirect('Product')
    return render(request,'html/view.html',{ 'mw':mw,'lt':lt,'elec':elec,'mobile':mob })
  
@login_required(login_url='login')
def addrese(request,oid):
    od=OrderDetails.objects.get(id=oid)
    use=request.user
    form = Addres
    if request.method =='POST':
        add=request.POST.get('addrese')
        city=request.POST.get('city')
        zc=request.POST.get('zipcode')
        form1=Addres(Addrese=add,city=city,zipcode=zc,user=use)
        form1.save()
        print('*******')
        print( form1.id )
        return redirect ('order', oid=oid, ad=form1.id)
    else:
        print("**else PArt **")
    return render(request,'html/addres.html',{'form':form,'od':od })

@login_required(login_url='login')
def order(request,oid,ad):
    od=OrderDetails.objects.get(id=oid)
    ad=Addres.objects.get(id=ad)
    use=request.user
    payment=od.qut * od.product.p_price
    dd=datetime.date.today()+datetime.timedelta(8)
    if request.method == 'POST':
        form = Order(OD=od,user=use,deliverydate=dd,totalpayment=payment,add=ad)
        form.save()
        print(form)
        return redirect('payment', form.id )
    return render (request,'html/order.html',{'od':od,'use':use,
     'payment': payment,'dd':dd,'ad':ad })

@login_required(login_url='login')
def payment(request,oid):
    pay = Payment
    user = request.user
    order = Order.objects.get(id=oid)
    if request.method == 'POST':
        order = Order.objects.get(id=oid)
        payp = int(request.POST.get('payp'))
        prem= order.totalpayment - payp 
        pay=Payment(order=order,payrem=prem,payp=payp)
        pay.save()
        return redirect('finshed',pay.id)
    return render(request,'html/payment.html',{'pay':pay,'user':user
                                        ,'order':order})
@login_required(login_url='login')
def finshed(request,pid):
    paym = Payment.objects.get(id=pid)
    user = request.user  
    print(request.user.first_name)
    return render(request,'html/finshed.html',{'paym':paym
                   , 'user': user })
        

@login_required(login_url='login')
def logoutfun(request):
    logout(request)
    return redirect('Home')


