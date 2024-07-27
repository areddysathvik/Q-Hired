from django.shortcuts import render
from django.views.generic import CreateView
from .models import Applications
from users.models import Postings
from django.contrib import messages
from django.urls import reverse_lazy

class ApplicantCreateView(CreateView):
    template_name = 'applications_form.html'
    model = Applications
    fields = ['applicant_name', 'applicant_email', 'resume']
    context_object_name = 'job_details'
    success_url = reverse_lazy('home-applications')

    def form_valid(self, form):
        job_id = self.kwargs['pk'] 
        job = Postings.objects.get(pk=job_id)
        form.instance.job_id = job  
        messages.success(self.request, 'Your application has been submitted successfully!, You can close this Tab Now')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_id = self.kwargs['pk'] 
        job = Postings.objects.get(pk=job_id)
        context['job_details'] = {
            'job_title': job.job_title,
            'job_description': job.job_description,
            'date_posted': job.date_posted,
            'posted_by': job.posted_by
        }
        return context

def home_apply(request):
    return render(request, 'base-apply.html')