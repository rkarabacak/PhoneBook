from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from book.models import Contacts
from book.form import ContactsForm
from django.http import HttpResponse


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

class bookUpdateView(UpdateView):
    model = Contacts
    fields = ['firstName','lastName', 'companyName', 'email', 'phoneNumber1', 'phoneNumber2', 'address']
    template_name = 'contacts/update.html'
    success_url = "/"


# class inlineBookCreateView(CreateView):
    
#     model = Contacts
#     form_class = ContactsForm # form_class alanlar için widget uygulamaya yarıyor ve form_class atanırsa fields alanı olmamalı
#     template_name = 'contacts/create.html'
#     context_object_name= 'data'
#     success_url = render(request, 'calllogs:search', con)

#     def get_context_data(self, **kwargs):
#         context = super(inlineBookCreateView, self).get_context_data(**kwargs)
#         data = data
#         return context
    
def inline_Create_contacts(request, getNumber):
     
    form = ContactsForm(request.POST or None)
    if form.is_valid():
        number = form.save(commit=False)        
        getNumber = number.phoneNumber1
        print(getNumber)
        number.save()
        
        return HttpResponseRedirect(reverse('calllogs:search', kwargs={'data':getNumber}))

    context={        
        'form':form,
        'getNumber':getNumber        
        }
    return render(request, "contacts/create.html", context)
    
    
    # success_url = reverse_lazy('call_logs:search')
    # return HttpResponseRedirect(reverse('book:create2', kwargs={'getNumber':getNumber}))

    


