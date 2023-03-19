from django.shortcuts import render,HttpResponse,redirect
from DHome.models import CustomerForm1,Account
from django.contrib.auth.models import User ,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def chome(request):
    # loginC = Account.objects.all()
    if request.user.is_anonymous:
        return redirect('loginuser')
    return render(request, 'index.html')
def cform(request):
    if request.user.is_anonymous:
        return redirect('loginuser')
    if request.method == "POST":
        imag = request.POST.get('Photos')
        dim1 = request.POST.get('dim1')
        dim2 = request.POST.get('dim2')
        typ = request.POST.get('type')
        loadwgt = request.POST.get('weight')
        tadd = request.POST.get('tadd')
        fadd = request.POST.get('fadd')
        ddate = request.POST.get('ddate')
        bgt = request.POST.get('budg')
        desc = request.POST.get('desc')
        en = CustomerForm1(imag = imag,dim1=dim1,dim2=dim2,typ=typ,loadWgt=loadwgt,tadd=tadd,fadd=fadd,ddate=ddate,budg=bgt,desc=desc)
        en.save()
        
    return render(request, 'cform.html')

def rhome(request):
    if request.user.is_anonymous:
        return redirect('loginuser')
    details = CustomerForm1.objects.all()
    return render(request,'rhome.html',{'details':details})

def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None and user.role == 'Customer':
            login(request, user)
            return redirect('/')
        elif user is not None and user.role == 'Driver':
            login(request, user)
            return redirect('dhome')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('loginuser')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role= request.POST.get('role')
        if password1 == password2:
            if Account.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('/register')
            elif Account.objects.filter(username = username):
                messages.info(request,"Username arlready registered")
                return redirect("/register")
            else:
                user = Account.objects.create_user(username=username,email=email,password = password1, role=role)
                user.save();
                return redirect('/loginuser')
        else:
            messages.info(request,"Password Not Matched")
            return redirect(request,"register")
    else:
        return render(request,'register.html')

def dhome(request):
    if request.user.is_anonymous:
        return redirect('loginuser')
    return render(request,'driverhome.html')

def logoutuser(request):
    logout(request)
    return redirect('loginuser')