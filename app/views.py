from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact

# Create your views here.
# def home(request):
#     context = {
#         'contacts': Contact.objects.all(),
#     }
#     return render(request, 'index.html', context)


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'


# def detail(request, id):
#     context = {
#         'contact': get_object_or_404(Contact, pk=id)
#     }
#     return render(request, 'detail.html', context)


class DetailPageView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'


class SearchContactView(LoginRequiredMixin, ListView):
    # template_name = 'search.html'
    # model = Contact

    def get(self, request):
        query = request.GET['query']
        res = Contact.objects.filter(
            Q(name__icontains=query) |
            Q(info__icontains=query) |
            Q(phone__iexact=query)
        )
        context = {
            'query': query,
            'contacts': res
        }
        return render(request, 'search.html', context)


class CreateContactView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name', 'phone', 'email', 'info', 'gender', 'image']
    success_url = '/'


class UpdateContactView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name', 'phone', 'email', 'info', 'gender', 'image']
    success_url = '/'

    def form_valid(self, form):
        instance = form.save()
        return redirect('detail', instance.pk)


class DeleteContact(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    fields = ['name', 'phone', 'email', 'info', 'gender', 'image']
    success_url = '/'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = 'home'
