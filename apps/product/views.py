from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View


class Product(LoginRequiredMixin, View):
    def get(self, request,id=None):

        return HttpResponse(status=200)

    def post(self, request):

        return HttpResponse('Created', status=201)

    def put(self, request):

        return HttpResponse('Update', status=200)


class Category(LoginRequiredMixin, View):
    def get(self, request,id=None):

        return HttpResponse(status=200)

    def post(self, request):

        return HttpResponse('Created', status=201)

    def put(self, request):

        return HttpResponse('Update', status=200)
