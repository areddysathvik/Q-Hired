from django.shortcuts import render
from users.models import Postings
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from django.contrib.auth.models import User
from applications.models import Applications
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    DetailView
)

def download_resume(request, pk):
    application = get_object_or_404(Applications, pk=pk)
    if not application.resume:
        raise Http404("Resume not found")

    response = FileResponse(application.resume, as_attachment=True, filename=application.resume.name)
    return response

class PostedDetailView(DetailView):
    model = Postings
    template_name = 'applications.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_id = self.object.job_id 
        
        context['applications'] = Applications.objects.filter(job_id=self.object)
        
        return context


class PostedListView(ListView):
    template_name = 'home.html'
    context_object_name = 'data'
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return user.posted_jobs.all().order_by('-date_posted')
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = [
            {
                'title': job.job_title, 
                'desc': job.job_description,
                'date_posted': job.date_posted,
                'job_id':job.job_id,
            } 
            for job in self.object_list
        ]
        return context

class PostedCreateView(CreateView):
    template_name = 'postings_form.html'
    model = Postings
    fields = ['job_title', 'job_description', 'min_match_rate_req']
    success_url = '/'
    def form_valid(self ,form):
        form.instance.posted_by = self.request.user

        return super().form_valid(form)
