from django.views.generic import ListView, DetailView, DeleteView, View, CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse

from .models import Item, User, Category
from .forms import UserForm, LoginForm, ItemForm


class IndexView(ListView):
    model = Item
    template_name = 'manager/IndexView.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


class Detail(DetailView):
    model = Item
    template_name = 'manager/DetailView.html'


@login_required()
def pickup_view(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'manager/PickupView.html', {'item': item})


@method_decorator(login_required(), name='dispatch')
class PickupConfirmationView(DeleteView):
    model = Item
    success_url = reverse_lazy('manager:index')


@method_decorator(login_required(), name='dispatch')
class AddItem(CreateView):
    model = Item
    template_name = 'manager/add_item.html'
    form_class = ItemForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.owner_contact = User.objects.get(username=request.user).email
            item.category = form.cleaned_data['category']
            item.name = form.cleaned_data['name']
            item.photo = request.FILES['photo']
            item.description = form.cleaned_data['description']
            item.save()
            return redirect('manager:detail', pk=item.pk)

        else:
            return render(request, self.template_name, {'form': form, 'form.errors': form.errors})

    def get(self, request):
        contact = User.objects.get(username=request.user).email
        form = self.form_class(initial={'owner_contact': contact})
        return render(request, 'manager/add_item.html', {'form': form})


class UserFormView(View):
    form_class = UserForm
    template_name = 'manager/registration.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('manager:index')

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'manager/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('manager:index')

        return HttpResponse('aef')


@method_decorator(login_required(), name='dispatch')
class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('manager:index')
