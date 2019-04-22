from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Debug, Future_Feature

def all_debug(request):
    debugs = Debug.objects.all()
    features = Future_Feature.objects.all()
    for debug in debugs:
        debug.views += 1
        debug.save()
    return render(request, 'debug_details.html', {"debugs": debugs}, {"features": features})
    
def bug_details(request, pk):
    debug = get_object_or_404(Debug, pk=pk)
    debug.views += 1
    debug.save()
    return render(request, 'debug_view.html', {'debug': debug})  
    
def bug_like(request, pk):
    if pk:
        debug = Debug.objects.get(id=pk)
        count = debug.likes
        count += 1
        debug.likes = count
        debug.save()
    return redirect('all_debug')
    
def free_debug(request):
    debugs = Debug.objects.all()
    return render(request, 'free_debug.html', {"debugs": debugs})    
    
    
    
    
    

