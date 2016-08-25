# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.models import Gallery
from myproject.myapp.forms import DocumentForm
from myproject.myapp.forms import NameForm
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.conf.urls import url
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse



# Create your views here.
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.template.defaultfilters import slugify

import json



def login(request):
    return render_to_response('login.html')



@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


@login_required(login_url='/')
def list(request):
    tags = Gallery.objects.filter(username=request.user)
    tagArray = []

    
    while (tags):
        tagArray.append(tags.first().tag)
        tags = tags.exclude(tag=tags.first().tag)

    #choices = Document.objects.order_by().values('tag').distinct()
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            tagSpace = slugify(request.POST.get('tag'))
            if Gallery.objects.filter(username=request.user,tag=tagSpace).exists():
                newdoc = Document(docfile=request.FILES['docfile'],gallery=Gallery.objects.filter(username=request.user,tag=tagSpace).first())
                newdoc.save()
            else:
                newGallery = Gallery(username=request.user,tag=tagSpace,thumb=request.FILES['docfile'])
                newGallery.save()
                newdoc = Document(docfile=request.FILES['docfile'],gallery=newGallery)
                newdoc.save()



            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    galleries = Gallery.objects.all()

    # Render list page with the documents and the form
    return render( 
        request,
        'list.html',
        {'form': form,'galleries':galleries,'tags':tagArray}
    )


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             newchoice = Choice(choice=request.POST.get("your_name"))
#             newchoice.save()

#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#     

  #  return render(request, 'name.html', {'form': form})


@login_required(login_url='/')
def viewTag(request, requestedTag,username):
    documents = Document.objects.filter(gallery=Gallery.objects.filter(username=username,tag=requestedTag)).all()
    return render(request,'images.html',{'documents':documents,'Tag':requestedTag,'user':username})

