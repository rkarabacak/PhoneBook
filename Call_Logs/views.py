from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from Call_Logs.models import call_logs
from Call_Logs.forms import CallLogsForm



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
    
    context_object_name = "callid"
    model = call_logs
    template_name = 'calllogs/detail.html'

    def detail_view(request, pk):
        callid = call_logs.objects.get(pk=pk)
        return render(request, 'calllogs/detail.html', context={'callid':callid})