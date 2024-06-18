from django.shortcuts import render


from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def services(request):
    return render(request, 'main/services.html')

def sell(request):
    return render(request, 'main/sell.html')

def shop(request):
    return render(request, 'main/shop.html')

def about(request):
    return render(request, 'main/about.html')

