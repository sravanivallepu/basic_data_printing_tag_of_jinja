from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'kanna','age':23}
    return render(request,'wish.html',context=d)