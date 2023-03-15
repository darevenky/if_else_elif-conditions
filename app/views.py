from django.shortcuts import render

# Create your views here.

def sample(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'sample.html',d)