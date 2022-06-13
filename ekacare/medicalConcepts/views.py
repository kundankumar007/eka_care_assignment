from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.http import HttpResponse
from .forms import fromClass


def showfromdata(request):
    if request.method == 'POST':
    
        form = fromClass(request.POST)
        
        if form.is_valid():
          
            return HttpResponseRedirect('/thanks/')

    
    else:
      form = fromClass()

    context = {'form':form}
   
    return render(request,'medicalConcepts/index.html',context)


def thanks(request):
    return HttpResponse("thanks")