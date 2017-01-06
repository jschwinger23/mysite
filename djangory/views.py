from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from djangory.models import Entries


# Create your views here.

def show_entries(request):
    entries = Entries.objects.all()
    return render(request, 'djangory/templates/show_entries.html', {'entries': entries})

def add_entry(request):
    if not request.session.get('logged_in'):
        return HttpResponse('Unauthorized', status=401)

    entries = Entries(title=request.POST['title'], text=request.POST['text'])
    entries.save()
    return HttpResponseRedirect('/v1')

def login(request):
    error = None
    if request.method == 'POST':
        if request.POST['username'] != settings.USERNAME:
            error = 'invalid username'
        elif request.POST['password'] != settings.PASSWORD:
            error = 'invalid password'
        else:
            request.session['logged_in'] = True
            return HttpResponseRedirect('/v1')
    return render(request, 'djangory/templates/login.html', dict(error=error))

def logout(request):
    request.session['logged_in'] = False
    return HttpResponseRedirect('/v1')
