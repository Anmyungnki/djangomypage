from django.shortcuts import render , get_object_or_404  , redirect     #
from django.http import HttpResponse , HttpResponseRedirect   #
from .models import Category, Post                          #
from django.urls import reverse                               #
from django.views import generic                              #
from django.template import loader                            #
from django.utils import timezone                             #
from django.http import Http404
# Create your views here.


def index(request):

    context= {

             }
    return render(request, "amk/index.html",context=context)


def contact(request):

    context= {

             }
    return render(request, "amk/contact.html",context=context)


def about(request):

    context= {

             }
    return render(request, "amk/about.html",context=context)


def post(request):

    context= {

             }
    return render(request, "amk/post.html",context=context)


def storege(request):
    st_msg = Post.objects.order_by('updateDate')[::-1][:6]

    context= {
              'st_msg': st_msg,
             }
    return render(request, "amk/storege.html",context=context)



def storege_detail(request):

    if request.method == 'POST':

        Post.objects.create(tittle=request.POST['tittle'], content=request.POST['content'])            #포스트생성

        return HttpResponseRedirect('storege')
