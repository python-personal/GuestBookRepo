from django.shortcuts import render,redirect
from guestapp.models import *
from .forms import GuestForm
# Create your views here.
def HomeView(request):
    lists=Guest.objects.all()
    return render(request,'guestapp/home.html',{'lists':lists})

def createView(request):
    if request.method=='POST':
        form=GuestForm(request.POST)
        if form.is_valid():
            form=Guest(name=request.POST['name'],comment=request.POST['comment'])
            form.save()
            return redirect('home')
    form=GuestForm()
    return render(request,'guestapp/create.html',{'form':form})
