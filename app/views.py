from django.shortcuts import render

# Create your views here.

def app_uday(request):
    dict={'a':1,'b':2,'c':3}
    return render(request,'app.html',context=dict)