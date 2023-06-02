from django.shortcuts import render, Http404, HttpResponseRedirect, reverse, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from book.models import Contacts
from book.views import bookCreateView
from Call_Logs.models import call_logs
from Call_Logs.forms import CallLogsForm, SCallLogsForm
from django.db.models import Q, When, Count, Case, BooleanField
from django.core.exceptions import ObjectDoesNotExist
import datetime



class callLogsView(ListView):
    
    model = call_logs
    template_name = 'calllogs/index.html'
    context_object_name = 'calllogs'

    
    def get_context_data(self, **kwargs):
        context = super(callLogsView, self).get_context_data(**kwargs)
        calllogs = self.get_queryset()
        return context

class callLogsCreateView(CreateView):

    model = call_logs
    form_class = CallLogsForm # form_class alanlar için widget uygulamaya yarıyor ve form_class atanırsa fields alanı olmamalı
    template_name = 'calllogs/create.html'
   
    success_url = reverse_lazy('calllogs:index')


class calllogsDetailView(DetailView):
    
    context_object_name = "callid "
    model = call_logs
    template_name = 'calllogs/detail.html'

    def detail_view(request, pk):        
        callid = call_logs.objects.get(pk=pk)
        return render(request, 'calllogs/detail.html', context={'callid':callid})

# Kullanılmıyor
# def search_view(request, data):  
    
#     getNumber = data # Kullanılmıyor 



#     try:
#         company = Contacts.objects.get(Q(phoneNumber1=data) | Q(phoneNumber2=data))
#         print(company.id)
#         companyNumbers = call_logs.objects.filter(id_contacts=company.id)
#         print(companyNumbers)
#         reqData = call_logs.objects.all()
#         caller_number = reqData.filter(id_contacts=company.id)
#         rtime = datetime.datetime.now()
#         print(caller_number)
        

#         form = SCallLogsForm(request.POST or None)
#         if form.is_valid():
#             post = form.save(commit=False)
#             user = User.objects.get(id=request.user.id)
#             post.fromNumber = data
#             post.toUser = user            
#             post.id_contacts = Contacts.objects.get(Q(phoneNumber1=data) | Q(phoneNumber2=data))          
#             form.save()
#             return HttpResponseRedirect(reverse('calllogs:index'))

#         context={
#             'rtime': rtime,
#             'data':data,
#             'getNumber':getNumber,
#             'form':form,
#             'caller_number':caller_number,
#             'company': company
#         }
#         return render(request, 'calllogs/search.html', context)
#         # Çağrı geçmişi listeler       

       
#     except Contacts.DoesNotExist:
#         context={
#             'getNumber':getNumber,
#             'data':data
#         }
#         print(context)
        
#         return HttpResponseRedirect(reverse('book:create2', kwargs={'getNumber':getNumber}))
#         # return HttpResponseRedirect(reverse('book:create2', kwargs={'getNumber':getNumber}))

       
    

    
    
#     # return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))
