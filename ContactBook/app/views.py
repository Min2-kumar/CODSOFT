from django.shortcuts import render
from .models import Directory
from .forms import DirectoryForm


def create_retrive(request):  # create and retrive
    print('hi')
    if request.method == 'POST':
        form = DirectoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    form = DirectoryForm()

    person = Directory.objects.all()
    return render(request, 'app/add.html',{'form':form, 'person':person})

# -----------------------------------------------------------------------------

def update_data(request, id): # update
    if request.method == 'POST':
        pid = Directory.objects.get(pk=id)
        form = DirectoryForm(request.POST, request.FILES, instance=pid)
        if form.is_valid():
            form.save()
    
    pid = Directory.objects.get(pk=id)
    form = DirectoryForm(instance=pid)

    # return render(request, 'app/index.html',{'form':form})