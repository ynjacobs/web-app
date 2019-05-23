from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from random import randint

def root(request):
    return HttpResponseRedirect('home')

def gallery(request):
    return HttpResponseRedirect('/portfolio')


def home_page(request):
    context = {'name': 'Betty Maker'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def portfolio(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))

    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request):
    context = {'skills': ['coding'], 'interests': ['sports', 'food', 'medicine']}
    response = render(request, 'about.html', context)
    return HttpResponse(response)

def favourites(request):
    context = {'fave_links': 'https://alexa.bitmaker.co/wdi/april-2019/assignments/5318'}
    response = render(request, 'fave.html', context)
    return HttpResponse(response)