'''
Created on Aug 26, 2013

@author: antipro
'''
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateResponseMixin
from social_auth.db.django_models import UserSocialAuth

@login_required
def main(request, template='accounts/social.html'):
    data = {}

    socials = UserSocialAuth.objects.filter(user=request.user)
    data['socials'] = socials

    return TemplateResponse(request, template, data)


