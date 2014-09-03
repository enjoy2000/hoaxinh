# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from datetime import date, datetime
import json

from hoaxinh.image.models import Image
from hoaxinh.image.forms import ImageForm

def index(request):
    # Count photos uploaded
    img_list = Image.objects.all().count()

    # Calculate number of days together
    started_day = date(2014,6,11)
    current_day = date.today()
    dif_days = current_day - started_day
    together_days = dif_days.days

    # Lovers profile
    male = {}
    male['name'] = 'Minh Hạt'
    male['fb'] = 'enjoy.hat'
    female = {}
    female['name'] = 'Hòa Xinh'
    female['fb'] = '100007996269960'
    lovers = {}
    lovers['male'] = male
    lovers['female'] = female

    # Num of photos uploaded
    numOfPhotos = Image.objects.all().count()

    return render_to_response('image/index.html',
        {
            'together_days': together_days,
            'lovers': lovers,
            'numOfPhotos': numOfPhotos,
        },
        context_instance=RequestContext(request))

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            for img in request.FILES.getlist('name'):
                newdoc = Image(name = img)
                newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('hoaxinh.image.views.list'))

    else:
        form = ImageForm() # A empty, unbound form


    # Load documents for the list page
    documents_list = Image.objects.all()

    # Pagination
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    limit = 16 # limit photos each page
    paginator = Paginator(documents_list, limit)

    # Render list page with the documents and the form
    return render_to_response(
        'image/list.html',
        {'paginator': paginator},
        context_instance=RequestContext(request)
    )

def add(request):
    # Handle file upload
    responseData = []
    response_data = {}
    response_data['result'] = 'failed'
    response_data['files'] = 'abc'
    for img in request.FILES.getlist('files[]'):
        # import pdb; pdb.set_trace();
        # Check file is image or not
        file_type = img.content_type.split('/')[0]
        if file_type != 'image':
            messages.error(request, "Your file is not image.")
            HttpResponseRedirect(reverse('hoaxinh.image.views.list'))
        
        newdoc = Image(name = img)
        newdoc.save()
        responseData.append(img)

    return HttpResponse(json.dumps(response_data), content_type="application/json")

# Delete photo by id
def delete(request):
    id = request.GET['id']
    if(id):
        photo = Image.objects.get(pk=id)
        if(photo):
            photo.delete()
            messages.success(request, "Your photo has been deleted.")
            return HttpResponseRedirect(reverse('hoaxinh.image.views.list'))
        else:
            messages.error(request, "Your photo is not exist.")
            return HttpResponseRedirect(reverse('hoaxinh.image.views.list'))


def clear(request):
    # Clear model
    if request.is_ajax():
        Image.objects.all().delete()
    else:
        messages.success(request, "This view for ajax only");
        return HttpResponseRedirect(reverse('hoaxinh.image.views.list'))
    
    successMessage = 'Deleted all.'
    return HttpResponse(successMessage)

def ajaxload(request):
    #Ajax view for loading additional photos
    if request.is_ajax():
        photo_list = Image.objects.all()

        # Pagination
        from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
        limit = 16 # limit photos each page
        paginator = Paginator(photo_list, limit)
        page = request.POST.get('page')
        try:
            documents = paginator.page(page)
        except PageNotAnInteger:
            # If page is not number, deliver to first page
            documents = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver to last page
            documents = paginator.page(paginator.num_pages)

        # Render list page with the documents and the form
        return render_to_response(
            'image/ajaxload.html',
            {'documents': documents,},
            context_instance=RequestContext(request)
        )