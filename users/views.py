from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import UpdateView
from users.models import CustomUser
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account Has been Created Successfully You can login Now")
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form':form})


@login_required
def profile(request):
    return HttpResponse(f'Name : {request.user.username}')


class ProfileUpdateView(UpdateView):
    model = CustomUser
    template_name = 'profile.html'
    success_url = '/'
    fields = ['company_name', 'contact_number']
    
    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.request.user.id)

    def form_valid(self, form):
        form.instance.password = self.request.user.password
        form.instance.email = self.request.user.email
        return super().form_valid(form)

