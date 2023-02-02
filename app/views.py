from django.contrib import messages
from django.shortcuts import render, redirect

from app.filters import UserFilter
from app.forms import CustomUserForm, CustomUserUpdateForm, Dresscategoryform, DressForm
from app.models import CustomUser, DressCategory, Dress


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
            messages.success(request,'Tailor Registeration Successful')
            return redirect('tailor_view')
    return render(request,'tailor_register.html',{'form':form})

def tailor_view(request):
    data = CustomUser.objects.filter(is_tailor=True)
    tailorFilter = UserFilter(request.GET,queryset=data)
    data = tailorFilter.qs
    context = {
        'data':data,
        'tailorFilter':tailorFilter
    }
    return render(request,'tailor_view.html',context)

def tailor_edit(request,id):
    data = CustomUser.objects.get(id=id)
    form = CustomUserUpdateForm(instance=data)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST or None,instance=data or None)
        if form.is_valid():
            form=form.save(commit=False)
            form.is_tailor = True
            form.save()
            messages.success(request, 'Tailor Edited Successful')
            return redirect('tailor_view')
    return render(request,'tailor_edit.html',{'form':form})

def tailor_delete(request,id):
    data = CustomUser.objects.get(id=id)
    data.delete()
    messages.success(request, 'Tailor Deleted Successful')
    return redirect('tailor_view')

def dresscategory_add(request):
    form = Dresscategoryform()
    if request.method == 'POST':
        form = Dresscategoryform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'DressCategory Added')
            return redirect('dresscategory_view')
    return render(request,'dresscategory_add.html',{'form':form})

def dresscategory_view(request):
    data = DressCategory.objects.all()
    return render(request,'dresscategory_view.html',{'data':data})

def dresscategory_delete(request,id):
    data = DressCategory.objects.get(id=id)
    data.delete()
    messages.success(request, 'DressCategory deleted')
    return redirect('dresscategory_view')

def dress_add(request):
    form = DressForm()
    if request.method == 'POST':
        form = DressForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Dress Added')
            return redirect('dress_view')
    return render(request,'dress_add.html',{'form':form})

def dress_view(request):
    data = Dress.objects.all()
    return render(request,'dress_view.html',{'data':data})

def dress_update(request,id):
    data = Dress.objects.get(id=id)
    form = DressForm(instance=data)
    if request.method == 'POST':
        form = DressForm(request.POST or None,request.FILES or None,instance=data or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dress Updated')
            return redirect('dress_view')
    return render(request,'dress_update.html',{'form':form})

def dress_delete(request,id):
    data = Dress.objects.get(id=id)
    data.delete()
    messages.success(request, 'Dress deleted')
    return redirect('dress_view')




