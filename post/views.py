from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from post.models import Article, Comment, Vote
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json


def home(request):
    posts = []
    return render_to_response('index.html', {'posts': posts}, context_instance=RequestContext(request))

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def get_user(request):
    authenticated = request.user.is_authenticated()
    username = request.user.username
    user_id = request.user.id
    data = {'username': username, 'authenticated':authenticated,'id':user_id}
    data = json.dumps(data)
    return HttpResponse(data)


def create_or_update_vote(request):
    post_data = json.loads(request.raw_post_data)
    article_id = post_data['article']
    vote_type = post_data['vote_type']
    user_id = request.user.id

    vote_obj,created = Vote.objects.get_or_create(article_id=article_id,user_id=user_id)
    vote_obj.vote_type = vote_type
    vote_obj.save()
    data = {'success': 'success'}
    data = json.dumps(data)
    return HttpResponse(data)


def calculate_points(request):
    user = json.loads(request.raw_post_data).get('user')
    vote_down_count_by_user = Vote.objects.filter(user=user, vote_type=-1).count()
    points_on_vote_down = vote_down_count_by_user*-2

    vote_up_count_on_articles_of_user = Vote.objects.filter(article__user=user,vote_type=1).count()
    vote_down_count_on_articles_of_user = Vote.objects.filter(article__user=user,vote_type=-1).count()

    total_votes_for_articles = vote_up_count_on_articles_of_user-vote_down_count_on_articles_of_user
    points_for_articles = total_votes_for_articles*10
    points = points_for_articles - points_on_vote_down
    data = json.dumps({'points':points})
    return HttpResponse(data)




