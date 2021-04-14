from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def toLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def toRegister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Taken')
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
            else:
                user = User.objects.create_user(username=username, password = password1, email=email, first_name =first_name, last_name=last_name)
                user.save()
                messages.info(request,'user created')
                return redirect('login.html')
        else:
            messages.info(request, 'password does not match....')
            return render(request, 'register.html')
        return redirect('/')
    else:
        return render(request,'register.html')

def toShopSingle(request):
    return render(request,'shop-single.html')
def toShop(request):
    return render(request,'shop.html')
def toContact(request):
    return render(request,'contact.html')
def toAbout(request):
    return render(request,'about.html')
def toIndex(request):
    return render(request,'index.html')

