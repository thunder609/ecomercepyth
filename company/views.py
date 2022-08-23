from django.http import HttpResponse
from django.shortcuts import render
from .forms import CountryForm

def index(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html',{'form':form})

    else:        
     form =CountryForm()
     return render(request,'index.html',{'form':form})
