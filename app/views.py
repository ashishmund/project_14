from django.shortcuts import render

# Create your views here.
def flash(request):
    return render(request,'flash.html')