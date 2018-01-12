from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from tasks.models import Contact, List, Task

def index(request):
    pk = 1
    if (request.method == 'GET'):
        contact = Contact.objects.get(pk=pk)
        list_list = contact.list_set.all()
        context = {'list_list': list_list}
        return render(request, 'lists/index.html', context)
    elif (request.method == 'POST'): #create
        l = List(
            title=request.POST['title'],
            owner_id=pk
        )
        l.save();
        return HttpResponseRedirect(reverse('lists:index'))

def show(request, list_id):    # destroy/update
    if (request.method == 'GET'): # show
        list = get_object_or_404(List, pk=list_id)
        tasks = Task.objects.filter(list_id=list_id)
        return render(request, 'lists/show.html', {'list': list, 'tasks': tasks})
    elif (request.method == 'POST'):
        if (request.POST['method'] == 'DELETE'): #destroy
            l = List.objects.get(pk=list_id)
            l.delete()
            return HttpResponseRedirect(reverse('lists:index'))
        elif (request.POST['method'] == 'PUT'): #update
            list = get_object_or_404(List, pk=list_id)
            list.title = request.POST['title']
            list.save()
            return HttpResponseRedirect(reverse('lists:index'))

def new(request):
    return render(request, 'lists/new.html')

def edit(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    return render(request, 'lists/edit.html', {'list': list})
