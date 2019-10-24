from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from book.models import Contacts
from book.form import ContactsForm


@method_decorator(login_required, name='dispatch') # login olmayan istekleri kabul etmez
class bookListView(ListView):

    model = Contacts
    template_name = 'contacts/index.html'
    context_object_name = 'contacts'

    
    def get_context_data(self, **kwargs):
        context = super(bookListView, self).get_context_data(**kwargs)
        contacts = self.get_queryset()
        return context

@method_decorator(login_required, name='dispatch') # login olmayan istekleri kabul etmez
class bookCreateView(CreateView):
    
    model = Contacts
    form_class = ContactsForm # form_class alanlar için widget uygulamaya yarıyor ve form_class atanırsa fields alanı olmamalı
    template_name = 'contacts/create.html'
   
    success_url = reverse_lazy('book:index')

    

# def create_view(request):
#     form = 

#     pass

# def update_view(request):
#     pass

# def delete_view(request):
#     pass
