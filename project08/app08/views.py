from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')

def preindex(request):
    return render(request,'Counter-Up-master/demo/preindex.html')