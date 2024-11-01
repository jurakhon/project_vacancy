from django.urls import path
from .views import *

urlpatterns = [
    path('',JobListView.as_view(),name='job_list'),
    path('category/', CategoryListView.as_view(),name='category_list'),
    path('createjob/',JobCreateView.as_view(),name='job_create'),
    path('createcategory/',CategoryCreateView.as_view(),name='category_create'),
    path('apply/',ApplicantCreateView.as_view(),name='applicant_create'),
    path('applicantlist/',ApplicantListView.as_view(),name='applicant_list'),
    path('filteredapplicantlist/',FilteredApplicantListView.as_view(),name='filtered_applicant_list'),



]