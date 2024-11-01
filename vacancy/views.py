from unicodedata import category

from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.
class JobListView(ListView):
    model = Job
    template_name = "job_list.html"
    context_object_name = "jobs"

class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"

class JobCreateView(CreateView):
    model = Job
    template_name = "job_create.html"
    fields = '__all__'
    success_url = reverse_lazy('job_list')

class CategoryCreateView(CreateView):
    model = Category
    template_name = "create_category.html"
    fields = ('name', 'image')
    success_url = reverse_lazy('category_list')


class ApplicantCreateView(CreateView):
    model = Applicant
    fields = ('fullname', 'email', 'category', 'job', 'description')
    template_name = "apply_for_job.html"
    success_url = reverse_lazy('job_list')

class ApplicantListView(ListView):
    model = Applicant
    template_name = "applicant_view.html"
    context_object_name = "applicants"

class FilteredApplicantListView(ListView):
    model = Applicant
    template_name = "applicant_filtered_view.html"
    context_object_name = "applicants"
    def get_queryset(self):
        cat = self.request.GET.get('category')
        if cat:
            return Applicant.objects.filter(category=cat)
        return Applicant.objects.all()



