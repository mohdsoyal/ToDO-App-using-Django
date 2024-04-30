from django.shortcuts import render,redirect
from .forms import FormModel
from .models import ToDOclass
from django.contrib.auth import login

# Create your views here.

def home(request):
    fm = FormModel()  
    data = ToDOclass.objects.all()  
    
    if request.method == 'POST':
        fm = FormModel(request.POST)  
        if fm.is_valid():
            subject = fm.cleaned_data['subject']
            description = fm.cleaned_data['description']
            task_Assign_by = fm.cleaned_data['task_Assign_by']
            task_complete_to = fm.cleaned_data['task_complete_to']
            Complete_By = fm.cleaned_data['Complete_By']
            Saved = ToDOclass(subject=subject, description=description, task_Assign_by=task_Assign_by, task_complete_to=task_complete_to, Complete_By=Complete_By)
            Saved.save()
            return  redirect('/') 
    else:
        fm=FormModel()        
    return render(request, 'todolist.html', {'fm': fm, 'data': data})


def Update(request,id):
    pi=ToDOclass.objects.get(id=id)
    if request.method =='POST':
        fm=FormModel(request.POST ,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm=FormModel(instance=pi)
        return render(request,'update.html',{'fm':fm})    
    
    
    
def Delete(request,id):
    fm=ToDOclass.objects.get(id=id)
    fm.delete()
    return redirect('/')
    
        
    
    


    