from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date
from django.db.models import Q
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def listings(request):
    listings = Job.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context=context)


def job_detail(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'details.html', {'job': job})


def faq(request):
    return render(request, 'faq.html')


def search(request):
    listings = Job.objects.all()
    query = request.GET.get('query')
    search_results = Job.objects.filter(Q(title__icontains=query) | Q(location__icontains=query)| Q(skills__icontains=query))
    return render(request, 'search.html', {'jobs': search_results, 'query': query, 'listings': listings})



def company_ads(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    companies = Company.objects.get(user=request.user)
    company_listings = Job.objects.filter(company=companies)

    return render(request, 'company_ads.html', {'company_listings':company_listings})


def company_add(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == "POST":
        title = request.POST['job_title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        salary = request.POST['salary']
        image = request.FILES['logo']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']
        user = request.user
        company = Company.objects.get(user=user)
        job = Job.objects.create(company=company, title=title, start_date=start_date, end_date=end_date, salary=salary,
                                 image=image, experience=experience, location=location, skills=skills,
                                 description=description, creation_date=date.today())
        job.save()
        return redirect('company_ads')
    return render(request, "company_add.html")


def edit_job(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    job = Job.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['job_title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        salary = request.POST['salary']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']

        job.title = title
        job.salary = salary
        job.experience = experience
        job.location = location
        job.skills = skills
        job.description = description

        job.save()
        if start_date:
            job.start_date = start_date
            job.save()
        if end_date:
            job.end_date = end_date
            job.save()
        return redirect('company_ads')
    return render(request, "edit_job.html", {'job': job})


def delete_job(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    job = Job.objects.filter(id=id)
    job.delete()
    return redirect('company_ads')


def all_applicants(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    company = Company.objects.get(user=request.user)
    application = Application.objects.filter(company=company)
    return render(request, "all_applicants.html", {'application':application})


def all_jobs(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    jobs = Job.objects.filter().order_by('-start_date')
    applicant = JobSeeker.objects.get(user=request.user)
    apply = Application.objects.filter(applicant=applicant)
    data = []
    for i in apply:
        data.append(i.job.id)
    return render(request, "all_jobs.html", {'jobs':jobs, 'data':data})


def job_apply(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    applicant = JobSeeker.objects.get(user=request.user)
    job = Job.objects.get(id=id)
    if request.method == "POST":
        resume = request.FILES['resume']
        Application.objects.create(job=job, company=job.company, applicant=applicant, resume=resume, apply_date=date.today())
        return redirect('all_jobs')
    return render(request, "job_apply.html", {'job':job})


def delete_application(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    application = Application.objects.filter(id=id)
    application.delete()
    return redirect('all_applicants')
