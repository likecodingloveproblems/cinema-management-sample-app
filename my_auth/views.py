from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from my_auth.forms import RegisterForm

# Create your views here.


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = User.objects.create(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email']
        )
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
