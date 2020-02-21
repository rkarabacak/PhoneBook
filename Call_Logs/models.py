from django.db import models
from django.contrib.auth.models import User
from book.models import Contacts




class call_logs(models.Model):

    callTime = models.DateTimeField(auto_now_add=True, verbose_name='Çağrı Zamanı')
    fromNumber = models.CharField(max_length=16, verbose_name='Arayan')
    toUser  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rn_to_user', verbose_name='Cevaplayan Kullanıcı')    
    note = models.TextField(verbose_name='Not')
    id_contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null= True, related_name='rn_id_contacts', verbose_name='Kayıtlı Firma')


    def __str__(self):
        return self.fromNumber

    class Meta:
        ordering = ['-callTime']