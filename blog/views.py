# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from datetime import date, datetime

from blog.models import Blog

# Create your views here.
def index(request):
	# List all blogs on index with pager
	blog_list = Blog.objects.all()

	# Pagination
	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
	limit = 8 # limit photos each page
	paginator = Paginator(blog_list, limit)

	# Get page from url
	page = request.GET.get('page')
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver to first page
		blogs = paginator.page(1)
	except EmptyPage:
		# If page is out of range, deliver to last page
		blogs = paginator.page(paginator.num_pages)

    # Return to list page with paginator and content
	return render_to_response(
        'blog/index.html',
        {'paginator': paginator, 'blogs': blogs},
        context_instance=RequestContext(request)
    )