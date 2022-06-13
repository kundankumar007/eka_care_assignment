from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.http import HttpResponse
from .forms import fromClass


def showfromdata(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = fromClass(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
      form = fromClass()

    """
    form = fromClass()
   
    """
    context = {'form':form}
   
    return render(request,'medicalConcepts/index.html',context)


def thanks(request):
    return HttpResponse("thanks")