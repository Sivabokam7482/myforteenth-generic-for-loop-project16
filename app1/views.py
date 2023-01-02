from django.shortcuts import render

# Create your views here.
def loops(request):
    d={'name':'NIVI','a':[11,12,13]}
    return render(request,'for-loop.html', d)