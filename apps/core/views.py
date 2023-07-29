from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboad(LoginRequiredMixin, View):

    def get(self, request: HttpRequest):

        return render(request, 'dashboard/dashboard.html', {'name': 'Esmailton Silva Gomes'})