from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View


class Product(View):
    def get(self, request,id=None):

        return HttpResponse('retrive', status=200)

    def post(self, request):

        return HttpResponse('Created', status=201)

    def put(self, request):

        return HttpResponse('Update', status=200)
