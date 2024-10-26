from django.shortcuts import render
from application.models import *
from django.contrib import messages

# Create your views here.

def home(request):
    
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('subject')
        d = request.POST.get('message')

        info = table(name=a, email=b, subject=c, message=d)

        info.save()

        messages.success(request, 'Data successfully inserted !')

    return render(request, 'index.html')


