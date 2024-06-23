from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Info/home.html')

def farming(request):
    return render(request, 'Info/farming.html')

def disease(request):
    return render(request, 'Info/disease.html')    

def market(request):
    return render(request, 'market/market_list.html')