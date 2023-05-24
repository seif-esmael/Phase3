from django.shortcuts import render

# Create your views here.
def first_of_all(request):
    return render(request, 'pages/First_Of_All.html')

def home_page(request):
    return render(request, 'pages/Home_Page.html')

def sign_in(request):
    return render(request, 'pages/Sign_In.html')