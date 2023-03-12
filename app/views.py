from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
pages={
    'tajmahal':'tajmahal.html'
}
def HomePage(request):
    return render (request,'home.html')


def HomePages(request):
    return render (request,'home1.html')


def City(request):
    return render(request, 'city.html')


def Petra(request):
    return render(request, 'petra.html')


def Statue(request):
    return render(request, 'statue.html')


def Machu(request):
    return render(request, 'machu.html')


def Chicken(request):
    return render(request, 'chicken.html')


def Roman(request):
    return render(request, 'roman.html')


def TajMahal(request):
    return render(request, 'tajmahal.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Passsword doesnt match!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect ('login')
        print(uname,pass1)
    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user = authenticate(request, username=username, password=pass1)
        return redirect('home1')  #
        
        if user is not None:
            login(request,user)
            return redirect('home1')
            
        else:
            return HttpResponse("Username or password incorrect!!")
    return render (request,'login.html')
def LogoutPage(request):
    logout(request)
    return redirect ('login')
def search(request):
    search=request.get('search')
    if search in pages:
        page_url = pages[search]
        return redirect(page_url)
    else:
        return HttpResponse("places not yet found!!")    # if request.method=="POST":
    #     search=request.POST.get['search']
    #     city=City.objects.filter(name__contains="search")
    #     return render(request,'city.html',{'search':search,'city':city},)
    # else:
    #     return render(request,'city.html')
   


