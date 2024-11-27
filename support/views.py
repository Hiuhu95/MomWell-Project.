from django.shortcuts import render

def index(request):
    return render(request, 'support/index.html')

def ppd(request):
    return render(request, 'support/ppd.html')

def anx(request):
    return render(request, 'support/anx.html')

def weightmgt(request):
    return render(request, 'support/weightmgt.html')
