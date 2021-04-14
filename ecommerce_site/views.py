from django.shortcuts import render

# Create your views here.
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

