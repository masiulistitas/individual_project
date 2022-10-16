from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listings/', views.listings, name='listings'),
    path('tinymce/', include('tinymce.urls')),
    path('search/', views.search, name='search'),
    path("job_apply/<int:id>/", views.job_apply, name="job_apply"),
    path('faq/', views.faq, name='faq'),
    path("all_jobs/", views.all_jobs, name="all_jobs"),
    path('company_ads/', views.company_ads, name='company_ads'),
    path("edit_job/<int:id>/", views.edit_job, name="edit_job"),
    path("delete_job/<int:id>/", views.delete_job, name="delete_job"),
    path("delete_application/<int:id>/", views.delete_application, name="delete_application"),
    path('company_add/', views.company_add, name='company_add'),
    path("details/<int:id>/", views.job_detail, name="details"),
    path("all_applicants/", views.all_applicants, name="all_applicants"),
    ]


