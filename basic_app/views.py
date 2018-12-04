# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View,TemplateView, ListView , DetailView
from django.http import HttpResponse
from django.shortcuts import render

from . import models

# Create your views here.
class CBView(View):
    def get(self,request):
        return HttpResponse("Class Base View are awesome")

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected_view'] ="Im injected from view"
        return context

class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name ="school_detail"
    model= models.School
    template_name = 'basic_app/school_detail.html'
