from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

# from .models import Contact, List, Task
from tasks.models import Contact, List, Task

def index(request):
    if (request.method == 'POST'): # create
        list_id = int(request.POST['list_id'])
        assignee_id = int(request.POST['assignee_id'])
        #TODO check if contact with assignee_id exist
        try:
            contact = Contact.objects.get(pk=assignee_id)
        except Contact.DoesNotExist:
            return render(request, 'tasks/new.html', {
                'list_id': list_id,
                'title': request.POST['title'],
                'description': request.POST['description'],
                'assignee_id': request.POST['assignee_id'],
                'status': request.POST['status']
            })
        t = Task(
                list_id=list_id,
                title=request.POST['title'],
                description=request.POST['description'],
                assignee_id=request.POST['assignee_id'],
                status=request.POST['status']
            )
        t.save();
        return HttpResponseRedirect(reverse('lists:show', args=[list_id]))

def show(request, task_id):    # destroy/update
    task = get_object_or_404(Task, pk=task_id)
    list_id = task.list_id
    if (request.method == 'GET'): # show
        assignee = get_object_or_404(Contact, pk=task.assignee_id)
        return render(request, 'tasks/show.html', {'task': task, 'assignee': assignee})
    elif (request.method == 'POST'):
        if (request.POST['method'] == 'DELETE'): #destroy
            task.delete()
            return HttpResponseRedirect(reverse('lists:show', args=[list_id]))
        elif (request.POST['method'] == 'PUT'): #update
            task.title = request.POST['title']
            task.description = request.POST['description']
            task.assignee_id = request.POST['assignee_id']
            task.status = request.POST['status']
            task.save()
            return HttpResponseRedirect(reverse('lists:show', args=[list_id]))

def new(request):
    return render(request, 'tasks/new.html', {'list_id': request.GET['list_id']})

def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/edit.html', {'task': task})
