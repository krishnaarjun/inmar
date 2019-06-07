# Author: Integra
# Dev: Partha(Ref)

import hashlib, re, sys, inspect
from datetime import datetime 

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.utils.translation import activate
from django.utils.deprecation import MiddlewareMixin


class LoginRequired(MiddlewareMixin):

    def process_request(self, request):
    	is_authenticated = request.user.is_authenticated
    	if is_authenticated:
    		if request.path == '/login/':
    			return HttpResponseRedirect('/')
    	else:
            if request.path == '/login/':
                return
            return HttpResponseRedirect('/login/')