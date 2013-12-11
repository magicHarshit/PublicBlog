from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from post.models import Article, Comment
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    posts = []
    return render_to_response('home.html', {'posts':posts}, context_instance=RequestContext(request))


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
