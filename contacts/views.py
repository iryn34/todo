# from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import Contact
import json

def index(request, format):
    if (request.method == 'GET'):
        contact_list = Contact.objects.all()
        context = {'contact_list': contact_list}
        if (format == 'html'):
            return render(request, 'contacts/index.html', context)
        elif (format == 'json'):
            contact_list_json = []
            for contact in contact_list:
                contact_list_json.append({
                    'name': contact.name,
                    'email': contact.email,
                    'telephone': contact.telephone
                })
            return HttpResponse(json.dumps(contact_list_json))
    elif (request.method == 'POST'): # create
        c = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            telephone=request.POST['telephone']
        )
        c.save();
        return HttpResponseRedirect(reverse('contacts:index', args=['html']))

def new(request):
    print('NEW')
    print('NEW')
    print('NEW')
    print('NEW')
    print('NEW')
    return render(request, 'contacts/new.html')

def show(request, contact_id, format):    # destroy/update
    if (request.method == 'GET'): # show
        contact = get_object_or_404(Contact, pk=contact_id)
        if (format == 'html'):
            return render(request, 'contacts/show.html', {'contact': contact})
        elif (format == 'json'):
            contact_json = json.dumps({
                'name': contact.name,
                'email': contact.email,
                'telephone': contact.telephone
            })
            return HttpResponse(contact_json)
    elif (request.method == 'POST'):
        if (request.POST['method'] == 'DELETE'): #destroy
            contact = Contact.objects.get(pk=contact_id)
            contact.delete()
            if (format == 'html'):
                return HttpResponseRedirect(reverse('contacts:index', args=['html']))
            elif (format == 'json'):
                contact_json = json.dumps({
                    'name': contact.name,
                    'email': contact.email,
                    'telephone': contact.telephone
                })
                return HttpResponse(contact_json)
        elif (request.POST['method'] == 'PUT'): #update
            contact = get_object_or_404(Contact, pk=contact_id)
            contact.name = request.POST['name']
            contact.email = request.POST['email']
            contact.telephone = request.POST['telephone']
            contact.save()
            if (format == 'html'):
                return HttpResponseRedirect(reverse('contacts:index', args=['html']))
            elif (format == 'json'):
                contact_json = json.dumps({
                    'name': contact.name,
                    'email': contact.email,
                    'telephone': contact.telephone
                })
                return HttpResponse(contact_json)

# def destroy(request, contact_id):
#     if (request.method == 'POST'):
#         if (request.POST['method'] == 'DELETE'):
#             c = Contact.objects.get(pk=contact_id)
#             c.delete()
#             return HttpResponseRedirect(reverse('contacts:index'))

def edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/edit.html', {'contact': contact})

# def update(request, contact_id):
#     if (request.method == 'POST'):
#         contact = get_object_or_404(Contact, pk=contact_id)
#         contact.name = request.POST['name']
#         contact.email = request.POST['email']
#         contact.telephone = request.POST['telephone']
#         contact.save()
#         return HttpResponseRedirect(reverse('contacts:index'))
