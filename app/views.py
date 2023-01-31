from django.shortcuts import render, redirect

from app.forms import CustomUserForm
from app.models import CustomUser


# Create your views here.
def home(request):
    return render(request,'index.html')

def tailor_register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        print(form)
        if form.is_valid():
            form=form.save(commit=False)
            form.is_tailor = True
            form.save()
            return redirect('tailor_view')
    return render(request,'tailor_register.html',{'form':form})

def tailor_view(request):
    data = CustomUser.objects.filter(is_tailor=True)
    return render(request,'tailor_view.html',{'data':data})

