from django.shortcuts import render, HttpResponseRedirect
from .models import Directory
from .forms import DirectoryForm
from django.contrib import messages
from django.db.models import Q

def create_retrive(request):  # create and retrive
    if request.method == 'POST':
        form = DirectoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "your contact detail added successfully !!")
    
    form = DirectoryForm()
    person = Directory.objects.all()
    return render(request, 'app/add.html',{'form':form,'person':person})

# -----------------------------------------------------------------------------

def update_data(request, id): # update
    if request.method == 'POST':
        pid = Directory.objects.get(pk=id)
        form = DirectoryForm(request.POST, request.FILES, instance=pid)
        if form.is_valid():
            form.save()
            messages.success(request, "your contact detail updated successfully !!")
    
    pid = Directory.objects.get(pk=id)
    form = DirectoryForm(instance=pid)

    return render(request, 'app/updatedata.html',{'form':form})

# -----------------------------------------------------------------------------------------

def delete_data(request,id):    # delete
    if request.method == 'POST':
        pid = Directory.objects.get(pk=id)
        pid.delete()
        return HttpResponseRedirect('/')

# ----------------------------------------------------------------------------------------

def search_data(request):   # search function
    if request.method == 'POST':
        q = request.POST['q']
        result = Directory.objects.filter(Q(name__icontains=q) | Q(number__icontains=q))
        return render (request, 'app/searchhistory.html',{'result':result})
    else:
        return render (request, 'app/searchhistory.html')