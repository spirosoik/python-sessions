from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
  return HttpResponse("Hello, Sparti Tech Lab!")


def name(request, name):
  return HttpResponse(f'Sparti Tech Lab says: hi {name}')


def template(request, name):
  return render(request, 'template-1.html', {'name': name})


class MyView(View):

  def get(self, request, *args, **kwargs):
    return HttpResponse('Awesome Sparti Tech Lab!!')
