from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import TemplateView, View
from .forms import CreateUserForm

# Create your views here.
class IndexView(TemplateView):
        template_name = 'app/index.html'

class AboutView(TemplateView):
    template_name = 'app/about.html'

class SignupView(TemplateView):
    template_name = 'app/signup.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, "app/index.html")
        form = CreateUserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "app/thanks.html", {'form': form})

        return render(request, self.template_name, {'form': form})

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        return render(
            request,
            self.template_name,
            {
                'error_message':
                'Email or password is incorrect'
            }
        )

class LogoutView(TemplateView):
    template_name = 'app/logout.html'

    def get(self, request,  *args, **kwargs):
        logout(request)
        return redirect('index')


class CheckUserNameView(View):
    def post(self, request):
        username = request.POST.get("username")
        if get_user_model().objects.filter(username=username).exists():
            return HttpResponse("""
                <b style='color:red'>This user name already exists</b>
                <button id="submit-button" disabled="" hx-swap-oob="true" type="submit" class="btn btn-primary btn-disabled btn-lg mt-4" value="Submit">Submit</button>
            """) 
        else:
            return HttpResponse("""
                <button id="submit-button" hx-swap-oob="true" type="submit" class="btn btn-primary btn-lg mt-4" value="Submit">Submit</button>
            """)